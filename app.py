from flask import Flask, render_template, request, redirect, url_for
import openai
import os
import csv
import pandas as pd
from config import OPENAI_API_KEY

app = Flask(__name__)

# OpenAI API 키 설정
openai.api_key = OPENAI_API_KEY

# data 폴더가 없으면 생성
if not os.path.exists('data'):
    os.makedirs('data')

@app.route('/')
def index():
    return render_template('input.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)
    
    if file and file.filename.endswith('.txt'):
        text = file.read().decode('utf-8')

        # 첫 번째 GPT 모델 호출: 요약 생성
        summary_response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Please summarize the text in Korean by dividing it into stores in a readable manner so that "
                        "the manager can see it in insights. For example, three cases of dirt, two cases of unkindness, "
                        "and others (you extract keywords). Summarize it simply by the number of cases. "
                        "For example, it should be printed out as follows: 치즈스낵 부스: - 직원 불친절: 2건 - 서비스 속도 느림: 1건 - 음식 정성 부족: 3건 - 매력 없는 메뉴: 1건 타코야끼 부스: - 완전히 익지 않은 타코야끼: 1건 - 위생 상태 불량: 1건 - 직원 무례: 1건 - 주문량 부족: 1건"
                    )
                },
                {
                    "role": "user",
                    "content": text
                }
            ],
            temperature=1,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        summary = summary_response['choices'][0]['message']['content'].strip()

        # 두 번째 GPT 모델 호출: CSV 생성 요청
        csv_response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Please create a CSV file by extracting the number of cases for each title from the summary. "
                        "The CSV file should have columns for Booth, Issue, and Count. "
                        "Please ensure that no commas are included in the Issue column to avoid errors in the CSV format."
                    )
                },
                {
                    "role": "user",
                    "content": summary
                }
            ],
            temperature=1,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        csv_data = csv_response['choices'][0]['message']['content'].strip()

        csv_filename = os.path.join('data', 'summary.csv')

        with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            for line in csv_data.split('\n'):
                writer.writerow(line.split(','))

        return render_template('output.html', original_text=text, summary=summary)

    return redirect(request.url)

@app.route('/analyze', methods=['GET'])
def analyze():
    csv_filename = 'data/summary.csv'
    
    if os.path.exists(csv_filename):
        df = pd.read_csv(csv_filename)

        # 데이터를 부스별로 그룹화하여 Chart.js 형식으로 변환
        chart_data = {
            "labels": df['Issue'].unique().tolist(),
            "datasets": []
        }

        booths = df['Booth'].unique()
        colors = ['rgba(75, 192, 192, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(255, 99, 132, 0.2)']  # 색상 리스트
        border_colors = ['rgba(75, 192, 192, 1)', 'rgba(54, 162, 235, 1)', 'rgba(255, 99, 132, 1)']

        for i, booth in enumerate(booths):
            booth_data = df[df['Booth'] == booth]
            chart_data["datasets"].append({
                "label": booth,
                "data": booth_data.set_index('Issue').reindex(chart_data['labels'], fill_value=0)['Count'].tolist(),
                "backgroundColor": colors[i % len(colors)],
                "borderColor": border_colors[i % len(border_colors)],
                "borderWidth": 1
            })

        return render_template('analysis.html', chart_data=chart_data)
    else:
        return "CSV file not found.", 404


if __name__ == '__main__':
    app.run(debug=True)

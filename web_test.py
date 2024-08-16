"""from flask import Flask, render_template, send_file
import pandas as pd
import os
import chardet

app = Flask(__name__)

# CSV 파일 경로 설정
CSV_FILE_PATH = 'data/summary.csv'

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        return result['encoding']

@app.route('/')
def home():
    return '''
    <h1>Welcome to the Plot Generator</h1>
    <p>Go to <a href="/plot">/plot</a> to see the graph.</p>
    '''

@app.route('/plot')
def plot_csv_data():
    # CSV 파일의 인코딩 감지
    encoding = detect_encoding(CSV_FILE_PATH)
    
    # CSV 파일을 감지된 인코딩으로 읽어 데이터프레임으로 변환
    df = pd.read_csv(CSV_FILE_PATH, encoding=encoding)
    
    # 데이터를 부스별로 그룹화
    booth_data = df.groupby('Booth').apply(lambda x: x[['Issue', 'Count']].to_dict(orient='list')).to_dict()

    # Chart.js에서 사용할 수 있는 형식으로 변환
    chart_data = {
        'labels': df['Issue'].tolist(),
        'datasets': [
            {
                'label': booth,
                'data': data['Count'],
                'backgroundColor': f"rgba({(hash(booth) % 256)}, {(hash(booth) // 256 % 256)}, {(hash(booth) // 256 // 256 % 256)}, 0.6)",
                'borderColor': f"rgba({(hash(booth) % 256)}, {(hash(booth) // 256 % 256)}, {(hash(booth) // 256 // 256 % 256)}, 1)",
                'borderWidth': 1
            }
            for booth, data in booth_data.items()
        ]
    }

    return render_template('plot.html', chart_data=chart_data)

if __name__ == '__main__':
    app.run(debug=True)
"""
"""import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일을 읽어 데이터프레임으로 변환
def create_bar_chart(csv_file_path, output_image_path):
    data = pd.read_csv(csv_file_path)
    
    # 데이터 가공
    data['Cases'] = data['Cases'].astype(int)
    
    # 막대그래프 생성
    plt.figure(figsize=(10, 6))
    plt.bar(data['Title'], data['Cases'], color='skyblue')
    plt.xlabel('Title')
    plt.ylabel('Number of Cases')
    plt.title('Number of Cases per Title')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # 그래프 이미지를 저장
    plt.savefig(output_image_path)
    plt.close()

if __name__ == '__main__':
    create_bar_chart('data/summary.csv', 'static/summary_chart.png')"""

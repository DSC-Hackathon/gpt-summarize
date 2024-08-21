# LLM 모델 기반 요약 및 CSV 파일 생성 후 시각화

## 관리자 페이지 구현

### 1. Flask
- Flask를 사용하여 관리자가 사용할 수 있는 웹 애플리케이션을 생성하였습니다.

### 2. GPT (GPT-4 모델)
- GPT-4 모델을 활용하여 **Prompt Engineering** 과정을 통해 대량의 텍스트를 요약합니다.
- 예시: 아래와 같이 대량의 텍스트에서 부정적인 내용을 인식하고 건수로 요약합니다.  
  ![Example Image](https://github.com/user-attachments/assets/bf8cb826-7f01-4a9d-94e0-482cb5c5f09c)

### 3. GPT-2
- 요약된 내용을 바탕으로 내용과 건수를 컬럼으로 작성한 CSV 파일을 생성하여 `data` 폴더에 저장합니다.  
  ![CSV File Creation](https://github.com/user-attachments/assets/50aa3aa6-30cb-460a-a483-d4e52c0926d1)

### 4. 시각화
- 생성된 CSV 파일을 통해 데이터를 시각화합니다.  
  ![Visualization Example](https://github.com/user-attachments/assets/8ea3855f-eea3-450b-bdb0-7831ef4f3c86)

## Trouble Shooting

- **Flask config.py 파일에서 키 값 인식 오류**  
  텍스트를 잘못 인식한 것이 원인이었습니다.

- **GPT Prompt Engineering 과정의 어려움**  
  GPT 모델을 튜닝하여 문제를 해결하였습니다.

## 향후 계획

- GPT 모델의 파인튜닝을 통해 성능을 강화할 예정입니다.
- 로드 밸런싱을 진행할 계획입니다.

# LLM 모델 기반 요약 및 CSV 파일 생성 후 시각화

## 관리자 페이지 구현

### Problems
- 지방 인구 소멸화 문제
- 축제 관리 및 모니터링의 어려움
- 리플렛 사용의 비효율성

### Solution
- **축제 관리자 전용 어플리케이션**: 축제를 관리하고 모니터링할 수 있는 전용 앱 개발
- **축제 관광객 전용 지도 및 리뷰 서비스 제공**: 관광객에게 편리한 지도 및 리뷰 서비스 제공

### Effect
- **인구유입**: 지방 인구 소멸화 문제를 해결하기 위해 축제를 활성화하여 인구 유입을 유도할 수 있습니다.
- **모니터링**: 앱에서 민원을 받고, 관리자 전용 웹을 통해 분석된 인사이트를 제공하여 피드백을 강화할 수 있습니다.
- **더 나은 플랫폼으로의 확장**: 현재 플랫폼을 더 나은 방향으로 확장할 계획입니다.
- **꿀잼도시 대전**: 도시의 활성화를 위해 재미있는 요소들을 결합합니다.
- **리플렛 소요 감소**: 행사 전용 어플리케이션을 통해 리플렛 사용을 줄이고, 지도를 통해 부스를 간편하게 자신의 위치정보로 확인하고, 민원을 통해 문제를 해결할 수 있습니다.


## 나의 역할 및 진행사항
- **팀장**
- **ML engineer**

### 프로젝트 도구
- **Jupyter Lab**
- **VScode**
- **GitHub**
- **Slack**
- **Notion**

### 1. Flask
- Flask를 사용하여 관리자가 사용할 수 있는 웹 애플리케이션을 생성했습니다.

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

### 5. 프로세스
- 프로젝트의 전체적인 프로세스는 아래와 같습니다.  
  ![Process Image](https://github.com/user-attachments/assets/3460b980-becb-4da6-8907-9bb38cb8559f)

## Trouble Shooting

- **Flask config.py 파일에서 키 값 인식 오류**  
  텍스트를 잘못 인식한 것이 원인이었습니다.

- **GPT Prompt Engineering 과정의 어려움**  
  GPT 모델을 튜닝하여 문제를 해결하였습니다.

## 향후 계획

- GPT 모델의 파인튜닝을 통해 성능을 강화할 예정입니다.
- 로드 밸런싱을 진행할 계획입니다.

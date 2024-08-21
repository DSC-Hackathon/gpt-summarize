![image](https://github.com/user-attachments/assets/e9b911fc-95d9-494f-a7b7-7e02631d7bd1)

* LLM모델 기반 요약 및 csv파일 생성 후 시각화

관리자 페이지 구현

1. flask
  - flask를 통해 관리자가 사용할 수 있는 웹을 생성하였습니다.
2. gpt
  - gpt4 모델을 통해 prompt engineering 과정을 거쳐 대량의 텍스트를 요약합니다.
  - ![image](https://github.com/user-attachments/assets/bf8cb826-7f01-4a9d-94e0-482cb5c5f09c)
  - 다음과 같이 대량의 텍스트에서 부정적인 텍스트를 인식 후 건수로 요약합니다.

3. gpt - 2
  - 요약된 내용을 통해 내용과 건수를 컬럼으로 작성된 csv파일을 생성하여 data폴더에 저장합니다.
  - ![image](https://github.com/user-attachments/assets/50aa3aa6-30cb-460a-a483-d4e52c0926d1)

4. 시각화
  - 해당 csv파일을 통해 시각화를 진행합니다.
  - ![image](https://github.com/user-attachments/assets/8ea3855f-eea3-450b-bdb0-7831ef4f3c86)

Trouble Shooting
  - 키 값을 넣는데 왜 자꾸 config.py파일에 왜 키를 인식할수가 없을까 고민 --> 텍스트로 인식하게 해서 난 오류
  - GPT Prompt Engineering 프롬포트 엔지니어링 하는 과정에서 고난 --> - gpt모델을 튜닝

향후 계획
  - GPT모델 파인튜닝을 통해 모델을 강화
  - 로드밸런싱 진행



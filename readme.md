# 2020 임베디드 시스템 및 설계

## Dependencies

https://pytorch.org/get-started/locally/ 에 접속하여 본인의 플랫폼에 맞는 방법으로 pytorch 설치.

아래도 설치.

```
pip install opencv-python
```

## 실행

실행 전 본인의 아이피 주소를 코드에 입력해야 함.

```
cd src/raspberry

# PC에서 (NetworkCar에 아이피 주소 입력 필수)
python socket-laptop.py

# 라즈베리파이에서 (connect 함수에 아이피 주소 입력 필수)
python3 socket-rasp.py

# PC에서 학습하기 위한 스크립트
python main-training.py

# PC에서 학습 결과를 확인하기 위한 스크립트
python test-prediction-viewer.py

```

## 조작법

socket-laptop.py 를 실행하면 0을 입력해 데이터수집 가능.

w a d 로 움직이며 c 를 누르면 버퍼 클리어, o를 누르면 데이터를 파일로 저장.


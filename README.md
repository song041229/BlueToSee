# BlueToSee
BlueToSee 앱의 face_recognition 부분

## 시작하기 전
다음의 라이브러리를 설치하여야 한다:

- OpenCV
- cvzone
- numpy
- face_recognition
- tkinter

```
pip install dlib
pip install cmake
pip install opencv-python
pip install cvzone
pip install numpy
pip install face_recognition
pip install tk
```

## 사용법
#### 1. 캠 설정하기 : 자신의 캠 설정에 맞게 설정하기
```
# <매개변수> - 17 line
# 0: 기본 캠, 1이상: 외부 캠
cap = cv.VideoCapture(0)
```

#### 2. 파일 경로 자신에 맞게 바꾸기
```
# main.py | Background 경로 - 36 line
imgBackground = cv.imread('./Resources/background/Background.png')

# main.py | mode에 있는 image들을 import하기 - 39 line
folderModePath = './Resources/Modes'

# EncodeGenerator.py | '../images' 경로 저장하기 - 7 line
folderPath = './Resources/Modes'
```

#### 3. EncodeGenerator.py에서 Modes 파일에 있는 이미지 encoding하기

#### 4. main.py 실행하기

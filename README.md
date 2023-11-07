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
# <매개변수>
# 0: 기본 캠, 1이상: 외부 캠
cap = cv.VideoCapture(0)
```

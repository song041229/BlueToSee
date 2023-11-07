# BlueToSee
BlueToSee 앱의 face_recognition 부분을 다루고 있다. 

카메라 버튼을 클릭했을 때, 이 코드가 실행되며 face recognition을 통해 이름이 return된다.

## 시작하기 전
참고로 모델 사용은 하지 않았다. 사진을 최소한(1장)으로 사용하기 때문에 필요없다고 판단하였다.


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

## 사용 방법
#### 1. 캠 설정하기 : 자신의 캠 설정에 맞게 설정하기
```
# <매개변수> - 17 line
# 0: 기본 캠, 1이상: 외부 캠
cap = cv.VideoCapture(0)
```

#### 2. 파일 경로 자신에 맞게 바꾸기
```
# main.py : Background 경로 - 36 line
imgBackground = cv.imread('./Resources/background/Background.png')

# main.py : mode에 있는 image들을 import하기 - 39 line
folderModePath = './Resources/Modes'

# EncodeGenerator.py : '../images' 경로 저장하기 - 7 line
folderPath = './Resources/Modes'
```

#### 3. EncodeGenerator.py에서 Modes 파일에 있는 이미지 encoding하기

#### 4. main.py 실행하기


## 라이선스
This project is licensed under the MIT License.

## 참고 자료
> [한땀한땀 딥러닝 컴퓨터 비전 백과사전](https://wikidocs.net/151311)

> [GhostFaceNets](https://github.com/HamadYA/GhostFaceNets)

> [Face Recognition with Real Time Database | 2 Hour Course | Computer Vision](https://www.youtube.com/watch?v=iBomaK2ARyI&ab_channel=Murtaza%27sWorkshop-RoboticsandAI)

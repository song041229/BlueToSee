import cv2 as cv
import cvzone
import numpy as np
import os
import pickle
import face_recognition
import tkinter as tk



# 화면에 뜨는 창 위치 조정
x = 600
y = 20

# TODO : 웹캠 설정하기
# 웹캠의 번째 수 (3번째 - 외부캠)
cap = cv.VideoCapture(3)


def display_text():

    root = tk.Tk()
    root.title("이름")
    root.geometry("250x70+" + str(x+30) + "+" + str(y+600))

    name = nameArr[np.argmax(nameCountArr)]

    # 텍스트 라벨 생성
    text_label = tk.Label(root, text=name, font=("Helvetica", 18))
    text_label.pack(pady=20)

    root.mainloop()


# Background 경로
imgBackground = cv.imread('./Resources/background/Background.png')

# mode에 있는 image들을 import하기
folderModePath = './Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []

# Resources/Modes/... 에 있는 파일 추가하기
for path in modePathList:
    imgModeList.append(cv.imread(os.path.join(folderModePath, path)))

# encoding한 파일 Load하기
print("Loading Encode File...")
file = open('EncodeFile.p', 'rb')
encodeListKnownWithId = pickle.load(file)
file.close()

# encode 할 때 설정했던 list 불러오기
encodeListKnown, personId = encodeListKnownWithId
print("Encode File Loaded")



# 얼마나 이름 count를 할 지 정하기 (정확도 상승)
count = 0
MAX_COUNT = 10

# 찾은 얼굴의 index 파악 (personId를 name으로 바꾸기 위함)
nameCountArr = [0] * len(personId)
nameArr = []
for i in range(len(personId)):
    nameArr.append(personId[i])


# 시작
while True:
    success, img = cap.read()

    # img : 실제 Background에 들어가는 capture한 이미지
    img = cv.resize(img, (367, 415), None, 0.595, 0.75)
    # imgS : img를 이미지 처리에 쓰이는 용도로 변환
    imgS = cv.resize(img, (0, 0), None, 0.75, 0.75)
    imgS = cv.cvtColor(imgS, cv.COLOR_BGR2RGB)

    # face
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    imgBackground[130:415 + 130, 0:367] = img

    # faceDis : face distance
    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):

        # face recognition - encoding 되어 있는 얼굴들의 list에서 인식한 encodeFace와 비교
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print("match : ", matches)
        print("faceDis", faceDis)

        # matchIndex 출력하기
        matchIndex = np.argmin(faceDis)
        print("MatchIndex", matchIndex)

        # face detection -> img에 fece 검출
        if matches[matchIndex]:
            print("Known Face detected")
            print(personId[matchIndex])

            y1, x2, y2, x1 = faceLoc
            bbox = x1 + 50, y1 + 90, x2 - 80, y2 - 60
            cvzone.cornerRect(imgBackground, bbox, l=20, t=3, rt=0)

            count += 1
            nameCountArr[matchIndex] += 1


        if count % MAX_COUNT == 0 and count != 0:
            display_text()



    # video를 잘 인식했다면 imshow() 함수로 보여줌
    if (success):
        cv.imshow("Background", imgBackground)
        cv.moveWindow("Background", x, y)

        # esc 키를 누르면 닫음
        if cv.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv.destroyAllWindows()
import cv2 as cv
import face_recognition
import pickle
import os

# '../images' 경로 저장하기
folderPath = './Resources/Modes'
# or.listdir() : './Resources/image' 경로에 있는 모든 파일 불러오기
pathList = os.listdir(folderPath)

# imgList = 사진, personId = [040808, 041229, ...]
imgList = []
personId = []

for path in pathList:
    # 각각의 imgList와 personId를 저장하기
    imgList.append(cv.imread(os.path.join(folderPath, path)))
    personId.append(os.path.splitext(path)[0])


def findEncodings(imagesList):

    # encodeList = encoding할 사진 저장
    encodeList = []
    for img in imagesList:
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


# 인코딩 시작
print("Encoding started...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithId = [encodeListKnown, personId]
print("Encoding finished")

# 인코딩한 파일 저장
file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithId, file)
file.close()
print("File saved")

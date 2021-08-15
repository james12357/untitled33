import cv2
from pyzbar import pyzbar
from tkinter.messagebox import showinfo
found = set()
capture = cv2.VideoCapture(0)
PATH = "test.csv"
while True:
    ret, frame = capture.read()
    test = pyzbar.decode(frame)
    for tests in test:
        testData = tests.data.decode('utf-8')
        showinfo("找到", testData)
        print(testData)
    cv2.imshow('Test', frame)
    if cv2.waitKey(1) == ord('q'):
        break

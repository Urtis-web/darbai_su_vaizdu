import cv2

faceCascade = cv2.CascadeClassifier(r'C:\Users\Urtis\PycharmProjects\Darbai_su_vaizdu/haarcascade_frontface_default.xml')
img = cv2.imread(r'C:\Users\Urtis\PycharmProjects\Darbai_su_vaizdu\veidai.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)



cv2.imshow("Image", img)
cv2.waitKey(0)
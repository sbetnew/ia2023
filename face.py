import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haar_face.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Classificador
    face = face_cascade.detectMultiScale(gray, 1.1, 3)

    #Desenhar os retângulos em cada carro
    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0), 2)
        cv2.imshow('video', frame)
        crop_img = frame[y:y+h, x:x+w]
    
    #Tecla de saída
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

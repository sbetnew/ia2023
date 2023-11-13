import cv2

cap = cv2.VideoCapture('people.mp4')
people_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Classificador
    people = people_cascade.detectMultiScale(gray, 1.1, 3)

    #Desenhar os retângulos em cada pessoa
    for (x,y,w,h) in people:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, 'Pessoa', (x + 6, y - 6), font, 0.5, (0,255,0), 1 )
        cv2.imshow('video', frame)
        crop_img = frame[y:y+h, x:x+w]
    
    #Tecla de saída
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

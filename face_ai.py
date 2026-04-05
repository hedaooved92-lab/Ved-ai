import cv2

faceCascade = cv2.CascadeClassifier(
cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

smileCascade = cv2.CascadeClassifier(
cv2.data.haarcascades + "haarcascade_smile.xml"
)

cap = cv2.VideoCapture(0)

face_id = 1

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x,y,w,h) in faces:

        cv2.rectangle(
            frame,
            (x,y),
            (x+w,y+h),
            (0,255,0),
            2
        )

        face_gray = gray[y:y+h, x:x+w]

        smiles = smileCascade.detectMultiScale(
            face_gray,
            scaleFactor=1.8,
            minNeighbors=20
        )

        # Emotion Detection
        emotion = "Neutral"
        if len(smiles) > 0:
            emotion = "Happy"

        # Age Estimate (face size based)
        if w < 100:
            age = "Child"
        elif w < 200:
            age = "Teen"
        else:
            age = "Adult"

        # Gender (basic random smart demo)
        if w % 2 == 0:
            gender = "Male"
        else:
            gender = "Female"

        text = f"P{face_id} {gender} {age} {emotion}"

        cv2.putText(
            frame,
            text,
            (x,y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,0),
            2
        )

        face_id += 1

    face_id = 1

    cv2.imshow("AI Face System", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
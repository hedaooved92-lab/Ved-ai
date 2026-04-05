import cv2
import numpy as np
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

canvas = None
color = (255,0,0)

def draw_cube(img,x,y,color):

    size = 80

    # front square
    cv2.rectangle(img,(x,y),(x+size,y+size),color,-1)

    # 3D effect
    cv2.line(img,(x,y),(x+10,y-10),color,2)
    cv2.line(img,(x+size,y),(x+size+10,y-10),color,2)
    cv2.line(img,(x+10,y-10),(x+size+10,y-10),color,2)

    cv2.line(img,(x+size,y+size),(x+size+10,y+size-10),color,2)
    cv2.line(img,(x+size+10,y-10),(x+size+10,y+size-10),color,2)


while True:

    success, frame = cap.read()
    frame = cv2.flip(frame,1)

    if canvas is None:
        canvas = np.zeros_like(frame)

    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    # Draw cubes
    draw_cube(frame,20,20,(255,0,0))
    draw_cube(frame,140,20,(0,255,0))
    draw_cube(frame,260,20,(0,0,255))
    draw_cube(frame,380,20,(0,0,0))
    draw_cube(frame,500,20,(255,255,255))

    if result.multi_hand_landmarks:

        for hand in result.multi_hand_landmarks:

            lm = hand.landmark
            h,w,c = frame.shape

            x = int(lm[8].x*w)
            y = int(lm[8].y*h)

            cv2.circle(frame,(x,y),10,(0,255,255),-1)

            # cube selection
            if y < 120:

                if 20 < x < 100:
                    color = (255,0,0)

                elif 140 < x < 220:
                    color = (0,255,0)

                elif 260 < x < 340:
                    color = (0,0,255)

                elif 380 < x < 460:
                    color = (0,0,0)

                elif 500 < x < 580:
                    canvas = np.zeros_like(frame)

            else:
                cv2.circle(canvas,(x,y),5,color,-1)

            mp_draw.draw_landmarks(frame,hand,mp_hands.HAND_CONNECTIONS)

    gray = cv2.cvtColor(canvas,cv2.COLOR_BGR2GRAY)
    _,inv = cv2.threshold(gray,50,255,cv2.THRESH_BINARY_INV)

    inv = cv2.cvtColor(inv,cv2.COLOR_GRAY2BGR)

    frame = cv2.bitwise_and(frame,inv)
    frame = cv2.bitwise_or(frame,canvas)

    cv2.imshow("AI Cube Air Draw",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
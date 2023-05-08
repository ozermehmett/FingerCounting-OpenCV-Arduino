import cv2
import mediapipe
import math
import serial

cap = cv2.VideoCapture(0)

ser = serial.Serial('COM8', 9600)

npHands = mediapipe.solutions.hands
hands = npHands.Hands()
npDraw = mediapipe.solutions.drawing_utils
while True:
    ret, frame = cap.read()

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    hlms = hands.process(rgb)

    height, width, channel = frame.shape

    if hlms.multi_hand_landmarks:
        for handlandmarks in hlms.multi_hand_landmarks:
            finger_count = 0
            for fingerNum, landmark in enumerate(handlandmarks.landmark):
                positionX, positionY = int(landmark.x * width), int(landmark.y * height)

                if fingerNum in [4, 8, 12, 16, 20]:
                    if fingerNum == 4:
                        x1, y1 = positionX, positionY
                        x2, y2 = int(handlandmarks.landmark[0].x * width), int(handlandmarks.landmark[0].y * height)
                        x3, y3 = int(handlandmarks.landmark[5].x * width), int(handlandmarks.landmark[5].y * height)
                        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
                        if angle < 0:
                            angle += 360
                        if angle < 90:
                            continue

                    if landmark.y < handlandmarks.landmark[fingerNum - 2].y:
                        finger_count += 1

                ser.write(str(finger_count).encode())

            # parmak sayısını ekrana yazdır
            cv2.putText(frame, f"Finger Count: {finger_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

            npDraw.draw_landmarks(frame, handlandmarks, npHands.HAND_CONNECTIONS)

    cv2.imshow("FRAME", frame)

    if cv2.waitKey(50) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
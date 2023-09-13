import cv2
import mediapipe
import math
import serial

#start camera
cap = cv2.VideoCapture(0)

#COM port and baud rate
ser = serial.Serial('COM8', 9600)

#create objects with mediaPipe
npHands = mediapipe.solutions.hands
hands = npHands.Hands()
npDraw = mediapipe.solutions.drawing_utils

#start loop
while True:
    #read frame
    ret, frame = cap.read()

    #bgr to rgb
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #hand detection
    hlms = hands.process(rgb)

    #Get the dimensions
    height, width, channel = frame.shape

    #If hands are detected
    if hlms.multi_hand_landmarks:
        for handlandmarks in hlms.multi_hand_landmarks:

            #Initialize finger count
            finger_count = 0
            for fingerNum, landmark in enumerate(handlandmarks.landmark):
                #Get the positions
                positionX, positionY = int(landmark.x * width), int(landmark.y * height)

                #For the fingers of interest
                if fingerNum in [4, 8, 12, 16, 20]:

                    #Get the positions of finger tips
                    if fingerNum == 4:
                        x1, y1 = positionX, positionY
                        x2, y2 = int(handlandmarks.landmark[0].x * width), int(handlandmarks.landmark[0].y * height)
                        x3, y3 = int(handlandmarks.landmark[5].x * width), int(handlandmarks.landmark[5].y * height)

                        #calculate the angle between two finger
                        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))

                        #change the angle to positive
                        if angle < 0:
                            angle += 360
                        if angle < 90:
                            continue

                    #Compare with a specific finger height
                    if landmark.y < handlandmarks.landmark[fingerNum - 2].y:
                        finger_count += 1

                #Send the finger count to Arduino 
                ser.write(str(finger_count).encode())

            # show finger count
            cv2.putText(frame, f"Finger Count: {finger_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            npDraw.draw_landmarks(frame, handlandmarks, npHands.HAND_CONNECTIONS)

    #show the frame
    cv2.imshow("FRAME", frame)

    #break the loop by "q"
    if cv2.waitKey(50) & 0xFF == ord("q"):
        break

#release camera and close the window
cap.release()
cv2.destroyAllWindows()

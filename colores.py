import cv2
import imutils
import numpy as np

print("corriendo")

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)






while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    amarillo_osc = np.array([20, 70, 120])
    amarillo_cl = np.array([40, 255, 255])

    rojo_osc = np.array([0, 70, 50])
    rojo_cl = np.array([10, 255, 255])

    verde_osc = np.array([40, 70, 50])
    verde_cl = np.array([80, 255, 255])

    azul_osc = np.array([90, 70, 50])
    azul_cl = np.array([130, 255, 255])

    negro_oscuro = np.array([0, 0, 0])
    negro_claro = np.array([179, 255, 30])

    rosa_oscuro = np.array([140, 70, 50])
    rosa_claro = np.array([170, 255, 255])

    morado_oscuro = np.array([120, 70, 50])
    morado_claro = np.array([150, 255, 255])

    naranja_oscuro = np.array([11, 70, 50])
    naranja_claro = np.array([25, 255, 255])





    cara1 = cv2.inRange(hsv, amarillo_osc, amarillo_cl)
    cara2 = cv2.inRange(hsv, rojo_osc, rojo_cl)
    cara3 = cv2.inRange(hsv, verde_osc, verde_cl)
    cara4 = cv2.inRange(hsv, azul_osc, azul_cl)
    cara5 = cv2.inRange(hsv, negro_oscuro, negro_claro)
    cara6 = cv2.inRange(hsv, rosa_oscuro, rosa_claro)
    cara7 = cv2.inRange(hsv, morado_oscuro, morado_claro)
    cara8 = cv2.inRange(hsv, naranja_oscuro, naranja_claro)

    conts1 = cv2.findContours(cara1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    conts1 = imutils.grab_contours(conts1)

    conts2 = cv2.findContours(cara2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    conts2 = imutils.grab_contours(conts2)

    conts3 = cv2.findContours(cara3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    conts3 = imutils.grab_contours(conts3)

    conts4 = cv2.findContours(cara4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    conts4 = imutils.grab_contours(conts4)

    conts5 = cv2.findContours(cara5, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    conts5 = imutils.grab_contours(conts5)

    conts6 = cv2.findContours(cara6, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    conts6 = imutils.grab_contours(conts6)

    conts7 = cv2.findContours(cara7, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    conts7= imutils.grab_contours(conts7)
    
    conts8 = cv2.findContours(cara8, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    conts8 = imutils.grab_contours(conts8)


    for c in conts1:
        area1 = cv2.contourArea(c)
        if area1 > 5000:
            cv2.drawContours(frame, [c], -1, (30, 255, 255), 3)
            M = cv2.moments(c)
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Amarillo", (cx - 20, cy - 20), cv2.FONT_ITALIC, 1, (255, 255, 255), 2)

    for c in conts2:
        area2 = cv2.contourArea(c)
        if area2 > 5000:
            cv2.drawContours(frame, [c], -1, (0, 0, 255), 3)
            M = cv2.moments(c)
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Rojo", (cx - 20, cy - 20), cv2.FONT_ITALIC, 1, (255, 255, 255), 2)

    for c in conts3:
        area3 = cv2.contourArea(c)
        if area3 > 5000:
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
            M = cv2.moments(c)
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Verde", (cx - 20, cy - 20), cv2.FONT_ITALIC, 1, (255, 255, 255), 2)

    for c in conts4:
        area4 = cv2.contourArea(c)
        if area4 > 5000:
            cv2.drawContours(frame, [c], -1, (255, 0, 0), 3)
            M = cv2.moments(c)
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Azul", (cx - 20, cy - 20), cv2.FONT_ITALIC, 1, (255, 255, 255), 2)

    for c in conts5:
        area5 = cv2.contourArea(c)
        if area5 > 5000:
            cv2.drawContours(frame, [c], -1, (0, 0, 0), 3)
            M = cv2.moments(c)
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Negro", (cx - 20, cy - 20), cv2.FONT_ITALIC, 1, (255, 255, 255), 2)

    for c in conts6:
        area6 = cv2.contourArea(c)
        if area6 > 5000:
            cv2.drawContours(frame, [c], -1, (230, 0, 255), 3)
            M = cv2.moments(c)
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Rosa", (cx - 20, cy - 20), cv2.FONT_ITALIC, 1, (255, 255, 255), 2)

    for c in conts7:
        area7 = cv2.contourArea(c)
        if area7 > 5000:
            cv2.drawContours(frame, [c], -1, (255, 0, 213), 3)
            M = cv2.moments(c)
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Morado", (cx - 20, cy - 20), cv2.FONT_ITALIC, 1, (255, 255, 255), 2)

    for c in conts8:
        area8 = cv2.contourArea(c)
        if area8 > 5000:
            cv2.drawContours(frame, [c], -1, (0, 162, 255), 3)
            M = cv2.moments(c)
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Naranja", (cx - 20, cy - 20), cv2.FONT_ITALIC, 1, (255, 255, 255), 2)



  
    cv2.imshow("Video", frame)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
    
    
    
    
 

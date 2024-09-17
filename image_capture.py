import cv2

save_dir = 'images/'

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

count = 0

while True:
    _, frame = cap.read()

    frame = cv2.flip(frame, 1)

    cv2.imshow("frame", frame)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('k'):
        cv2.imwrite(f'{save_dir}img_{count}.jpg', frame)
        count += 1
    elif(k == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
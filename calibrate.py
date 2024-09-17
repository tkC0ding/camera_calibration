import cv2
import numpy as np
import os

image_path = 'images/'

images = os.listdir(image_path)

chessboard_size = (9, 6)
square_size = 3.0 #cm
image_path = 'images/'

objp = np.hstack([np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2), np.zeros((chessboard_size[0]*chessboard_size[1], 1))])*square_size

object_points = []
image_points = []

images = os.listdir(image_path)

for image in images:
    frame = cv2.imread(f'{image_path}{image}')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray, chessboard_size, None, None)

    if ret:
        object_points.append(objp)

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.01)
        corners_final = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)

        image_points.append(corners_final)

        iamge = cv2.drawChessboardCorners(frame, chessboard_size, corners_final, ret)
        cv2.imshow("points", image)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            continue
    else:
        print("no chessboard corners found")
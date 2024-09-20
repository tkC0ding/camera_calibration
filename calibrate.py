import cv2
import numpy as np
import os

chessboard_size = (8, 5) #(number_squares_x - 1, number_squares_y - 1)
square_size = 0.0275 #m
image_path = 'images/'
image_size = (640, 480) #(w,h)

objp = np.zeros((chessboard_size[0] * chessboard_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:chessboard_size[1], 0:chessboard_size[0]].T.reshape(-1, 2)
objp = objp * square_size

object_points = []
image_points = []

images = os.listdir(image_path)

for image in images:
    frame = cv2.imread(f'{image_path}{image}')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray, chessboard_size, None)

    if ret:
        object_points.append(objp)

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.01)
        corners_final = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)

        image_points.append(corners_final)

        img = cv2.drawChessboardCorners(frame, chessboard_size, corners_final, ret)
        cv2.imshow("points", img)
        cv2.waitKey(1000)
    else:
        print("no chessboard corners found")
cv2.destroyAllWindows()

rep, camera_matrix, dist_coeff, rvecs, tvecs = cv2.calibrateCamera(object_points, image_points, image_size, None, None)

np.savez("calibration.npz", camera_matrix=camera_matrix, dist_coeff=dist_coeff, rvecs=rvecs, tvecs=tvecs)
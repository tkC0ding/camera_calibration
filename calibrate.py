import cv2
import numpy as np
import os

chessboard_size = (9, 6)
square_size = 3.0 #cm
image_path = 'images/'
image_size = (640, 480)

objp = np.hstack([np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2), np.zeros((chessboard_size[0]*chessboard_size[1], 1))])*square_size

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

        iamge = cv2.drawChessboardCorners(frame, chessboard_size, corners_final, ret)
        cv2.imshow("points", image)
        cv2.waitKey(500)
    else:
        print("no chessboard corners found")
cv2.destroyAllWindows()

rep, camera_matrix, dist_coeff, rvecs, tvecs = cv2.calibrateCamera(object_points, image_points, image_size, None, None)

np.savez("calibration.npz", camera_matrix=camera_matrix, dist_coeff=dist_coeff, rvecs=rvecs, tvecs=tvecs)
import cv2
import numpy as np
import os

calibration_data = np.load('calibration_files/calibration.npz')

camera_matrix = calibration_data['camera_matrix']
dist_coeffs = calibration_data['dist_coeff']

image_path = 'images/'
images = os.listdir(image_path)


for image in images:
    img_path = f'{image_path}{image}'
    img = cv2.imread(img_path)

    new_camera_matrix, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, dist_coeffs, (640,480), 1, (640,480))

    dst = cv2.undistort(img, camera_matrix, dist_coeffs, None, new_camera_matrix)

    x, y, w, h = roi
    dst = dst[y:y+h, x:x+w]

    cv2.imshow('caliresutl2', dst)
    cv2.waitKey(3000)
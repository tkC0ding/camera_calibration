import cv2
import numpy as np
import os

image_path = 'images/'

images = os.listdir(image_path)

chessboard_size = (9, 6)
square_size = 3.0 #cm

objp = np.hstack([np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2), np.zeros((chessboard_size[0]*chessboard_size[1], 1))])*square_size

object_points = []
image_points = []
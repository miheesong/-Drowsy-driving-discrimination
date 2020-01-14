import numpy as np
import cv2

def faceangle(frame, facialpoints):
    
    _2d_points = np.array([facialpoints[0], facialpoints[1], facialpoints[2], facialpoints[3], facialpoints[4], facialpoints[5]], dtype = "double")
    _3d_points = np.array([(0.0, 0.0, 0.0), (0.0, -330.0, -65.0), (-225.0, 170.0, -135.0), (225.0, 170.0, -135.0), (-150.0, -150.0, -125.0), (150.0, -150.0, -125.0)])

    camera = np.array([[frame.shape[1], 0, frame.shape[1]/2], [0, frame.shape[1], frame.shape[0]/2], [0, 0, 1]], dtype = "double")

    (_, r_vector, t_vector) = cv2.solvePnP(_3d_points, _2d_points, camera, np.array([[0], [0], [0], [0]]))

    r_matrix = cv2.Rodrigues(r_vector)[0]
    angles = cv2.decomposeProjectionMatrix(np.hstack((r_matrix, t_vector)))[-1]

    result = 0

    if angles[0] > 0:
        result = float(180-angles[0])
    elif angles[0] < 0:
        result = float(-180-angles[0])

    return result

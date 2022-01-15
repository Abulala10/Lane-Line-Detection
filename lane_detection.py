"""

import os
import numpy as np
from matplotlib import pyplot as plt
import operator
import cv2


def regionOfInterest(_image, _vertices):
    """
    Function to crop image or video
    :param _vertices: Are according to X and Y axis [example if x axis is from 0 - 100]
    :param _image: image or frame of a video until in runs
    :return: masked_image
    """

    try:
        mask = np.zeros_like(_image)
        # channel_count = _image.shape[2]
        match_mask_color = 255  # (255, ) * channel_count
        cv2.fillPoly(mask, _vertices, match_mask_color)
        masked_image = cv2.bitwise_and(_image, mask)
        return masked_image

    except Exception as e:
        print("Error in Function region of Interest " + str(e))


def draw_lines(img, lines):
    """

    :param img: image or frame of a video until in runs
    :param lines: lines as in HoughLines
    :return:
    """
    img = np.copy(img)  # copying image
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            print("X1 - %s Y1 - %s.\nX2 - %s Y2 - %s." % (x1, y1, x2, y2))
            cv2.line(blank_image, (x1, y1), (x2, y2), (100, 255, 0), thickness=5)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)  # image, alpha, 2nd image, beta, gamma
    return img


# image = cv2.imread(image_location)
def processEntireCode(image):
    """
    This Function acts a main Function
    :param image: image or frame of a video until in runs
    :return: image_with_lines
    """
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    print("HEIGHT --> %s ::: WIDTH --> %s" % (height, width))
    region_of_interest_vertices = [(0, height), (width / 1.9, height / 1.78), (width, height)]
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    canny_image = cv2.Canny(gray_image, 100, 120)
    cropped_image = regionOfInterest(canny_image, np.array([region_of_interest_vertices], np.int32), )
    lines = cv2.HoughLinesP(cropped_image, rho=10, theta=np.pi / 60, threshold=160, lines=np.array([]),
                            minLineLength=60, maxLineGap=100)
    image_with_lines = draw_lines(image, lines)
    return image_with_lines


def readVideo(_video):
    """
    Function to get video or image
    :param _video location of video image
    :return: video and frame
    """

    try:
        vid = cv2.VideoCapture(_video)
        while vid.isOpened():
            flags, frame = vid.read()
            frame = processEntireCode(frame)
            cv2.imshow("VIDEO", frame)
            if cv2.waitKey(25) & 0XFF == ord('q'):
                break
        vid.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print("Error in readVideo Function " + str(e))


if __name__ == '__main__':

    try:
        if os.listdir(location of your directory where the video is saved): # Eg : C:\\folder1\\folder2\\
            video_location = location of your directory where the video is saved with the file name # Eg C:\\folder1\\folder2\\filename.mp4
            readVideo(video_location)

    except Exception as e:
        print("Check Your Directory again")

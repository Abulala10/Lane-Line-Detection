"""
INTRODUCTION:
The traffic safety becomes more and more convincing with
the increasing urban traffic. Exiting the lane without
following proper rules is the root cause of most of the
accidents on the avenues. Most of these are result of the
interrupted and lethargic attitude of the driver. Lane
discipline is crucial to road safety for drivers and pedestrians
alike. The system has an objective to identify the lane
marks. It’s intent is to obtain a secure environment and
improved traffic surroundings. The functions of the
proposed system can range from displaying road line
positions to the driving person on any exterior display, to
more convoluted applications like detecting switching of the
lanes in the near future so that one can prevent concussions
caused on the highways.
Actuate detection of lane roads is a critical issue in lane
detection and departure warning systems. If an automobile
crosses a lane confinement then vehicles enabled with
predicting lane borders system directs the vehicles to
prevent collisions and generates an alarming condition.
These kind of intelligent system always makes the safe
travel but it is not always necessary that lane boundaries are
clearly noticeable, as poor road conditions,

Region Of Interest
A region of interest (ROI) is that area of an image that one
want to percolate or allow some other operations on them.
One can use the high-level ROI functions in order to create
ROIs of many shapes, for example drawpolygon or
drawcircle in the library of openCV. The main objective of
ROI is to decrease the portion of an image for speedy
calculation and also the size of image can be decremented
by ROI generation. One can describe several ROI in an
image. Generally, ROIs are defined as collections of several
contiguous pixels but you can also describe them as ROIs by
depth values, where it is not necessarily that the regions
must be contiguous. Most general use of an ROI is to
generate a binary mask image which is defined as the
combination of 0 & 1 in the image file matrix. Pixels that
belong to the ROI are set to 1 that is white and pixels
outside the ROI are set to 0 that is Black In the mask image.
There are two images shown below which indicates how
one’s image may look like after we focus only on the region
of interest. The original image is as shown below in the Fig
4.3 and in Fig 4.4 the Region of Interest is shown


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
        if os.listdir("C:\\abulala\\MIT\\TRIMESTER 1\\ARTIFICIAL INTELLIGENCE\\test_videos\\"):
            video_location = "C:\\abulala\\MIT\\TRIMESTER 1\\ARTIFICIAL INTELLIGENCE\\test_videos\\solidYellowLeft.mp4"
            readVideo(video_location)

    except Exception as e:
        print("Check Your Directory again")

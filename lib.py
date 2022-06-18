import os
import cv2 as cv
import numpy as np

def filter_edge(filename: str, opening: int, minEdgeThresh: float, maxEdgeThresh: float, theta: float = np.pi/180, houghThresh: int = 130):
    if not os.path.isdir("dist_"+filename): 
        os.mkdir("dist_"+filename)

    morph_kernel = cv.getStructuringElement(cv.MORPH_RECT, (5,5));

    img = cv.imread(filename, cv.IMREAD_GRAYSCALE)
    img_opening = img.copy()

    for i in range(0, opening):
        img_opening = cv.dilate(img_opening, morph_kernel)
    
    img_opening_edges = cv.Canny(img_opening, minEdgeThresh, maxEdgeThresh)
    img_opening_edges_lines = cv.HoughLinesP(img_opening_edges, 1, theta, houghThresh)

    cv.imwrite("dist_"+filename+"/img.jpg", img)
    cv.imwrite("dist_"+filename+"/opening_{}.jpg".format(opening), img_opening)
    cv.imwrite("dist_"+filename+"/edges_{}_{}_opening_{}.jpg".format(opening, minEdgeThresh, maxEdgeThresh), img_opening_edges)

    black_img = get_black_img(img)
    if(img_opening_edges_lines is None): 
        return
        
    for line in img_opening_edges_lines:
        x1, y1, x2, y2 = line[0]
        cv.line(black_img, (x1,y1), (x2, y2), 255)
    cv.imwrite("dist_"+filename+"/lines_img_opening_{}_edges_{}_{}.jpg".format(opening, minEdgeThresh, maxEdgeThresh, theta, houghThresh), black_img)

    return

def get_black_img(img: cv.Mat):
    height, width = img.shape
    black_img = np.zeros((height, width))
    return black_img

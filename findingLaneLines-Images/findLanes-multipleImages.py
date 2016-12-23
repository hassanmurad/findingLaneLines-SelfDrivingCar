import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2, os


# Start from the correct directory all the time
os.chdir("/Users/Murad/Desktop/git/CarND-LaneLines-P1/test_images/")
allFiles = os.listdir("/Users/Murad/Desktop/git/CarND-LaneLines-P1/test_images/")

print(allFiles)
for file in allFiles:
    
    print("Working on: %s" % file)

    # Read in and grayscale the image
    image = mpimg.imread(file)
    gray = grayscale(image)

    # Define a kernel size and apply Gaussian smoothing
    kernel_size = 5
    blur_gray = gaussian_blur(gray, kernel_size)

    # Define our parameters for Canny and apply
    low_threshold = 50
    high_threshold = 150
    edges = canny(blur_gray, low_threshold, high_threshold)

    imshape = image.shape
    vertices = np.array([[(0, imshape[0]), (450, 290), (490,290), (imshape[1], imshape[0])]], dtype=np.int32)
    masked_edges = region_of_interest(edges, vertices)


    # Define the Hough transform parameters
    # Make a blank the same size as our image to draw on
    rho = 1
    theta = (np.pi/180)
    threshold = 1
    min_line_length = 1
    max_line_gap = 1
    line_image = np.copy(image)*0 #creating a blank to draw lines o
    lines = hough_lines(masked_edges, rho, theta, threshold, min_line_length, max_line_gap)

    # Create a "color" binary image to combine with line image
    color_edges = np.dstack((edges, edges, edges)) 

    # Draw the lines on the edge image
    lines_edges = weighted_img(lines, image, α=0.9, β=1., λ=0.)

    
    #Save in file directory
    newfile = 'result_' + file
    cv2.imwrite(newfile, lines_edges)


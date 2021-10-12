 # -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 15:33:23 2021

@author: S2124194
"""

#Color Changing CODE

import cv2
import numpy
import os.path

#library of colors
color_list = [[0,0,255], [255,0,0], [0,250,0],[255,255,255],[120,120,120],[0,0,0],[255,250,0],[40,40,180],[170,0,84],[100,100,0],[0,240,250],[120,25,125],[10,60,195],[120,0,0],[10,140,255],[193,182,255], [180,105,255], [221,211,155], [210,240,188], [170,255,155], [135,45,150], [255,60,210],]
#color_list[0] = bright red
#color_list1 = bright blue
#color_list2 = bright green
#color_list3 = white
#color_list4 = grey
#color_list5 = black
#color_list6 = cyan
#color_list7 = maroonish red
#color_list8 = purpley blue
#color_list9 = teal
#color_list10 = yellow
#color_list11 = plum purple
#color_list12 = orangey red
#color_list13 = dark blue
#color_list14 = light orange
#color_list15 = baby pink
#color_list16 = hot pink
#color_list17 = baby blue
#color_list18 = neon pastel blue
#color_list19 = baby pastel green
#color_list20 = magenta
#color_list21 = lavender
#custom color = [B,G,R]


def trackPosition(slider_name, window_name, min_val):
    current_pos = cv2.getTrackbarPos(slider_name, window_name)
    if current_pos < min_val:
        print("Hey. That's too low")
        cv2.setTrackbarPos(slider_name, window_name, min_val)
        return min_val
    else:
        return current_pos

print ("Save your original image in the same folder as this program.")
filename_valid = False
while filename_valid == False:
    filename = input("Enter the name of your file, including the "\
                                 "extension, and then press 'enter': ")
    if os.path.isfile(filename) == True:
        filename_valid = True
    else:
        print ("Something was wrong with that filename. Please try again.")

#Brings in colored image, makes it 2d greyscale, then 3d greyscale
original_image = cv2.imread(filename,1)
grayscale_image_simple = cv2.imread(filename, 0)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)

#Creates display windows
cv2.namedWindow('Original Image')
cv2.namedWindow('Grayscale Image')
cv2.namedWindow('Customized Image')
cv2.namedWindow('Sliders2')

cv2.resizeWindow ('Sliders2', 960, 540)

image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]

#making papers the right size
color1_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color2_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
color3_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
color4_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
color5_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
color6_paper = numpy.zeros((image_height,image_width,image_channels),
                            numpy.uint8)

#assigns paper the specific color, please input your color selections
color1_paper[0:image_height,0:image_width, 0:image_channels] = [color_list[10]]
color2_paper[0:image_height,0:image_width, 0:image_channels] = [color_list[8]]
color3_paper[0:image_height,0:image_width, 0:image_channels] = [color_list[9]]
color4_paper[0:image_height,0:image_width, 0:image_channels] = [color_list[5]]
color5_paper[0:image_height,0:image_width, 0:image_channels] = [color_list[13]]
color6_paper[0:image_height,0:image_width, 0:image_channels] = [color_list[17]]

#sets the point which we divide "light" from "dark" in the greyscale image
#creates sliders to change greyscale break values
cv2.createTrackbar('Greyscale', 'Sliders2', 30, 150, lambda x:None)
cv2.createTrackbar('Greyscale2', 'Sliders2', 60, 175, lambda x:None)
cv2.createTrackbar('Greyscale3', 'Sliders2', 90, 190, lambda x:None)
cv2.createTrackbar('Greyscale4', 'Sliders2', 120, 205, lambda x:None)
cv2.createTrackbar('Greyscale5', 'Sliders2', 165, 235, lambda x:None)

#repeats search to update image with slider
keypressed = 1
while (keypressed != 27 and keypressed != ord('s')):
    grayscale_break = trackPosition('Greyscale', 'Sliders2', 5)
    grayscale_break2 = trackPosition('Greyscale2', 'Sliders2', 20)
    grayscale_break3 = trackPosition('Greyscale3', 'Sliders2', 40)
    grayscale_break4 = trackPosition('Greyscale4', 'Sliders2', 90)
    grayscale_break5 = trackPosition('Greyscale5', 'Sliders2', 130)

    
    #applies the greyscale to the specific color
    min_grayscale_for_color1 = [0,0,0]
    max_grayscale_for_color1 = [grayscale_break,grayscale_break,grayscale_break]
    min_grayscale_for_color2 = [grayscale_break+1,grayscale_break+1,grayscale_break+1]
    max_grayscale_for_color2 = [grayscale_break2,grayscale_break2,grayscale_break2]
    min_grayscale_for_color3 = [grayscale_break2+1,grayscale_break2+1, 
                                grayscale_break2+1]
    max_grayscale_for_color3 = [grayscale_break3,grayscale_break3,grayscale_break3]
    min_grayscale_for_color4 = [grayscale_break3+1,grayscale_break3+1, 
                                grayscale_break3+1]
    max_grayscale_for_color4 = [grayscale_break4,grayscale_break4,grayscale_break4]
    min_grayscale_for_color5 = [grayscale_break4+1,grayscale_break4+1, 
                                grayscale_break4+1]
    max_grayscale_for_color5 = [grayscale_break5,grayscale_break5,grayscale_break5]
    min_grayscale_for_color6 = [grayscale_break5+1,grayscale_break5+1, 
                                grayscale_break5+1]
    max_grayscale_for_color6 = [255,255,255]
    
    min_grayscale_for_color1 = numpy.array(min_grayscale_for_color1, dtype = "uint8")
    max_grayscale_for_color1 = numpy.array(max_grayscale_for_color1, dtype = "uint8")
    min_grayscale_for_color2 = numpy.array(min_grayscale_for_color2,
                                           dtype = "uint8")
    max_grayscale_for_color2 = numpy.array(max_grayscale_for_color2,
                                           dtype = "uint8")
    min_grayscale_for_color3 = numpy.array(min_grayscale_for_color3,
                                           dtype = "uint8")
    max_grayscale_for_color3 = numpy.array(max_grayscale_for_color3,
                                           dtype = "uint8")
    
    min_grayscale_for_color4 = numpy.array(min_grayscale_for_color4, dtype = "uint8")
    max_grayscale_for_color4 = numpy.array(max_grayscale_for_color4, dtype = "uint8")
    min_grayscale_for_color5 = numpy.array(min_grayscale_for_color5,
                                           dtype = "uint8")
    max_grayscale_for_color5 = numpy.array(max_grayscale_for_color5,
                                           dtype = "uint8")
    min_grayscale_for_color6 = numpy.array(min_grayscale_for_color6, dtype = "uint8")
    max_grayscale_for_color6 = numpy.array(max_grayscale_for_color6, dtype = "uint8")
  
    
    
    #tells the program to chop out anything that doesn't fit in the color range
    block_all_but_the_color1_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_color1,
                                              max_grayscale_for_color1)
    block_all_but_the_color2_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_color2,
                                                 max_grayscale_for_color2)
    block_all_but_the_color3_parts = cv2.inRange(grayscale_image,
                                                 min_grayscale_for_color3,
                                                 max_grayscale_for_color3)
    block_all_but_the_color4_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_color4,
                                              max_grayscale_for_color4)
    block_all_but_the_color5_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_color5,
                                              max_grayscale_for_color5)
    block_all_but_the_color6_parts = cv2.inRange(grayscale_image,
                                              min_grayscale_for_color6,
                                              max_grayscale_for_color6)
    
    #assigns the correct color to chosen color variable name
    color1_parts_of_image = cv2.bitwise_or(color1_paper, color1_paper,
                                        mask = block_all_but_the_color1_parts)
    color2_parts_of_image = cv2.bitwise_or(color2_paper, color2_paper,
                                           mask = block_all_but_the_color2_parts)
    color3_parts_of_image = cv2.bitwise_or(color3_paper, color3_paper,
                                           mask = block_all_but_the_color3_parts)
    color4_parts_of_image = cv2.bitwise_or(color4_paper, color4_paper,
                                        mask = block_all_but_the_color4_parts)
    color5_parts_of_image = cv2.bitwise_or(color5_paper, color5_paper,
                                           mask = block_all_but_the_color5_parts)
    color6_parts_of_image = cv2.bitwise_or(color6_paper, color6_paper,
                                           mask = block_all_but_the_color6_parts)
    
    #creates custom image
    customized_image = cv2.bitwise_or(color1_parts_of_image, color2_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color3_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color4_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color5_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color6_parts_of_image)
    
    #displays the windows
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Grayscale Image',grayscale_image)
    cv2.imshow('Customized Image',customized_image)
    
    #escape function
    #press escape to cancel out the image
    keypressed = cv2.waitKey(1)
if keypressed == 27:
    cv2.destroyAllWindows()
    #press s to name and save the image
elif keypressed == ord('s'): 
    new_file = input('Name your file, be sure to include .jpg:')
   # cv2.imwrite('phot',grayscale_image)
    cv2.imwrite(new_file, customized_image)
    cv2.destroyAllWindows()

import cv2 as cv
import numpy as np
import logging
from time import sleep
class Vision:

    # properties
    needle_img = None
    needle_star_img  = None
    needle_w = 0
    needle_h = 0
    needle_star_w = 0
    needle_star_h = 0  
    method = None

    #logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',filename='foe_vision.log', encoding='utf-8', level=logging.INFO)

    # constructor
    def __init__(self, needle_img_path,needle_star_img_path='', method=cv.TM_CCOEFF_NORMED):
        # load the image we're trying to match
        # https://docs.opencv.org/4.2.0/d4/da8/group__imgcodecs.html
        self.needle_img = cv.imread(needle_img_path, cv.IMREAD_UNCHANGED)
         # Save the dimensions of the needle image
        self.needle_w = self.needle_img.shape[1]
        self.needle_h = self.needle_img.shape[0]

  
        if(needle_star_img_path):
            self.needle_star_img = cv.imread(needle_star_img_path, cv.IMREAD_UNCHANGED)
            #Save the dimensions of the needle image
            self.needle_star_w = self.needle_star_img.shape[1]
            self.needle_star_h = self.needle_star_img.shape[0]

         # There are 6 methods to choose from:
        # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
        self.method = method

    def findMultiple(self, haystack_img, threshold=0.5, debug_mode=None, imgNumber=0,needle='None'):
       
        #cv.imwrite('results\multiple_' + needle + '.png', self.needle_img) 
        # run the OpenCV algorithm
        
        # Image matching works only on gray images
        # (color conversion from RGB/BGR to GRAY scale)
        '''result = cv.minMaxLoc(
            cv.matchTemplate(
                cv.cvtColor(
                    haystack_img,
                    cv.COLOR_RGB2GRAY
                ),
                cv.cvtColor(
                    self.needle_img,
                    cv.COLOR_BGR2GRAY
                ),
                self.method
            )
        )'''
        result =   cv.matchTemplate(
                cv.cvtColor(
                    haystack_img,
                    cv.COLOR_RGB2BGR
                ),
                cv.cvtColor(
                    self.needle_img,
                    cv.COLOR_RGB2BGR
                ),
                self.method
            )
        #result = cv.matchTemplate(haystack_img, self.needle_img, self.method)
        
        #result = cv.matchTemplate(haystack_img, self.needle_img, self.method)
        # Get the all the positions from the match result that exceed our threshold
        #logging.info('threshold:', threshold)
        #logging.info('result:', result)
        #locations = np.where(result >= 0.7)
        #logging.info('locations1:', locations)
        locations = np.where(result >= threshold)
        #logging.info('locations2:', locations)
        locations = list(zip(*locations[::-1]))
        #if(locations):
        #    cv.imwrite('result_'+ needle + str(imgNumber) +'.png', result) 
        #logging.info(locations)
        # You'll notice a lot of overlapping rectangles get drawn. We can eliminate those redundant
        # locations by using groupRectangles().
        # First we need to create the list of [x, y, w, h] rectangles
        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), self.needle_w, self.needle_h]
            # Add every box to the list twice in order to retain single (non-overlapping) boxes
            rectangles.append(rect)
            rectangles.append(rect)
        # Apply group rectangles.
        # The groupThreshold parameter should usually be 1. If you put it at 0 then no grouping is
        # done. If you put it at 2 then an object needs at least 3 overlapping rectangles to appear
        # in the result. I've set eps to 0.5, which is:
        # "Relative difference between sides of the rectangles to merge them into a group."
        rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)
        logging.info("rectangles: %s", rectangles)
        points = []
        if len(rectangles):
            logging.info('Found needle.')
            line_color = (0, 255, 0)
            line_type = cv.LINE_4
            marker_color = (255, 0, 255)
            click_color = (0, 0, 0)
            marker_type = cv.MARKER_CROSS
            # Loop over all the rectangles
            for (x, y, w, h) in rectangles:
                # Determine the center position
                center_x = x + int(w/2)
                center_y = y + int(h/2)
                # Save the points
                points.append((center_x, center_y))

                logging.info('debug_mode: %s', debug_mode)
                if debug_mode == 'rectangles':
                    # Determine the box position
                    top_left = (x, y)
                    bottom_right = (x + w, y + h)

                    # font
                    font = cv.FONT_HERSHEY_SIMPLEX
                    
                    # fontScale
                    fontScale = 1
                    
                    # Blue color in BGR
                    color = (255, 0, 0)
                    
                    # Line thickness of 2 px
                    thickness = 2
                    
                    # Using cv2.putText() method
                    cv.putText(haystack_img,  str(center_x - int(w/2)) +','+ str(center_y + int(h/2) + h), (center_x - int(w/2), center_y + int(h/2) + h), font, fontScale, color, thickness, cv.LINE_AA)
                   # Draw the box
                    cv.rectangle(haystack_img, top_left, bottom_right, color=line_color, lineType=line_type, thickness=2)
                    cv.drawMarker(haystack_img, (center_x, center_y), color=marker_color, markerType=marker_type, markerSize=40, thickness=2)
                    cv.drawMarker(haystack_img, (center_x - int(w/2), center_y + int(h/2) + h), color=click_color, markerType=marker_type, markerSize=20, thickness=2)

                elif debug_mode == 'points':
                    # Draw the center point
                    cv.drawMarker(haystack_img, (center_x, center_y), 
                                color=marker_color, markerType=marker_type, 
                                markerSize=40, thickness=2)
            sleep(5)
            cv.imwrite('result_click_' + needle + '.png', haystack_img)
            if debug_mode:
                logging.info('Debug Found needle.')
                #cv.waitKey()
                #cv.imwrite('Game'+ str(imgNumber) +'.png', haystack_img) 
                #cv.imwrite('results\result_click_point'+ str(imgNumber) +'.png', haystack_img)
                #cv.imshow('Matches', haystack_img)
        sleep(5)
        #cv.imwrite('result_click_' + needle +  str(imgNumber) +'.png', haystack_img)
        return points

    def findSingle(self, haystack_img, threshold=0.5, debug_mode=None, imgNumber=0,needle='None'):
       
        points = []
        cv.imwrite('results\_single_self.needle_img.png', self.needle_img) 
        # run the OpenCV algorithm
        
        # Image matching works only on gray images
        # (color conversion from RGB/BGR to GRAY scale)
        result = cv.matchTemplate(
                cv.cvtColor(
                    haystack_img,
                    cv.COLOR_RGB2BGR
                ),
                cv.cvtColor(
                    self.needle_img,
                    cv.COLOR_RGB2BGR
                ),
                self.method
            )
       
        
        # Get the best match position from the match result.
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        if max_val >= threshold:
            logging.info('Found needle.')
        else:
            return points
        #result = cv.matchTemplate(haystack_img, self.needle_img, self.method)
        
        #result = cv.matchTemplate(haystack_img, self.needle_img, self.method)
        # Get the all the positions from the match result that exceed our threshold
        #logging.info('threshold:', threshold)
        #logging.info('result:', result)
        #locations = np.where(result >= 0.7)
        #logging.info('locations1:', locations)
        #locations = np.where(result >= threshold)
        #logging.info('locations2:', locations)
        #locations = list(zip(*locations[::-1]))
        #if(locations):
        #    cv.imwrite('result_'+ needle + str(imgNumber) +'.png', result) 
        #logging.info(locations)
        # You'll notice a lot of overlapping rectangles get drawn. We can eliminate those redundant
        # locations by using groupRectangles().
        # First we need to create the list of [x, y, w, h] rectangles
        rectangles = []
        #for loc in locations:
        logging.info('result: %s, %s, %s, %s ',min_val, max_val, min_loc, max_loc)
        rect = [int(max_loc[0]), int(max_loc[1]), self.needle_w, self.needle_h]
        
        logging.info('rect: %s',rect)
        # Add every box to the list twice in order to retain single (non-overlapping) boxes
        rectangles.append(rect)
        rectangles.append(rect)
        # Apply group rectangles.
        # The groupThreshold parameter should usually be 1. If you put it at 0 then no grouping is
        # done. If you put it at 2 then an object needs at least 3 overlapping rectangles to appear
        # in the result. I've set eps to 0.5, which is:
        # "Relative difference between sides of the rectangles to merge them into a group."
        rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)
        #logging.info(rectangles)
        
        if len(rectangles):
            #logging.info('Found needle.')
            line_color = (0, 255, 0)
            line_type = cv.LINE_4
            marker_color = (255, 0, 255)
            marker_type = cv.MARKER_CROSS
            # Loop over all the rectangles
            for (x, y, w, h) in rectangles:
                # Determine the center position
                center_x = x + int(w/2)
                center_y = y + int(h/2)
                # Save the points
                points.append((center_x, center_y))
                if debug_mode == 'rectangles':
                    logging.info('Found needle. %s',(center_x, center_y))
                    # Determine the box position
                    top_left = (x, y)
                    bottom_right = (x + w, y + h)
                    # Draw the box
                    cv.rectangle(haystack_img, top_left, bottom_right, color=line_color, lineType=line_type, thickness=2)
                #elif debug_mode == 'points':
                    # Draw the center point
                    cv.drawMarker(haystack_img, (center_x, center_y), 
                                color=marker_color, markerType=marker_type, 
                                markerSize=40, thickness=2)
            if debug_mode:
                logging.info('Found needle.')
                #cv.waitKey()
                #cv.imwrite('Game'+ str(imgNumber) +'.png', haystack_img) 
                cv.imwrite('results\result_click_point.jpg', haystack_img)
                #cv.imshow('Matches', haystack_img)
        return points
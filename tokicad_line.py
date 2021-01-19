import sys
import math
import cv2 as cv
import numpy as np
def main(argv):
    
    default_file = '1teszt.png'
    filename = argv[0] if len(argv) > 0 else default_file
    # Fajl betoltes
    src = cv.imread(cv.samples.findFile(filename))
    src=cv.cvtColor(src.astype(np.uint8), cv.COLOR_BGR2GRAY)
    # fajl ellenorzese
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_lines.py [image_name -- default ' + default_file + '] \n')
        return -1
    
    
    dst = cv.Canny(src, 50, 200, None, 7)
    #dst = cv.blur(dst, (2, 2))
    # Masolja az eleket azokra a képekre, amelyek az eredmenyeket BGR-ben jelenitik meg

    cdstP = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
       
    linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 4, 4)
    
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)
    
    cv.imshow("Source", src)
    cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdstP)
    
    cv.waitKey()
    return 0
    
if __name__ == "__main__":
    main(sys.argv[1:])
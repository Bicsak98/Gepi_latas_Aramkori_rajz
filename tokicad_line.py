import sys
import math
import cv2 as cv
import numpy as np

def main(argv):
    
    default_file = 'test.jpg'
    filename = argv[0] if len(argv) > 0 else default_file
    # Kép betöltése
    s=cv.imread(default_file)
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_GRAYSCALE)
    # Ellenőrizze, hogy a kép jól van-e betöltve
    if src is None:
        print ('Error opening image!')
        print ('Usage: tokicad.py [image_name -- default ' + default_file + '] \n')
        return -1
    
    
    dst = cv.Canny(src, 50, 200, None, 3)
    
    # Másolja az éleket azokra a képekre, amelyek az eredményeket BGR-ben jelenítik meg
    cdstP = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
    
    linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 5, None, 40, 10)
    
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)
    
    cv.imshow("Eredeti rajz", s)
    cv.imshow("Felismert vonalak", cdstP)
    
    cv.waitKey()
    return 0
    
if __name__ == "__main__":
    main(sys.argv[1:])
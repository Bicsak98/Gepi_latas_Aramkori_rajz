import cv2
import numpy as np


I = cv2.imread("211teszt.png")
Ellenallas = cv2.imread("test3.png").astype(int)
Kondenzator = cv2.imread("kondenzator4.png").astype(int)
Kapcsolo = cv2.imread("kapcsolo.png").astype(int)
Lampa = cv2.imread("x.png").astype(int)
Amper = cv2.imread("Amper.png").astype(int)
Volt = cv2.imread("Volt.png").astype(int)

I_sz=cv2.cvtColor(I.astype(np.uint8), cv2.COLOR_BGR2GRAY)
T_sz=cv2.cvtColor(Ellenallas.astype(np.uint8), cv2.COLOR_BGR2GRAY)
T1_sz=cv2.cvtColor(Kondenzator.astype(np.uint8), cv2.COLOR_BGR2GRAY)
T2_sz=cv2.cvtColor(Kapcsolo.astype(np.uint8), cv2.COLOR_BGR2GRAY)
T3_sz=cv2.cvtColor(Lampa.astype(np.uint8), cv2.COLOR_BGR2GRAY)
T4_sz=cv2.cvtColor(Amper.astype(np.uint8), cv2.COLOR_BGR2GRAY)
T5_sz=cv2.cvtColor(Volt.astype(np.uint8), cv2.COLOR_BGR2GRAY)

M1 = cv2.matchTemplate(I_sz, T_sz.astype(np.uint8), cv2.TM_CCOEFF)
M2 = cv2.matchTemplate(I_sz, T1_sz.astype(np.uint8), cv2.TM_CCOEFF_NORMED)
M3 = cv2.matchTemplate(I_sz, T2_sz.astype(np.uint8), cv2.TM_CCORR_NORMED)
M4 = cv2.matchTemplate(I_sz, T3_sz.astype(np.uint8), cv2.TM_CCOEFF_NORMED)
M5 = cv2.matchTemplate(I_sz, T4_sz.astype(np.uint8), cv2.TM_CCOEFF_NORMED)
M6 = cv2.matchTemplate(I_sz, T5_sz.astype(np.uint8), cv2.TM_CCOEFF_NORMED)


(_, maxVal, _, maxloc) = cv2.minMaxLoc(M1)
(_, maxVal2, _, maxloc2) = cv2.minMaxLoc(M2)
(_, maxVal3, _, maxloc3) = cv2.minMaxLoc(M3)
(_, maxVal4, _, maxloc4) = cv2.minMaxLoc(M4)
(_, maxVal5, _, maxloc5) = cv2.minMaxLoc(M5)
(_, maxVal6, _, maxloc6) = cv2.minMaxLoc(M6)

threshold = 0.9047

if(np.amax(M1) >= threshold):
    cv2.circle(I, (maxloc[0] + Ellenallas.shape[1] // 2, maxloc[1] + Ellenallas.shape[0] // 2), 20, (255, 0, 0), 3)
if(np.amax(M2) >= threshold):
    cv2.circle(I, (maxloc2[0] + Kondenzator.shape[1] // 2, maxloc2[1] + Kondenzator.shape[0] // 2), 20, (0, 0, 255), 3)
if(np.amax(M3) >= threshold):
    cv2.circle(I, (maxloc3[0] + Kapcsolo.shape[1] // 2, maxloc3[1] + Kapcsolo.shape[0] // 2), 20, (0, 255, 0), 3)
if(np.amax(M4) >= threshold):
    cv2.circle(I, (maxloc4[0] + Lampa.shape[1] // 2, maxloc4[1] + Lampa.shape[0] // 2), 20, (0, 255, 255), 3)
if(np.amax(M5) >= threshold):
    cv2.circle(I, (maxloc5[0] + Amper.shape[1] // 2, maxloc5[1] + Amper.shape[0] // 2), 20, (0, 200, 255), 3)
if(np.amax(M6) >= threshold):
    cv2.circle(I, (maxloc6[0] + Volt.shape[1] // 2, maxloc6[1] + Volt.shape[0] // 2), 20, (100, 255, 255), 3)





M1 = ((M1- M1.min()) / (M1.max() - M1.min()) * 255).astype(np.uint8)
M2 = ((M2- M2.min()) / (M2.max() - M2.min()) * 255).astype(np.uint8)
M3 = ((M3- M3.min()) / (M3.max() - M3.min()) * 255).astype(np.uint8)
M4 = ((M4- M4.min()) / (M4.max() - M4.min()) * 255).astype(np.uint8)
M5 = ((M5- M5.min()) / (M5.max() - M5.min()) * 255).astype(np.uint8)
M6 = ((M6- M6.min()) / (M6.max() - M6.min()) * 255).astype(np.uint8)



#cv2.imshow("Keresett objektum",T.astype(np.uint8))
#cv2.imshow("Keresett objektum",T1.astype(np.uint8))
cv2.imshow("Keresett kepen az objektum helye", I)
cv2.waitKey(0)
cv2.destroyAllWindows()
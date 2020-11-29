import cv2
import numpy as np


I = cv2.imread("test.jpg")
T = cv2.imread("test1.jpg").astype(int)

W = I.shape[1]
H = I.shape[0]

Wt = T.shape[1]
Ht = T.shape[0]

M0 = np.zeros((H, W))

for i in range(W - Wt):
    for j in range(H - Ht):
        I_roi = I[j:j+Ht, i:i+Wt].astype(int)
        d = np.sum(np.abs(I_roi - T))
        M0[j, i] = d

(_, _, minloc, _) = cv2.minMaxLoc(M0[:H - Ht, :W - Wt])

M0 = ((M0 - M0.min()) / (M0.max() - M0.min()) * 255).astype(np.uint8)

M1 = cv2.matchTemplate(I, T.astype(np.uint8), cv2.TM_CCOEFF)

(_, _, _, maxloc) = cv2.minMaxLoc(M1)

cv2.circle(I, (minloc[0] + T.shape[1] // 2, minloc[1] + T.shape[0] // 2), 30, (0, 0, 255), 3)
cv2.circle(I, (maxloc[0] + T.shape[1] // 2, maxloc[1] + T.shape[0] // 2), 20, (0, 255, 0), 3)

M1 = ((M1- M1.min()) / (M1.max() - M1.min()) * 255).astype(np.uint8)

cv2.imshow("Keresett objektum",T.astype(np.uint8))
cv2.imshow("Keresett képen az objektum helye", I)
cv2.waitKey(0)
cv2.destroyAllWindows()
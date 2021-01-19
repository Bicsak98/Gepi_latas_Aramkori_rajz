import sys
import math
import cv2 
import numpy as np


# Fájl beolvasása   
I = cv2.imread("1teszt.png")

# Objektum felismerés
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
# SCH fájl elejének megírása
h="~"
i='"'

f = open("rajz3.sch", "w")
f.write("EESchema Schematic File Version 4\n")
f.write("EELAYER 30 0\n")
f.write("EELAYER END\n")
f.write("$Descr A4 11693 8268\n")
f.write("encoding utf-8\n")
f.write("Sheet 1 1\n")
f.write("Title "+i+i+"\n")
f.write("Date "+i+i+"\n")
f.write("Rev "+i+i+"\n")
f.write("Comp "+i+i+"\n")
f.write("Comment1 "+i+i+"\n")
f.write("Comment2 "+i+i+"\n")
f.write("Comment3 "+i+i+"\n")
f.write("Comment4 "+i+i+"\n")
f.write("$EndDescr\n")


threshold = 0.9047

if(np.amax(M1) >= threshold):
    #cv2.circle(I, (maxloc[0] + Ellenallas.shape[1] // 2, maxloc[1] + Ellenallas.shape[0] // 2), 20, (255, 0, 0), 3)
    Rc="R1"
    Rn="R_PHOTO"
    x=int((maxloc[0] + Ellenallas.shape[1] // 2)*10.4166667)
    y=int((maxloc[1] + Ellenallas.shape[0] // 2)*10.4166667)

    f.write("$Comp\n")
    f.write("L Device:R_PHOTO R1\n")
    f.write("U 1 1 6003C928\n")
    f.write("P "+str(x)+" "+str(y)+"\n")
    f.write("F 0 "+str(i+Rc+i)+" V "+str(x+len(Rc))+" "+str(y+len(Rc))+" 50  0000 C CNN\n")
    f.write("F 1 "+i+Rn+i+" V "+str(x+len(Rn))+" "+str(y+len(Rn))+" 50  0000 C CNN\n")
    f.write("F 2 "+i+i+" V "+str(x)+" "+str(y+60)+" 50  0001 L CNN\n")
    f.write("F 3 "+i+h+i+" H "+str(x)+" "+str(y+60)+" 50  0001 C CNN\n")
    f.write("	1    "+str(x)+" "+str(y)+"\n")
    f.write("	1    -1    -1    0\n")
    f.write("$EndComp\n")

if(np.amax(M2) >= threshold):
    #cv2.circle(I, (maxloc2[0] + Kondenzator.shape[1] // 2, maxloc2[1] + Kondenzator.shape[0] // 2), 20, (0, 0, 255), 3)
    Batterc="BT1"
    Bn="Battery_Cell"
    x=int((maxloc2[0] + Kondenzator.shape[1] // 2)*10.4166667)
    y=int((maxloc2[1] + Kondenzator.shape[0] // 2)*10.4166667)

    f.write("$Comp\n")
    f.write("L Device:Battery_Cell BT1\n")
    f.write("U 1 1 600230B0\n")
    f.write("P "+str(x)+" "+str(y)+"\n")
    f.write("F 0 "+i+Batterc+i+" H "+str(x+len(Batterc))+" "+str(y+len(Batterc))+" 50  0000 L CNN\n")
    f.write("F 1 "+i+Bn+i+" H "+str(x+len(Bn))+" "+str(y+len(Bn))+" 50  0000 L CNN\n")
    f.write("F 2 "+i+i+" V "+str(x)+" "+str(y+60)+" 50  0001 C CNN\n")
    f.write("F 3 "+i+h+i+" V "+str(x)+" "+str(y+60)+" 50  0001 C CNN\n")
    f.write("	1    "+str(x)+" "+str(y)+"\n")
    f.write("	1    -1   -1   0\n")
    f.write("$EndComp\n")

if(np.amax(M3) >= threshold):
    #cv2.circle(I, (maxloc3[0] + Kapcsolo.shape[1] // 2, maxloc3[1] + Kapcsolo.shape[0] // 2), 20, (0, 255, 0), 3)
    Circc="CB1"
    Cn="CircuitBreaker_1P"
    x=int((maxloc3[0] + Kapcsolo.shape[1] // 2)*10.4166667)
    y=int((maxloc3[1] + Kapcsolo.shape[0] // 2)*10.4166667)

    f.write("$Comp\n")
    f.write("L Device:CircuitBreaker_1P CB1\n")
    f.write("U 1 1 6001C3B0\n")
    f.write("P "+str(x)+" "+str(y)+"\n")
    f.write("F 0 "+i+Circc+i+" H "+str(x+len(Circc))+" "+str(y+len(Circc))+" 50  0000 L CNN\n")
    f.write("F 1 "+i+Cn+i+" H "+str(x+len(Cn))+" "+str(y+len(Cn))+" 50  0000 L CNN\n")
    f.write("F 2 "+i+i+" H "+str(x)+" "+str(y+60)+" 50  0001 C CNN\n")
    f.write("F 3 "+i+h+i+" H "+str(x)+" "+str(y+60)+" 50  0001 C CNN\n")
    f.write("	1    "+str(x)+" "+str(y)+"\n")
    f.write("	1    1    1    0\n")
    f.write("$EndComp\n")

if(np.amax(M4) >= threshold):
    #cv2.circle(I, (maxloc4[0] + Lampa.shape[1] // 2, maxloc4[1] + Lampa.shape[0] // 2), 20, (0, 255, 255), 3)
    Lampc="LA?"
    Ln="Lamp"
    x=int((maxloc4[0] + Lampa.shape[1] // 2)*10.4166667)
    y=int((maxloc4[1] + Lampa.shape[0] // 2)*10.4166667)


    f.write("$Comp\n")
    f.write("L Device:Lamp LA?\n")
    f.write("U 1 1 600446D0\n")
    f.write("P "+str(x)+" "+str(y)+"\n")
    f.write("F 0 "+i+Lampc+i+" H "+str(x+len(Lampc))+" "+str(y+len(Lampc))+" 50  0000 L CNN\n")
    f.write("F 1 "+i+Ln+i+" H "+str(x+len(Ln))+" "+str(y+len(Ln))+" 50  0000 L CNN\n")
    f.write("F 2 "+i+i+" H "+str(x)+" "+str(y+60)+" 50  0001 C CNN\n")
    f.write("F 3 "+i+h+i+" H "+str(x)+" "+str(y+60)+" 50  0001 C CNN\n")
    f.write("	1    "+str(x)+" "+str(y)+"\n")
    f.write("	1    1    1    0\n")
    f.write("$EndComp\n")

if(np.amax(M5) >= threshold):
    #cv2.circle(I, (maxloc5[0] + Amper.shape[1] // 2, maxloc5[1] + Amper.shape[0] // 2), 20, (0, 200, 255), 3)
    Amperc="MES1"
    An="Amperemeter_DC"
    x=int((maxloc5[0] + Amper.shape[1] // 2)*10.4166667)
    y=int((maxloc5[1] + Amper.shape[0] // 2)*10.4166667)

    f.write("$Comp\n")
    f.write("L Device:Amperemeter_DC MES1\n")
    f.write("U 1 1 6001AF81\n")
    f.write("P "+str(x)+" "+str(y)+"\n")
    f.write("F 0 "+i+Amperc+i+" H "+str(x+len(Amperc))+" "+str(y+len(Amperc))+" 50  0000 L CNN\n")
    f.write("F 2 "+i+An+i+" V "+str(x+len(An))+" "+str(y+len(An))+" 50  0001 C CNN\n")
    f.write("F 2 "+i+i+" V "+str(x)+" "+str(y+60)+" 50  0001 C CNN\n")
    f.write("F 3 "+i+h+i+" V "+str(x)+" "+str(y+60)+" 50  0001 C CNN\n")
    f.write("	1    "+str(x)+" "+str(y)+"\n")
    f.write("	1    0    0    -1\n")
    f.write("$EndComp\n")

if(np.amax(M6) >= threshold):
    #cv2.circle(I, (maxloc6[0] + Volt.shape[1] // 2, maxloc6[1] + Volt.shape[0] // 2), 20, (100, 255, 255), 3)
    Voltc="MES2"
    Vn="Voltmeter_DC"
    x=int((maxloc6[0] + Volt.shape[1] // 2)*10.4166667)
    y=int((maxloc6[1] + Volt.shape[0] // 2)*10.4166667)

    f.write("$Comp\n")
    f.write("L Device:Voltmeter_DC MES2\n")
    f.write("U 1 1 600243AC\n")
    f.write("P "+str(x)+" "+str(y)+"\n")
    f.write("F 0 "+i+Voltc+i+" H "+str(x+len(Voltc))+" "+str(y+len(Voltc))+" 50  0000 L CNN\n")
    f.write("F 1 "+i+Vn+i+" H "+str(x+len(Vn))+" "+str(y+len(Vn))+" 50  0000 L CNN\n")
    f.write("F 2 "+i+i+" V "+str(x)+" "+str(y+60)+" 50  0001 C CNN\n")
    f.write("F 3 "+i+h+i+" V "+str(x)+" "+str(y+60)+" 50  0001 C CNN\n")
    f.write("	1    "+str(x)+" "+str(y)+"\n")
    f.write("	1    0    0    -1\n")
    f.write("$EndComp\n")

M1 = ((M1- M1.min()) / (M1.max() - M1.min()) * 255).astype(np.uint8)
M2 = ((M2- M2.min()) / (M2.max() - M2.min()) * 255).astype(np.uint8)
M3 = ((M3- M3.min()) / (M3.max() - M3.min()) * 255).astype(np.uint8)
M4 = ((M4- M4.min()) / (M4.max() - M4.min()) * 255).astype(np.uint8)
M5 = ((M5- M5.min()) / (M5.max() - M5.min()) * 255).astype(np.uint8)
M6 = ((M6- M6.min()) / (M6.max() - M6.min()) * 255).astype(np.uint8)

# Objektum felismerés vége

# Egyenesek felismerése és fájlba írás

dst = cv2.Canny(I_sz, 50, 200, None, 7)
linesP = cv2.HoughLinesP(dst, 1, np.pi / 180, 50, None, 4, 4)
    
if linesP is not None:
    for i in range(0, len(linesP)):
        l = linesP[i][0]
        f.write("Wire Wire Line\n")
        f.write("	"+str(int(l[0]*10.4166667))+" "+str(int(l[1]*10.4166667))+" "+str(int(l[2]*10.4166667))+" "+str(int(l[3]*10.4166667))+"\n")
        # cv2.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv2.LINE_AA)

# Egyenesek felismerése és fájlba írás vége
 
f.write("$EndSCHEMATC\n")
f.close()
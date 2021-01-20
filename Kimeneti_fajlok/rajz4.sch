EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Device:R_PHOTO R1
U 1 1 6003C928
P 1385 1333
F 0 "R1" V 1387 1335 50  0000 C CNN
F 1 "R_PHOTO" V 1392 1340 50  0000 C CNN
F 2 "" V 1385 1393 50  0001 L CNN
F 3 "~" H 1385 1393 50  0001 C CNN
	1    1385 1333
	1    -1    -1    0
$EndComp
$Comp
L Device:Battery_Cell BT1
U 1 1 600230B0
P 1197 302
F 0 "BT1" H 1200 305 50  0000 L CNN
F 1 "Battery_Cell" H 1209 314 50  0000 L CNN
F 2 "" V 1197 362 50  0001 C CNN
F 3 "~" V 1197 362 50  0001 C CNN
	1    1197 302
	1    -1   -1   0
$EndComp
$Comp
L Device:CircuitBreaker_1P CB1
U 1 1 6001C3B0
P 1895 250
F 0 "CB1" H 1898 253 50  0000 L CNN
F 1 "CircuitBreaker_1P" H 1912 267 50  0000 L CNN
F 2 "" H 1895 310 50  0001 C CNN
F 3 "~" H 1895 310 50  0001 C CNN
	1    1895 250
	1    1    1    0
$EndComp
$Comp
L Device:Amperemeter_DC MES1
U 1 1 6001AF81
P 291 906
F 0 "MES1" H 295 910 50  0000 L CNN
F 2 "Amperemeter_DC" V 305 920 50  0001 C CNN
F 2 "" V 291 966 50  0001 C CNN
F 3 "~" V 291 966 50  0001 C CNN
	1    291 906
	1    0    0    -1
$EndComp
$Comp
L Device:Voltmeter_DC MES2
U 1 1 600243AC
P 1343 1958
F 0 "MES2" H 1347 1962 50  0000 L CNN
F 1 "Voltmeter_DC" H 1355 1970 50  0000 L CNN
F 2 "" V 1343 2018 50  0001 C CNN
F 3 "~" V 1343 2018 50  0001 C CNN
	1    1343 1958
	1    0    0    -1
$EndComp
Wire Wire Line
	1281 281 1645 281
Wire Wire Line
	250 312 697 312
Wire Wire Line
	1593 1385 2135 1385
Wire Wire Line
	281 281 593 281
Wire Wire Line
	2260 1385 2260 270
Wire Wire Line
	2291 1364 2291 302
Wire Wire Line
	1281 302 1864 302
Wire Wire Line
	260 1364 1166 1364
Wire Wire Line
	270 1395 1000 1395
Wire Wire Line
	854 1979 1197 1979
Wire Wire Line
	1510 1937 1906 1937
Wire Wire Line
	1593 1354 2250 1354
Wire Wire Line
	281 322 281 666
Wire Wire Line
	1375 1958 1416 1958
Wire Wire Line
	1093 562 1093 10
Wire Wire Line
	1166 1270 1166 1479
Wire Wire Line
	1562 1968 1916 1968
Wire Wire Line
	781 1958 781 1406
Wire Wire Line
	260 791 260 947
Wire Wire Line
	260 1114 260 1375
Wire Wire Line
	2000 1906 2000 1395
Wire Wire Line
	812 1979 812 1437
$EndSCHEMATC

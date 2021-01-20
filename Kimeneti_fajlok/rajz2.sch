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
	1    1    1    0
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
	260 302 2281 302
Wire Wire Line
	343 281 2281 281
Wire Wire Line
	2260 1375 2260 270
Wire Wire Line
	2281 1375 2281 291
Wire Wire Line
	270 1395 270 1114
Wire Wire Line
	1604 1364 2291 1354
Wire Wire Line
	510 1385 1156 1385
Wire Wire Line
	291 1114 291 1395
Wire Wire Line
	1562 1947 2020 1947
Wire Wire Line
	1604 1385 2020 1395
Wire Wire Line
	791 1968 1104 1968
Wire Wire Line
	1114 552 1114 62
Wire Wire Line
	2000 1968 2000 1385
Wire Wire Line
	1562 1968 1927 1968
Wire Wire Line
	1093 552 1093 62
$EndSCHEMATC

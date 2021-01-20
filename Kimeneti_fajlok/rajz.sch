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
L Device:Amperemeter_DC MES1
U 1 1 6001AF81
P 3600 4100
F 0 "MES1" H 3753 4146 50  0000 L CNN
F 2 "" V 3600 4200 50  0001 C CNN
F 3 "~" V 3600 4200 50  0001 C CNN
	1    3600 4100
	1    0    0    -1
$EndComp
$Comp
L Device:Battery_Cell BT1
U 1 1 600230B0
P 4350 3400
F 0 "BT1" H 4468 3496 50  0000 L CNN
F 1 "Battery_Cell" H 4468 3405 50  0000 L CNN
F 2 "" V 4350 3460 50  0001 C CNN
F 3 "~" V 4350 3460 50  0001 C CNN
	1    4350 3400
	1    -1   -1   0
$EndComp
$Comp
L Device:Voltmeter_DC MES2
U 1 1 600243AC
P 4550 5050
F 0 "MES2" H 4703 5096 50  0000 L CNN
F 1 "Voltmeter_DC" H 4703 5005 50  0000 L CNN
F 2 "" V 4550 5150 50  0001 C CNN
F 3 "~" V 4550 5150 50  0001 C CNN
	1    4550 5050
	1    0    0    -1
$EndComp
$Comp
L Device:CircuitBreaker_1P CB1
U 1 1 6001C3B0
P 5150 3400
F 0 "CB1" H 5202 3446 50  0000 L CNN
F 1 "CircuitBreaker_1P" H 5202 3355 50  0000 L CNN
F 2 "" H 5150 3400 50  0001 C CNN
F 3 "~" H 5150 3400 50  0001 C CNN
	1    5150 3400
	1    1    1    0
$EndComp
$Comp
L Device:R_PHOTO R1
U 1 1 6003C928
P 4550 4500
F 0 "R1" V 4225 4500 50  0000 C CNN
F 1 "R_PHOTO" V 4316 4500 50  0000 C CNN
F 2 "" V 4600 4250 50  0001 L CNN
F 3 "~" H 4550 4450 50  0001 C CNN
	1    4550 4500
	1    1    1    0
$EndComp
Wire Wire Line
	3600 3400 3600 3900
Wire Wire Line
	3600 4300 3600 4500
Wire Wire Line
	3600 4500 4000 4500
Wire Wire Line
	5550 4500 5550 3400
Wire Wire Line
	4000 4850 4000 4500
Connection ~ 4000 4500
Wire Wire Line
	4000 4500 4400 4500
Wire Wire Line
	4550 4850 4000 4850
Wire Wire Line
	4700 4500 5300 4500
Wire Wire Line
	5300 5250 5300 4500
Wire Wire Line
	4550 5250 5300 5250
Connection ~ 5300 4500
Wire Wire Line
	5300 4500 5550 4500
Wire Wire Line
	3600 3400 4150 3400
Wire Wire Line
	5550 3400 5450 3400
Wire Wire Line
	4450 3400 4850 3400
$EndSCHEMATC

h="~"
i='"'

f = open("rajz.sch", "w")
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

Amperc="MES1"
An="Amperemeter_DC"

f.write("$Comp\n")
f.write("L Device:Amperemeter_DC MES1\n")
f.write("U 1 1 6001AF81\n")
f.write("P 3600 4100\n")
f.write("F 0 "+i+Amperc+i+" H 3753 4146 50  0000 L CNN\n")
f.write("F 2 "+i+i+" V 3600 4200 50  0001 C CNN\n")
f.write("F 3 "+i+h+i+" V 3600 4200 50  0001 C CNN\n")
f.write("	1    3600 4100\n")
f.write("	1    0    0    -1\n")
f.write("$EndComp\n")

Batterc="BT1"
Bn="Battery_Cell"

f.write("$Comp\n")
f.write("L Device:Battery_Cell BT1\n")
f.write("U 1 1 600230B0\n")
f.write("P 4350 3400\n")
f.write("F 0 "+i+Batterc+i+" H 4468 3496 50  0000 L CNN\n")
f.write("F 1 "+i+Bn+i+" H 4468 3405 50  0000 L CNN\n")
f.write("F 2 "+i+i+" V 4350 3460 50  0001 C CNN\n")
f.write("F 3 "+i+h+i+" V 4350 3460 50  0001 C CNN\n")
f.write("	1    4350 3400\n")
f.write("	1    -1   -1   0\n")
f.write("$EndComp\n")

Voltc="MES2"
Vn="Voltmeter_DC"

f.write("$Comp\n")
f.write("L Device:Voltmeter_DC MES2\n")
f.write("U 1 1 600243AC\n")
f.write("P 4550 5050\n")
f.write("F 0 "+i+Voltc+i+" H 4703 5096 50  0000 L CNN\n")
f.write("F 1 "+i+Vn+i+" H 4703 5005 50  0000 L CNN\n")
f.write("F 2 "+i+i+" V 4550 5150 50  0001 C CNN\n")
f.write("F 3 "+i+h+i+" V 4550 5150 50  0001 C CNN\n")
f.write("	1    4550 5050\n")
f.write("	1    0    0    -1\n")
f.write("$EndComp\n")

Circc="CB1"
Cn="CircuitBreaker_1P"

f.write("$Comp\n")
f.write("L Device:CircuitBreaker_1P CB1\n")
f.write("U 1 1 6001C3B0\n")
f.write("P 5150 3400\n")
f.write("F 0 "+i+Circc+i+" H 5202 3446 50  0000 L CNN\n")
f.write("F 1 "+i+Cn+i+" H 5202 3355 50  0000 L CNN\n")
f.write("F 2 "+i+i+" H 5150 3400 50  0001 C CNN\n")
f.write("F 3 "+i+h+i+" H 5150 3400 50  0001 C CNN\n")
f.write("	1    5150 3400\n")
f.write("	1    1    1    0\n")
f.write("$EndComp\n")

Rc="R1"
Rn="R_PHOTO"

f.write("$Comp\n")
f.write("L Device:R_PHOTO R1\n")
f.write("U 1 1 6003C928\n")
f.write("P 4550 4500\n")
f.write("F 0 "+i+Rc+i+" V 4225 4500 50  0000 C CNN\n")
f.write("F 1 "+i+Rn+i+" V 4316 4500 50  0000 C CNN\n")
f.write("F 2 "+i+i+" V 4600 4250 50  0001 L CNN\n")
f.write("F 3 "+i+h+i+" H 4550 4450 50  0001 C CNN\n")
f.write("	1    4550 4500\n")
f.write("	1    1    1    0\n")
f.write("$EndComp\n")

f.write("Wire Wire Line\n")
f.write("	3600 3400 3600 3900\n")
f.write("Wire Wire Line\n")
f.write("	3600 4300 3600 4500\n")
f.write("Wire Wire Line\n")
f.write("	3600 4500 4000 4500\n")
f.write("Wire Wire Line\n")
f.write("	5550 4500 5550 3400\n")
f.write("Wire Wire Line\n")
f.write("	4000 4850 4000 4500\n")
f.write("Connection ~ 4000 4500\n")
f.write("Wire Wire Line\n")
f.write("	4000 4500 4400 4500\n")
f.write("Wire Wire Line\n")
f.write("	4550 4850 4000 4850\n")
f.write("Wire Wire Line\n")
f.write("	4700 4500 5300 4500\n")
f.write("Wire Wire Line\n")
f.write("	5300 5250 5300 4500\n")
f.write("Wire Wire Line\n")
f.write("	4550 5250 5300 5250\n")
f.write("Connection ~ 5300 4500\n")
f.write("Wire Wire Line\n")
f.write("	5300 4500 5550 4500\n")
f.write("Wire Wire Line\n")
f.write("	3600 3400 4150 3400\n")
f.write("Wire Wire Line\n")
f.write("	5550 3400 5450 3400\n")
f.write("Wire Wire Line\n")
f.write("	4450 3400 4850 3400\n")


f.write("$EndSCHEMATC\n")
f.close()

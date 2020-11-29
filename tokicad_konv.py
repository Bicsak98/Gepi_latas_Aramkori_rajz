from skidl import * 
import cv2
import numpy as np

#két ellenállás létrehozása
rup = Part("Device", 'R', value='1K', footprint='Resistor_SMD.pretty:R_0805_2012Metric')                            
rlow = skidl.Part("Device", 'R', value='500', footprint='Resistor_SMD.pretty:R_0805_2012Metric')

#háló létrehozása
v_in = skidl.Net('VIN')

#rup hozzáfűzése a hálohoz
rup[1] += v_in

gnd = skidl.Net('GND')
rlow[1] += gnd

v_out = skidl.Net('VO')
v_out += rup[2], rlow[2]

up[2] += rlow[2]
v_out = skidl.Net('VO')
v_out += rlow[2]

skidl.generate_xml()


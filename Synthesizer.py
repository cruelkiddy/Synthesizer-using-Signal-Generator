import visa
import time
'''Hello world!'''
Scale = [1, 130.816, 146.836, 164.818, 174.618, 196.002, 220.005, 246.947, 261.632, 293.672, 329.636, 349.237, 392.005, 440.010, 493.895] # Scale
LZLH = [1,2,3,1,0,1,2,3,1,0,3,4,5,0,3,4,5,0,5,6,5,4,3,1,5,6,5,4,3,1,0,3,-2,1,0,3,-2,1] # Melody
LZLH_JZ = [2,2,2,2,0,2,2,2,2,0,2,2,4,0,2,2,4,0,1,1,1,1,2,2,1,1,1,1,2,2,0,2,2,4,0,2,2,4] # Delay Table

rm = visa.ResourceManager()
print("instruments list: "+str(rm.list_resources()))
dg = rm.open_resource('USB0::0x1AB1::0x0641::DG4E192200864::INSTR') # Replace with your device's address 
print(dg.query('*IDN?'))
dg.write("OUTP1 ON")
for i in range(len(LZLH)):
    if LZLH[i] == 0:
        dg.write("OUTP1 OFF")
        time.sleep(0.25*LZLH_JZ[i])
        dg.write("OUTP1 ON")
        continue
    dg.write("SOUR1:APPL:SQU "+str(Scale[LZLH[i]+7]*4)+",10,5,0") 
    time.sleep(0.25*LZLH_JZ[i])
    print(LZLH[i])
dg.write("OUTP1 OFF")

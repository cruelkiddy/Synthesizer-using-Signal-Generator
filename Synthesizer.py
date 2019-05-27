import visa
import time
'''Hello world!'''
'''
Scale = [1, 130.816, 146.836, 164.818, 174.618, 196.002, 220.005, 246.947, 261.632, 293.672, 329.636, 349.237, 392.005, 440.010, 493.895]
LZLH = [1,2,3,1,0,1,2,3,1,0,3,4,5,0,3,4,5,0,5,6,5,4,3,1,5,6,5,4,3,1,0,3,-2,1,0,3,-2,1]
LZLH_JZ = [2,2,2,2,0,2,2,2,2,0,2,2,4,0,2,2,4,0,1,1,1,1,2,2,1,1,1,1,2,2,0,2,2,4,0,2,2,4]



rm = visa.ResourceManager()
print("instruments list: "+str(rm.list_resources()))
#m3 = input("choose an instrument(ex. 16): ")
dg = rm.open_resource('USB0::0x1AB1::0x0641::DG4E192200864::INSTR')
print(dg.query('*IDN?'))
dg.write("OUTP1 ON")
for i in range(len(LZLH)):
    if LZLH[i] == 0:
        dg.write("OUTP1 OFF")
        time.sleep(0.25*LZLH_JZ[i])
        dg.write("OUTP1 ON")
        continue
    dg.write("SOUR1:APPL:SQU "+str(Scale[LZLH[i]+7]*4)+",2,1,0")  #
    time.sleep(0.25*LZLH_JZ[i])
    print(LZLH[i])
dg.write("OUTP1 OFF")
'''

rm = visa.ResourceManager()
print("instruments list: "+str(rm.list_resources()))
#m3 = input("choose an instrument(ex. 16): ")
dg = rm.open_resource('USB0::0x1AB1::0x0641::DG4E192200864::INSTR')
print(dg.query('*IDN?'))
dg.write("OUTP1 ON")

tmpCount = 0

SampleList = []
with open("C:\\Users\\84368\\Desktop\\Sample_Amp.txt", "r") as f:
    for line in f:
        SampleList.append(line.strip('\n'))
print(SampleList)
f.close()
# "SOUR1:APPL:CUST ,1,1,0,0"

while True:
    for i in SampleList:
        dg.write("SOUR1:APPL:CUST 1," + i + ",0,0")
    tmpCount += 1
    if tmpCount > 100:
        break
dg.write("OUTP1 OFF")

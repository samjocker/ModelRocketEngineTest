import serial
import time
import keyboard
from datetime import datetime

state_run = 1
state_catch = 0

COM_PORT = 'COM4'
BAUD_RATES = 9600
ser = serial.Serial(COM_PORT, BAUD_RATES)
time.sleep(2)
print("序列阜連線成功")

seconds = time.time()
NowTime = time.localtime(seconds)
name = "trst"+"%d"%NowTime.tm_mon+"-%d"%NowTime.tm_mday+"_%d"%NowTime.tm_hour+"-%d"%NowTime.tm_min+"-%d"%NowTime.tm_sec+".txt"
data = open(name, "wt")
data = open(name, "at")

while state_run:
    if keyboard.is_pressed("q"):
        break
    date_s = (datetime.now().strftime('%M:%S.%f')[:-3])
    data_raw = ser.readline()
    data_final = data_raw.decode()
    print(data_final, end="")
    if state_catch == 1:
        print(date_s+" "+data_final.strip().lstrip().rstrip("\n"), file=data)
    if data_final == "python start run\r\n":
        state_catch = 1   

data.close

print(name)


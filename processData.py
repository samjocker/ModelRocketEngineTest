name = input("輸入檔名:")

data_read = open(name, "rt")

start_time = input("輸入開始時間(min:sec.msec):").split(":")
end_time = input("輸入結束時間(min:sec.msec):").split(":")

start_min = int(start_time[0])
end_min = int(end_time[0])
start_sec = float(start_time[1])
end_sec = float(end_time[1])
print(start_min)
print(end_min)
print(start_sec)
print(end_sec)
state = 1
num = 0
total_thrust = 0
total_impulse_kg = 0.0
line1 = data_read.readline()
line2 = data_read.readline()

while(state):
    time1_min = int(line1[0:2])
    time2_min = int(line2[0:2])
    time1_sec = float(line1[3:9])
    time2_sec = float(line2[3:9])
    line1_g = int(line1[10:14])
    line2_g = int(line2[10:14])
    if time1_min >= start_min and time1_sec >= start_sec:
        num += 1
        total_thrust += line1_g
        if time1_min == time2_min:
            past_time = time2_sec - time1_sec
        elif time1_min > time2_min:
            past_time = (time2_sec+60.0)-time1_sec
        total_impulse_kg += (line1_g+line2_g)*past_time/2/1000
    if time1_min >= end_min and time1_sec >= end_sec:
        state = 0
        break
    
    line1 = line2
    line2 = data_read.readline()

average_thrust_kg = total_thrust/num/1000
average_thrust_lb = average_thrust_kg*2.20462
total_impulse_lb = total_impulse_kg*2.20462

print("平均推力(kg):", average_thrust_kg, "(kg)")
print("總衝量(kg):", total_impulse_kg, "(kg)")
print("平均推力(lb):", average_thrust_lb, "(lb)")
print("總衝量(lb):", total_impulse_lb, "(lb)")

data_read.close()
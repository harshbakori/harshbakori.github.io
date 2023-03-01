from sys import stdout
from sgp4.conveniences import dump_satrec
import requests
from sgp4.api import Satrec
from sgp4.api import jday , WGS84,WGS72

url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=stations&FORMAT=tle"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)


f = open("demofile2.txt", "w")
f.write(response.text)
f.close()

satalite_list=[]
obj_dic={}
counter_val = 0
for line in response.text.splitlines():
    # if line[0] == "HSU-SAT1":
        # print(i)
        if line[0] != "1" and line[0] != "2":
            # print("name = ",line)
            obj_dic['names']=line
            counter_val+=1
        if line[0] == "1":
            # print("line1 = ",line)
            obj_dic['line1']=line
            counter_val+=1
        if line[0] == "2":
            # print("line2 = ",line)
            obj_dic['line2']=line
            counter_val+=1
        if counter_val == 3:
            # print(counter_val)
            satellite = Satrec.twoline2rv(obj_dic["line1"], obj_dic["line2"],WGS72)
            obj_dic['sat_data_obj']=satellite
            counter_val = 0
            satalite_list.append(obj_dic)
            obj_dic={}


jd, fr = jday(2023, 2, 27, 23, 11, 0)


for i in satalite_list:
    if i['line2'] == "2 53462  51.6255 132.2555 0007984  15.0436 345.0808 15.97153441 31143":
        print(i)
        e, r, v = i["sat_data_obj"].sgp4(jd, fr)
        print(e)
        print("r:",r)
        print("v:",v)   # ? lingituted ?
        print("===============================================================================================")
        print(i["sat_data_obj"].gsto)
    # stdout.writelines(dump_satrec(i["sat_data_obj"]))
    # 4.291346630347583      2:15   SL-4 R/B
    # 4.291346630347583      2:26
    # 6.2533566616080165     10:50



# import numpy as np
# np.set_printoptions(precision=2)



# jd, fr = jday(2022, 12, 9, 12, 0, 0)

# e, r, v = satellite.sgp4(jd, fr)

# print(e)
# print(r)
# print(v)


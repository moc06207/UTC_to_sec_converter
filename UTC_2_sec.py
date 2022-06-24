import csv
import math
import numpy as np
import time as timee
import copy
import datetime

def main():

    # when you have csv about UTC information, you can use this code
    # if you have ros time, it is inaccurate
    # because yout time is your county or internal time
    # so, accurate time information is needed

    # if you want to practice this code, you convert bag file to csv
    # the csv file include time information

    f = open('UTC.csv', 'r')
    rdr = csv.reader(f)
    UTC = []
    for line in rdr:
        row_list = []
        for i in range(len(line)):
            num = float(line[i])
            row_list.append(num)
        UTC.append(row_list)

    q = open('UTC_2_sec.csv', 'w', newline='')
    wr = csv.writer(q)

    time_list = []
    for i in range(len(UTC)):

        year = int(UTC[i][0] + 2000)
        month = int(UTC[i][1])
        day = int(UTC[i][2])
        hour = int(UTC[i][3])
        min = int(UTC[i][4])
        sec = int(UTC[i][5])
        ms = int(UTC[i][6])
        ns = int(UTC[i][5])

        #t = datetime.datetime(year,month,day,hour,min,sec,ms)
        t = datetime.datetime(year, month, day, hour, min, sec, ms*1000+ns)
        t = (t - datetime.datetime(1970, 1, 1)).total_seconds()
        t = t * 1000000000
        t = int(t)
        time_list.append([t])
    time_list = np.array(time_list)

    for i in range(len(time_list)):
        wr.writerow(time_list[i])

    q.close()

    f.close()

if __name__ == '__main__':
    main()

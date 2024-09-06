import csv
import io 
from datetime import datetime, timedelta

def getdata(s):
    f = io.StringIO(s)
    reader = csv.reader(f, delimiter=',')
    result = next(reader)
    return result

ALL = open("file/TKB.csv", mode = "r", encoding="utf-8-sig")
CID = open("file/class.txt", mode = "r")
OUT = open("file/calendar.csv", mode = "w")
temp = open("file/template.csv", mode = "r")

FIRST = open("file/firstweek.txt","r").readline()
FIRST = datetime.strptime(FIRST, '%m/%d/%Y').date()

temp = temp.readline()
OUT.write(temp)
OUT.write("\n")

courses = []
ID = CID.readline();
while ID != '': 
    courses.append(ID.strip())
    ID = CID.readline()
    
ID = 'Mã_lớp'
TIME = 'Thời_gian'
DAY = 'Thứ'
WEEK = 'Tuần'
SUB = 'Mã_HP'
LOC = 'Phòng'

def Out(data):
    block = data[WEEK].split(",")
    start = data[TIME][:4]
    start = start[:2] + ":" + start[2:]
    stop = data[TIME][-4:]
    stop = stop[:2] + ":" + stop[2:]
    for week in block:
        if '-' in week:
            week = week.split("-")
            for date in range((int)(week[0]), (int)(week[1]) + 1):
                date = (str)((FIRST + timedelta(weeks=(date-1)) + timedelta(days = ((int)(data[DAY]) - 2))).strftime('%m/%d/%Y'))
                result = data[SUB] + "," + date + "," + start + "," + date + "," + stop + "," + "FALSE" + "," + "," + data[LOC] + "\n"
                OUT.write(result)
        else:
            date = (str)((FIRST + timedelta(weeks=((int)(week)-1)) + + timedelta((int)(data[DAY]) - 2)).strftime('%m/%d/%Y'))
            result = data[SUB] + "," + date + "," + start + "," + date + "," + stop + "," + "FALSE" + "," + "," + data[LOC] + "\n"
            OUT.write(result)

ALL.readline()
ALL.readline()
head = ALL.readline().split(",")
data = ALL.readline()
while data != '':
    data = getdata(data)
    data = dict(zip(head, data))
    if data[ID] in courses:
        Out(data)
    data = ALL.readline()
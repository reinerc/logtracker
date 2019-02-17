import datetime
import pandas as pd

path = "/var/log/"
#path = ""

f = open(path+"syslog","r")
l = f.readlines()

def unzip(li):
  return tuple(map(list,zip(*li)))

year = datetime.datetime.today().year

def getentry(s,year=datetime.datetime.today().year):
   xs=s.split(" ",5)
   timestring = str(year)+' '+' '.join(xs[0:3])
   entrytime = datetime.datetime.strptime(timestring,"%Y %b %d %X")
   return (entrytime,xs[4],xs[5])

#print(l[:3])
dd = dict(zip(["Time","Tag","Attr"],unzip(map(getentry,l))))
data = pd.DataFrame(dd)

print(data.head())
#print(unzip(getentry(l[0])))
print(data.groupby(['Time','Tag']).count())
#print(data.groupby(['Tag']).count())
#print(data[data['Tag'].str.contains("CRON")])

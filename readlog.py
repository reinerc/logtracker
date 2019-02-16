import datetime
import pandas as pd

f = open("syslog","r")
l = f.readlines()

def unzip(li):
  return tuple(map(list,zip(*li)))

year = datetime.datetime.today().year

def getentry(s,year=datetime.datetime.today().year):
   xs=s.split(" ",5)
   timestring = str(year)+' '+' '.join(xs[0:3])
   entrytime = datetime.datetime.strptime(timestring,"%Y %b %d %X")
   return (entrytime,xs[4],xs[5])

print(l[:3])
dd = dict(zip(["Time","Entry","Attr"],unzip(map(getentry,l[:3]))))
data = pd.DataFrame(dd)
print(data)
#print(unzip(getentry(l[0])))

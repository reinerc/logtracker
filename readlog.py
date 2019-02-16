import datetime

f = open("syslog","r")
l = f.readlines()

year = datetime.datetime.today().year

def getentry(s,year=datetime.datetime.today().year):
   xs=s.split(" ",5)
   timestring = str(year)+' '+' '.join(xs[0:3])
   entrytime = datetime.datetime.strptime(timestring,"%Y %b %d %X")
   return (entrytime,xs[4],xs[5])

print(getentry(l[0]))

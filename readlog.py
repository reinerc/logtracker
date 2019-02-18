import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import sys




#_plot = True
_plot = False

#
# Default file
#

#path = "/var/log/"
path = ""
filename = path+"syslog"
#f = open(path+"syslog", "r")


def unzip(li):
  return tuple(map(list, zip(*li)))

year = datetime.datetime.today().year

def getentry(s,year=datetime.datetime.today().year):
   xs = s.split(" ", 5)
   timestring = str(year)+' '+' '.join(xs[0:3])
   entrytime = datetime.datetime.strptime(timestring, "%Y %b %d %X")
   return (entrytime, xs[4], xs[5])

#print(l[:3])
def readlog(inputlog):
   "read lines from file or stream inputlog and returns a dataframe"
   l = inputlog.readlines()
   dd = dict(zip(["Time", "Tag", "Attr"], unzip(map(getentry, l))))
   return pd.DataFrame(dd)

if len(sys.argv) == 1:
  f = open(filename,"r")
else:
  if sys.argv[1] == "-":
    f = sys.stdin
  else:
    f = open(sys.argv[1],"r")
data = readlog(f)

print(data.head())
#print(unzip(getentry(l[0])))
print(data.groupby(['Time', 'Tag']).count())
#print(data.groupby(['Tag']).count())
#print(data[data['Tag'].str.contains("CRON")])

print (sys.argv)

if _plot:
   tl = data.groupby(['Time']).count()['Tag']
   tl.cumsum().plot()
   tl.plot(style='ro')
   plt.show()
   

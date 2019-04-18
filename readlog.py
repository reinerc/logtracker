import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import re
import gzip
import sys

_plot = True
#_plot = False

if _plot:
  import visual

#
# Default file
#

#path = "/var/log/"
path = ""
filename = path+"syslog"
#f = open(path+"syslog", "r")


def gopen(filename,mode="r"):
  if filename.endswith(".gz"):
#    print("gzip")
    return gzip.open(filename,mode)
  else:
 #   print("no gzip")
    return open(filename,mode)

def unzip(li):
  liste = list(li)
  return tuple(map(list, zip(*liste)))

year = datetime.datetime.today().year

def getentry(s,year=datetime.datetime.today().year):
  try:
   xs = s.split(maxsplit= 5)
   timestring = str(year)+' '+' '.join(xs[0:3])
   entrytime = datetime.datetime.strptime(timestring, "%Y %b %d %X")
   return (entrytime, xs[4], xs[5])
  except:
   # skip syntactic incorrect lines
   return None

#print(l[:3])
def readlog(inputlog):
   "read lines from file or stream inputlog and returns a dataframe"
   l = inputlog.readlines()
#   print(l)
   dd = dict(zip(["Time", "Tag", "Attr"], unzip(filter(None,map(getentry, l)))))
   return pd.DataFrame(dd)


if __name__ == "__main__":

  if len(sys.argv) == 1:
    f = gopen(filename,"rt")
  else:
    if sys.argv[1] == "-":
      f = sys.stdin
    else:
      f = gopen(sys.argv[1],"rt")
  data = readlog(f)
  print(data.head())
  data['Tag_noID'] = data['Tag'].apply(lambda s:re.sub("\[.*\]","[]",s))
  print(data.head())
  #print(unzip(getentry(l[0])))
  #print(data.groupby(['Time', 'Tag']).count())
  #print(data.groupby(['Tag']).count())
  #print(data[data['Tag'].str.contains("CRON")])
  print(data.groupby(['Tag_noID','Tag']).count())
  print (sys.argv)
  
  if _plot:
     try:
       ax=data[data['Tag_noID']=='NetworkManager[]:'].groupby(['Time','Tag']).count()['Tag'].unstack().fillna(0).cumsum().plot()
       data[data['Tag_noID']=='kernel:'].groupby(['Time','Tag']).count()['Tag'].unstack().fillna(0).plot(style='o',ax=ax)
       plt.show()
     except:
       pass #if logfile is not syslog

     tl = data.groupby(['Time']).count()['Tag']
  #   tl.cumsum().plot()
  #   tl.plot(style='ro')
  #   plt.show()
     data2 = data.copy()
     data2['Tag'] = data2['Tag'].apply(lambda s:re.sub("\[.*\]","[]",s))
     h = data2.groupby(['Tag']).count()['Tag']
     
     dd = data2.groupby(['Time','Tag']).count()['Tag']
     df = dd.unstack().fillna(0)
  
  #   visual.plot_sep_df(data2)
  #   visual.plot_sep_df(data2,1)
     visual.plot_sep_df(df)
     sys.exit(0)
  
     visual.plot_hist_and_timeline(h,tl)
  
     df.plot()
     plt.show()
     df.cumsum().plot()   
     plt.show()

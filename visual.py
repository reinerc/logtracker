"""
===============
Aligning Labels
===============

Aligning xlabel and ylabel using `Figure.align_xlabels` and
`Figure.align_ylabels`

`Figure.align_labels` wraps these two functions.

Note that the xlabel "XLabel1 1" would normally be much closer to the
x-axis, and "YLabel1 0" would be much closer to the y-axis of their
respective axes.
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

def plot_hist_and_timeline(h,tl):

  fig = plt.figure(tight_layout=True)
  gs = gridspec.GridSpec(2, 2)

  ax = fig.add_subplot(gs[0, :])
# ax.plot(tl)
# ax.set_ylabel('YLabel0')
# ax.set_xlabel('XLabel0')
  tl.plot(style='ro',ax=ax)

  ax2 = fig.add_subplot(gs[1,1])
  h.plot(kind='barh',ax=ax2) 
#fig.align_labels()  # same as fig.align_xlabels(); fig.align_ylabels()
#fig.align_xlabels(); fig.align_ylabels()

  plt.show()

def plot_sep_df(df,partsize=4):
  size =len(df.columns)
  if size < partsize:
    partsize = size
  parts = int(len(df.columns) / partsize)
  lastsize = len(df.columns) % partsize
  if lastsize:
    frames = parts + 1
  else:
    frames = parts

  print((len(df.columns),":",parts,lastsize,frames,partsize))
  print(df.columns)
  for i in range(0,size,partsize):
     print(df.columns[i:i+partsize],i)
     ax = plt.subplot(frames,1,int(i / partsize)+1)
     print(df[df.columns[i:i+partsize]].head())
     dd = df[df.columns[i:i+partsize]]
     print(dd.head())
     dd.plot(style="o",ax=ax)

  if lastsize:
     ax = plt.subplot(frames,1,frames)
     print(df.columns[-lastsize:])
     df[df.columns[-lastsize:]].plot(style="o",ax=ax)
  plt.show()   

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
  ax.plot(tl)
  ax.set_ylabel('YLabel0')
  ax.set_xlabel('XLabel0')

  ax2 = fig.add_subplot(gs[1,1])
  h.plot(kind='barh',ax=ax2) 
#fig.align_labels()  # same as fig.align_xlabels(); fig.align_ylabels()
#fig.align_xlabels(); fig.align_ylabels()

  plt.show()


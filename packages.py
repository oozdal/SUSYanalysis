#!/usr/bin/python

from __future__ import division
from math import *
import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib, os
import matplotlib.cm as cm
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from scipy.interpolate import griddata
import scipy
import pylab, subprocess
import pandas as pd

pylab.rcParams['figure.figsize'] = (8.0, 6.0)

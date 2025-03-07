# -*- coding: utf-8 -*-
"""qVAR.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rFHl0C7p8pcc_-IwArBrPzp9bTgmSTWS
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def VaR(r, confidence, principal=1):
    var_threshold = np.percentile(r, (1 - confidence) * 100)
    out = principal * abs(var_threshold)
    return out

def percent_var(r, confidence):
    plt.hist(r, bins=50, alpha=0.75)
    plt.show()
    out = np.percentile(r, (1 - confidence) * 100)
    return abs(out)
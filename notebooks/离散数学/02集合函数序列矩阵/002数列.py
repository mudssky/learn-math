# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# %%
import matplotlib.pyplot as plt
from sympy import *	
import numpy as np

# %%
import numpy as np
import matplotlib.pyplot as plt

n = np.arange(1, 50)
y = 1/n

plt.scatter(n, y)
# plt.xscale('log')
plt.xlabel('n')
plt.ylabel('1/n')
plt.title('1/n Scatter Plot')
plt.show()


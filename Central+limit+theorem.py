
# coding: utf-8

# In[3]:

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from numpy.random import randint
from numpy import mean
from scipy import stats
from numpy.random import seed


# Binomial

# In[4]:

results = []
for num_trials in range(1, 1000):
    trials = np.random.binomial(60, .5, num_trials)
    mean_of_trials = trials.mean()
    results.append(mean_of_trials)
    
df = pd.DataFrame({ 'trials' : results})

df.plot()


# In[5]:

means = [mean(np.random.binomial(60, .5, 1000)) for _ in range(1000)]

plt.hist(means)
plt.show()


# Gamma

# In[6]:

results = []
for num_trials in range(1, 1000):
    trials = np.random.gamma(2, 2, num_trials)
    mean_of_trials = trials.mean()
    results.append(mean_of_trials)
    
df = pd.DataFrame({ 'trials' : results})

df.plot()


# In[7]:

means = [mean(np.random.gamma(2, 2, 1000)) for _ in range(1000)]

plt.hist(means)
plt.show()


# In[ ]:




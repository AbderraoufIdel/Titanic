import numpy as np
import pandas as pd

import os 
#for dirname, _, filenames in os.walk(r"C:\Users\abder\Desktop\folder0\Titanic"):
#   for filename in filenames:
#        print(os.path.join(dirname, filename))

train_data = pd.read_csv(r"C:\Users\abder\Desktop\folder0\Titanic\train.csv")
train_data.head()

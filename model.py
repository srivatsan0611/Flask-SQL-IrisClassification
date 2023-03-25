#%%

import pandas as pd
import numpy as np
import pickle

data = pd.read_csv("Iris.csv")
data.head()

#%%
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
data["Species"] = le.fit_transform(data["Species"])
data = data.drop(columns="Id")
data.head()

print(le.classes_)
# %%
data.head()
X = data.iloc[:,:-1].values
y = data.iloc[:,-1].values
model = RandomForestClassifier()
model.fit(X, y)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

# %%

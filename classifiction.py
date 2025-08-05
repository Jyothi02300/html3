from sklearn.linear_model import LogisticRegression
import numpy as np
x=np.array([[1],[2],[3],[4]])
y=np.array([0,0,1,1])
model = LogisticRegression()
model.fit(x, y)
print(model.predict([[5]]))
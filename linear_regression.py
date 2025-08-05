from sklearn.linear_model import LinearRegression
import numpy as np
x = np.array([[1000], [1500],[2000],[2500]])
y = np.array([30,45,60,75])
model = LinearRegression()
model.fit(x,y)
print(model.predict([[3000]]))
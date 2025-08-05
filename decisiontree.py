from sklearn.tree import DecisionTreeClassifier
import numpy as np
x=np.array([[20,35000],[25,30000],[35,40000],[26,50000]])
y=np.array([1,0,0,1])
model = DecisionTreeClassifier()
model.fit(x,y)
print(model.predict([[26,45000]]))
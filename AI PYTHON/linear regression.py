from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

x=np.array([5,15,25,35,45,55]).reshape((-1,1))
y=np.array([5,20,14,32,22,38])
print(x)
print(y)
plt.scatter(x,y)

model = LinearRegression().fit(x, y)
r_square =  model.score(x,y)
plt.title("linear regression")
plt.plot(x ,model.predict(x),c="blue",label = "fited")
print('coefficient of determination :',r_square)
est_coef = model.coef_
print('estimated coefficiennts:',est_coef)
ind_term = model.intercept_
print('independent term in linear model:',ind_term)

val = int(input("ENTER A  VALUE TO PREDICT : "))
y_predict=model.predict(np.array(val).reshape(-1,1))
print("predicted value of y:",y_predict)
plt.show()
plt.close()

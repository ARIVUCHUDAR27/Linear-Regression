# importing necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_squared_error as mse

#Dataset
data = pd.DataFrame({"Height": [1.4,2.7,3.8,4.4,5.9,6.9,7.0], "Weight":[1.8,3.6,4.8,5.9,6.6,7.6,8.8] }) #Load your own dataset
print(data.head())

#ScatterPlot
plt.scatter(data.Height, data.Weight, color = 'red', label = 'data points')
plt.xlim(1,9)
plt.ylim(1,9)
plt.xlabel('Height')
plt.ylabel('Weight')
plt.legend()

#Linear regression model
beta2=0.9 #Adjust accordingly
b=1.1
line2=[]
for i in range(len(data)):
    line2.append(data.Height[i]*beta2+b)
plt.scatter(data.Height,data.Weight,color='blue',label='Data points')
plt.plot(data.Height,line2,color='black',label='Line')
plt.xlim(1,9)
plt.ylim(1,9)
plt.xlabel('Height')
plt.ylabel('Weight')
plt.legend()
MSE=mse(Weight,line2)
plt.title("MSE:"+str(MSE)) 

def Error(Beta,data):
    b=1.1
    weight=[]
    Weigh=data.Weight
    for i in range(len(data.Height)):
        temp=data.Height[i]*beta+b
        weight.append(temp)
    MSE=mse(data.Weight,weight)
    return MSE
#Cost Function
slope = [i/100 for i in range(0,150)]
Cost = []
for i in slope:
    cost = Error( Beta = i, data = data)
    Cost.append(cost)
cost_table=pd.DataFrame({
    'BETA': slope,
    'COST': Cost
})
cost_table.head()
#Cost Function curve
plt.plot(cost_table.BETA,cost_table.COST,color='red',label='Cost FN')
plt.xlabel('BETA')
plt.ylabel('COST')
plt.legend()

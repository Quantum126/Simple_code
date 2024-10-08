import numpy as np
from matplotlib import pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


input2 = np.array([0.5,0.8])
weight2 = np.array([0.4,0.6])
bias= 0.2
learning_rate = 0.1
y_target = 1

error_list=[]
iteration_list=[]
# let do epoch 
for i in range(1000):
    # let make perceptron model


    print("epoch ", i,"\n")
    iteration_list.append(i)
    
    summation = np.matmul(input2,weight2) + bias
    print("sum ->",summation)
    y_predicated = sigmoid(summation)

    print("output of activation function -> ",y_predicated)
    error = y_target - y_predicated 
    error_list.append(error)
    print("error -> ",error)

    # gradient calculation 
    gradient= error * y_predicated * ( 1 - y_predicated)

    weight2 = weight2 + learning_rate * gradient * input2
    print("weight -> ",weight2)

    bias = bias + learning_rate * gradient 
    print("bias -> ",bias,"\n")

x =iteration_list
y = error_list

plt.title("graph of iteration and error")
plt.plot(x,y)

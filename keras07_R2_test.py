from keras.models import Sequential
from keras.layers import Dense

import numpy as np
x_train = np.array([1,2,3,4,5,6,7,8,9,10])
y_train = np.array([1,2,3,4,5,6,7,8,9,10])
x_test = np.array([11,12,13,14,15,16,17,18,19,20])
y_test = np.array([11,12,13,14,15,16,17,18,19,20])
# x_predict = np.array([21,22,23,24,25])


model = Sequential()
# model.add(Dense(1800, input_dim=1, activation='relu'))
model.add(Dense(1, input_shape=(1, ), activation='relu'))
model.add(Dense(8))
model.add(Dense(70))
model.add(Dense(555))
model.add(Dense(888))
model.add(Dense(1))

model.summary()

model.compile(loss='mse', optimizer='adam', #metrics=['accuracy']
                 metrics=['mse'])

model.fit(x_train,y_train, epochs=100,batch_size=1)

loss, mse = model.evaluate(x_test, y_test) # a[0], a[1]
print("mse : ", mse)    #1.0
print("loss : ", loss)  #0.0012...

y_predict = model.predict(x_test)
print(y_predict)

# RMSE 구하기
from sklearn.metrics import mean_squared_error
def RMSE (y_test, y_predict,batch_size=1):
    return np.sqrt(mean_squared_error(y_test, y_predict))
print("RMSE : " ,RMSE(y_test, y_predict))

#R2 구하기
from sklearn.metrics import r2_score
r2_y_predict = r2_score(y_test, y_predict)
print("R2 : ", r2_y_predict)

#문제 1. R2를 0.5 이하로 줄이시오
#레이어는 인풋과 아웃풋 포함 5개 이상, 노드는 각 레이더당 5개 이상
#batch_size = 1
#epochs = 100 이상

# mse :  105.0290298461914
# loss :  105.0290298461914
# [[5.6623664]
#  [5.6623664]
#  [5.6623664]
#  [5.6623664]
#  [5.6623664]
#  [5.6623664]
#  [5.6623664]
#  [5.6623664]
#  [5.6623664]
#  [5.6623664]]
# RMSE :  10.248367432918783
# R2 :  -11.730792126073979

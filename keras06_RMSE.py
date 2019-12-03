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
model.add(Dense(1800, input_shape=(1, ), activation='relu'))
model.add(Dense(1200))
model.add(Dense(600))
model.add(Dense(300))
model.add(Dense(150))
model.add(Dense(100))
model.add(Dense(50))
model.add(Dense(10))
model.add(Dense(5))
model.add(Dense(1))

model.summary()

model.compile(loss='mse', optimizer='adam', #metrics=['accuracy']
                 metrics=['mse'])

model.fit(x_train,y_train, epochs=100)

loss, mse = model.evaluate(x_test, y_test) # a[0], a[1]
print("mse : ", mse)    #1.0
print("loss : ", loss)  #0.0012...

# y_predict = model.predict(x_test)
# print(y_predict)

# # RMSE 구하기
# from sklearn.metrics import mean_squared_error
# def RMSE (y_test, y_predict):
#     return np.sqrt(mean_squared_error(y_test, y_predict))
# print("RMSE : " ,RMSE(y_test, y_predict))

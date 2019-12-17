#1.데이터  keras18
import numpy as np
x = np.array(range(1,101))
y = np.array(range(1,101))
print(x)

# x_train = x[:60]
# x_val = x[60:80]
# x_test = x[80:]
# y_train = y[:60]
# y_val = y[60:80]
# y_test = y[80:]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=33, test_size=0.4, shuffle=False)
x_val, x_test, y_val, y_test = train_test_split(x_test, y_test, random_state=33, test_size=0.5, shuffle=False)

#2.모델구성
from keras.models import Sequential
from keras.layers import Dense, Dropout, BatchNormalization
model = Sequential()


model = Sequential()
# model.add(Dense(1800, input_dim=1, activation='relu'))
model.add(Dense(1000, input_shape=(1, ), activation='relu'))
model.add(Dense(1000))
model.add(BatchNormalization())
model.add(Dense(1000))
model.add(Dropout(0.3)) # 같이써도 되긴하는데 그렇게 좋지는 않음 GAN이라는거에서는 둘다 쓴다고 합니다.
model.add(BatchNormalization())
model.add(Dense(1000))
model.add(Dense(1000))
model.add(BatchNormalization())
model.add(Dense(1000))
model.add(Dense(1000))
model.add(BatchNormalization())
model.add(Dense(1000))
model.add(Dense(1))

#model.summary()
#3.훈련
model.compile(loss='mse', optimizer='adam', #metrics=['accuracy']
                 metrics=['mse'])

# model.fit(x_train,y_train, epochs=100)
model.fit(x_train,y_train, epochs=10,batch_size=1,validation_data=(x_val, y_val))
# print("acc : ", acc)
lose, mse = model.evaluate(x_test, y_test, batch_size=1)
print("mise : ", mse)

y_predict = model.predict(x_test)
print(y_predict)

# loss, mse = model.evaluate(x_test, y_test) # a[0], a[1]
# print("mse : ", mse)    #1.0
# print("loss : ", loss)  #0.0012...


# RMSE 구하기
from sklearn.metrics import mean_squared_error
def RMSE (y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))
print("RMSE : " ,RMSE(y_test, y_predict))

#R2 구하기
from sklearn.metrics import r2_score
r2_y_predict = r2_score(y_test, y_predict)
print("R2 : ", r2_y_predict)

# mise :  173141508096.0
# [[-348552.72]
#  [-355444.06]
#  [-362352.47]
#  [-369254.72]
#  [-376148.34]
#  [-383046.97]
#  [-389952.6 ]
#  [-396851.25]
#  [-403756.1 ]
#  [-410658.2 ]
#  [-417559.97]
#  [-424457.9 ]
#  [-431348.66]
#  [-438247.84]
#  [-445159.78]
#  [-452053.16]
#  [-458962.56]
#  [-465865.03]
#  [-472751.75]
#  [-479660.7 ]]
# RMSE :  416102.16789310967
# R2 :  -5207248544.123177
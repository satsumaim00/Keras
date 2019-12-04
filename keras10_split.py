#1.데이터
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
from keras.layers import Dense
model = Sequential()


model = Sequential()
# model.add(Dense(1800, input_dim=1, activation='relu'))
model.add(Dense(800, input_shape=(1, ), activation='relu'))
model.add(Dense(500))
model.add(Dense(300))
model.add(Dense(150))
model.add(Dense(100))
model.add(Dense(50))
model.add(Dense(10))
model.add(Dense(5))
model.add(Dense(1))

#model.summary()
#3.훈련
model.compile(loss='mse', optimizer='adam', #metrics=['accuracy']
                 metrics=['mse'])

# model.fit(x_train,y_train, epochs=100)
model.fit(x_train,y_train, epochs=100,batch_size=1,validation_data=(x_val, y_val))
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


# mise :  2.76914119720459
# [[ 82.52985 ]
#  [ 83.54376 ]
#  [ 84.557686]
#  [ 85.57161 ]
#  [ 86.58555 ]
#  [ 87.599464]
#  [ 88.61338 ]
#  [ 89.62729 ]
#  [ 90.64121 ]
#  [ 91.65513 ]
#  [ 92.66906 ]
#  [ 93.682976]
#  [ 94.69692 ]
#  [ 95.71086 ]
#  [ 96.7248  ]
#  [ 97.73872 ]
#  [ 98.752686]
#  [ 99.76661 ]
#  [100.78054 ]
#  [101.79448 ]]
# RMSE :  1.66406831368488
# R2 :  0.9167180946583446
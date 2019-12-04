#1.데이터
import numpy as np
x = np.array([range(1,101), range(101,201)])
y = np.array([range(1,101), range(101,201)])
print(x)


print(x.shape)

x = np.transpose(x)
y = np.transpose(y)

print(x.shape)

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
model.add(Dense(800, input_shape=(2, ), activation='relu'))
model.add(Dense(500))
model.add(Dense(300))
model.add(Dense(150))
model.add(Dense(100))
model.add(Dense(50))
model.add(Dense(10))
model.add(Dense(5))
model.add(Dense(2))

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

#멀티 레이어 퍼셉트론
# mise :  50.000816345214844
# [[ 76.762695 185.54173 ]
#  [ 77.52039  186.79773 ]
#  [ 78.26787  188.06512 ]
#  [ 79.0135   189.33252 ]
#  [ 79.75865  190.60028 ]
#  [ 80.503235 191.86823 ]
#  [ 81.24783  193.13626 ]
#  [ 81.991844 194.40504 ]
#  [ 82.739975 195.67674 ]
#  [ 83.48492  196.95795 ]
#  [ 84.2304   198.24115 ]
#  [ 84.9752   199.52524 ]
#  [ 85.71988  200.80925 ]
#  [ 86.464554 202.09395 ]
#  [ 87.2076   203.37924 ]
#  [ 87.94726  204.67522 ]
#  [ 88.686    205.97536 ]
#  [ 89.42488  207.27693 ]
#  [ 90.16376  208.57857 ]
#  [ 90.90261  209.88013 ]]
# RMSE :  7.0711220722585395
# R2 :  -0.503782477015997
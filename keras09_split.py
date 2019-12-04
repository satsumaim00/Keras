#1.데이터
import numpy as np
x = np.array(range(1,101))
y = np.array(range(1,101))
print(x)

x_train = x[:60]
x_val = x[60:80]
x_test = x[80:]
y_train = y[:60]
y_val = y[60:80]
y_test = y[80:]

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

# mise :  5.794249534606934
# [[78.818245]
#  [79.7949  ]
#  [80.771576]
#  [81.748245]
#  [82.72492 ]
#  [83.701584]
#  [84.67829 ]
#  [85.654945]
#  [86.631615]
#  [87.6083  ]
#  [88.584984]
#  [89.56163 ]
#  [90.53834 ]
#  [91.51501 ]
#  [92.49168 ]
#  [93.46835 ]
#  [94.445015]
#  [95.4217  ]
#  [96.39838 ]
#  [97.37504 ]]
# RMSE :  2.407123643047714
# R2 :  0.8257370155512993

#keras10
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
from keras.models import Sequential,load_model
from keras.layers import Dense

model = load_model("./save/savetest01.h5")
model.add(Dense(100, name='dense_100000'))
model.add(Dense(1, name='dense_200000'))

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


# mise :  18.759395599365234
# [[77.096436]
#  [78.05219 ]
#  [79.007965]
#  [79.96377 ]
#  [80.91954 ]
#  [81.8753  ]
#  [82.8311  ]
#  [83.786835]
#  [84.74263 ]
#  [85.6984  ]
#  [86.65419 ]
#  [87.60995 ]
#  [88.565735]
#  [89.52152 ]
#  [90.47729 ]
#  [91.433075]
#  [92.38883 ]
#  [93.34462 ]
#  [94.30042 ]
#  [95.25619 ]]
# RMSE :  4.331214067386921
# R2 :  0.4358070587208914
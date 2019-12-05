#1.데이터
import numpy as np
x = np.array([range(1,101), range(101,201)])
y = np.array([range(201,301)])
# print(x)

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
model.add(Dense(500, input_shape=(2, ), activation='relu'))
model.add(Dense(300))
model.add(Dense(100))
model.add(Dense(50))
model.add(Dense(10))
model.add(Dense(5))
model.add(Dense(1))#이거 바뀜

#model.summary()
#3.훈련
model.compile(loss='mse', optimizer='adam', #metrics=['accuracy']
                 metrics=['mse'])

# model.fit(x_train,y_train, epochs=100)
model.fit(x_train,y_train, epochs=10,batch_size=1,validation_data=(x_val, y_val))
# print("acc : ", acc)
lose, mse = model.evaluate(x_test, y_test, batch_size=1)
print("mise : ", mse)

# aaa = np.array([[101,102,103],[201,202,203]])   # 2, 3
# aaa = np.transpose(aaa)

# y_predict = model.predict(aaa)
# print(y_predict)

y_predict = model.predict(x_test) #모양 맞추기
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

# mise :  55.739112854003906
# [[285.53677]
#  [286.79675]
#  [288.06897]
#  [289.35065]
#  [290.63345]
#  [291.9164 ]
#  [293.19882]
#  [294.48123]
#  [295.76373]
#  [297.0472 ]
#  [298.34158]
#  [299.63654]
#  [300.9465 ]
#  [302.26062]
#  [303.582  ]
#  [304.90457]
#  [306.2272 ]
#  [307.54974]
#  [308.87238]
#  [310.19507]]
# RMSE :  7.465863270604807
# R2 :  -0.6763643421162675

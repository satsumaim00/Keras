#1.데이터
import numpy as np
x = np.array(range(1,101))
y = np.array(range(1,101))
print(x)


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=33, test_size=0.4, shuffle=False)
x_val, x_test, y_val, y_test = train_test_split(x_test, y_test, random_state=33, test_size=0.5, shuffle=False)

#2.모델구성
from keras.models import Sequential, Model
from keras.layers import Dense, Input
#model = Sequential()
# input1 = Input(shape=(1,))
# dense1 = Dense(11, activation='relu')(input1)
# dense2 = Dense(3)(dense1)
# dense3 = Dense(10)(dense2)
# dense4 = Dense(5)(dense3)
# dense5 = Dense(8)(dense4)
# dense6 = Dense(9)(dense5)
# dense7 = Dense(2)(dense6)
# dense8 = Dense(7)(dense7)
# dense9 = Dense(6)(dense8)
# dense10 = Dense(4)(dense9)
# output1 = Dense(1)(dense10)

input1 = Input(shape=(1,))
xx = Dense(11, activation='relu')(input1)
xx = Dense(3)(xx)
xx = Dense(10)(xx)
xx = Dense(5)(xx)
xx = Dense(8)(xx)
xx = Dense(9)(xx)
xx = Dense(2)(xx)
xx = Dense(7)(xx)
xx = Dense(6)(xx)
xx = Dense(4)(xx)
output1 = Dense(1)(xx)

model = Model(inputs = input1, outputs= output1)
model.summary()
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

#레이어를 10개 이상 늘리시오.

# mise :  5.2386893434341886e-11
# [[ 80.99999 ]
#  [ 82.      ]
#  [ 82.99999 ]
#  [ 84.      ]
#  [ 84.99999 ]
#  [ 85.99999 ]
#  [ 87.00001 ]
#  [ 88.      ]
#  [ 88.999985]
#  [ 90.      ]
#  [ 91.00001 ]
#  [ 92.00001 ]
#  [ 92.999985]
#  [ 94.00001 ]
#  [ 94.99999 ]
#  [ 95.99998 ]
#  [ 97.00001 ]
#  [ 98.000015]
#  [ 98.999985]
#  [100.000015]]
# RMSE :  1.0653869662299302e-05
# R2 :  0.9999999999965863

# xx로 바꾼후
# mise :  107.87895202636719
# [[ 90.27347 ]
#  [ 91.38841 ]
#  [ 92.50335 ]
#  [ 93.61827 ]
#  [ 94.733215]
#  [ 95.84812 ]
#  [ 96.96307 ]
#  [ 98.07797 ]
#  [ 99.19292 ]
#  [100.30785 ]
#  [101.42276 ]
#  [102.53772 ]
#  [103.65262 ]
#  [104.76758 ]
#  [105.8825  ]
#  [106.99742 ]
#  [108.112366]
#  [109.22727 ]
#  [110.34221 ]
#  [111.457146]]
# RMSE :  10.386476262129301
# R2 :  -2.2444778689857277
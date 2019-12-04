#2.모델구성
from keras.models import Sequential
from keras.layers import Dense
model = Sequential()
#1.데이터
import numpy as np
x_train = np.array([1,2,3,4,5,6,7,8,9,10])
y_train = np.array([1,2,3,4,5,6,7,8,9,10])
x_test = np.array([11,12,13,14,15,16,17,18,19,20])
y_test = np.array([11,12,13,14,15,16,17,18,19,20])
x_val = np.array([101,102,103,104,105])
y_val = np.array([101,107,13,1104,2105])
# x_predict = np.array([21,22,23,24,25])


model = Sequential()
# model.add(Dense(1800, input_dim=1, activation='relu'))
model.add(Dense(1200, input_shape=(1, ), activation='relu'))
model.add(Dense(700))
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


# mise :  0.02440338395535946
# [[10.825097 ]
#  [11.8288145]
#  [12.832675 ]
#  [13.836815 ]
#  [14.841303 ]
#  [15.8459835]
#  [16.850805 ]
#  [17.855686 ]
#  [18.860594 ]
#  [19.865524 ]]
# RMSE :  0.1562151573408654
# R2 :  0.9970420393475113
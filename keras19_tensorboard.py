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
from keras.layers import Dense, Dropout
model = Sequential()


model = Sequential()
# model.add(Dense(1800, input_dim=1, activation='relu'))
model.add(Dense(5, input_shape=(1, ), activation='relu'))
model.add(Dense(4))
model.add(Dense(3))
model.add(Dense(1))


#model.summary()
#3.훈련
model.compile(loss='mse', optimizer='adam', #metrics=['accuracy']
                 metrics=['mse'])
import keras
tb_hist = keras.callbacks.TensorBoard(log_dir='graph',histogram_freq=0, write_graph=True, write_images=True)

from keras.callbacks import EarlyStopping, TensorBoard
early_stopping = EarlyStopping(monitor='loss', patience=30, mode='auto')

model.fit(x_train,y_train, epochs=10,batch_size=1,validation_data=(x_val, y_val),callbacks=[early_stopping, tb_hist])
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

# mise :  0.7006374597549438
# [[80.32429 ]
#  [81.30786 ]
#  [82.29144 ]
#  [83.275024]
#  [84.25861 ]
#  [85.242195]
#  [86.225784]
#  [87.20936 ]
#  [88.19294 ]
#  [89.17655 ]
#  [90.16012 ]
#  [91.143715]
#  [92.12728 ]
#  [93.11087 ]
#  [94.09445 ]
#  [95.07804 ]
#  [96.06164 ]
#  [97.045204]
#  [98.02882 ]
#  [99.012375]]
# RMSE :  0.8370408199566965
# R2 :  0.978928200472969
###### earlyStopping 적용하기 실습,
# loss, acc, val_loss, val_acc
#
from keras.models import Sequential
from keras.layers import Dense

import numpy as np
x_train = np.array([1,2,3,4,5,6,7,8,9,10])
y_train = np.array([1,2,3,4,5,6,7,8,9,10])
x_test = np.array([11,12,13,14,15,16,17,18,19,20])
y_test = np.array([11,12,13,14,15,16,17,18,19,20])
x_predict = np.array([21,22,23,24,25])


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

#model.summary()

model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
from keras.callbacks import EarlyStopping

early_stopping = EarlyStopping(monitor='loss', patience=100, mode='auto')
model.fit(x_train, y_train, epochs=100, callbacks=[early_stopping])
model.fit(x_train,y_train, epochs=100)

loss, acc = model.evaluate(x_test, y_test)
print("acc : ", acc)
print("loss : ", loss)

y_predict = model.predict(x_predict)
print(y_predict)
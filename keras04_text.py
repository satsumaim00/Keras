from keras.models import Sequential
from keras.layers import Dense

import numpy as np
x_train = np.array([1,2,3,4,5,6,7,8,9,10])
y_train = np.array([1,2,3,4,5,6,7,8,9,10])
x_test = np.array([11,12,13,14,15,16,17,18,19,20])
y_test = np.array([11,12,13,14,15,16,17,18,19,20])


model = Sequential()
# model.add(Dense(5, input_dim=1, activation='relu'))
# model.add(Dense(3))
# model.add(Dense(1))
model.add(Dense(1800, input_dim=1, activation='relu'))
model.add(Dense(1200))
model.add(Dense(600))
model.add(Dense(300))
model.add(Dense(150))
model.add(Dense(100))
model.add(Dense(50))
model.add(Dense(10))
model.add(Dense(5))
model.add(Dense(1))


model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])

model.fit(x_train,y_train, epochs=500)

loss, acc = model.evaluate(x_test, y_test)
print("acc : ", acc)
print("loss : ", loss)

y_predict = model.predict(x_test)
print(y_predict)

# acc :  1.0
# loss :  4.797131259692833e-05
# [[11.002517]
#  [12.003373]
#  [13.004249]
#  [14.005118]
#  [15.00599 ]
#  [16.00686 ]
#  [17.007751]
#  [18.008644]
#  [19.009539]
#  [20.01044 ]]

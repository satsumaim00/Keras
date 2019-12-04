from keras.models import Sequential
from keras.layers import Dense

import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([1,2,3,4,5,6,7,8,9,10])
X2 = np.array([11,12,13,14,15])

model = Sequential()
model.add(Dense(10, input_dim=1, activation='relu'))
model.add(Dense(5))
model.add(Dense(3))
model.add(Dense(1))



model.compile(loss='mse', optimizer='adam',
            metrics=['accuracy'])
model.fit(x,y, epochs=100, batch_size=1)

loss, acc = model.evaluate(x, y, batch_size=1)
print("acc :", acc)
print("loss:", loss)

y_predict = model.predict(X2)
print(y_predict)

[keras02.py]
from keras.models import Sequential
from keras.layers import Dense

import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([1,2,3,4,5,6,7,8,9,10])
X2 = np.array([11,12,13,14,15])

model = Sequential()
model.add(Dense(300, input_dim=1, activation='relu'))
model.add(Dense(150))
model.add(Dense(100))
model.add(Dense(50))
model.add(Dense(30))
model.add(Dense(15))
model.add(Dense(1))


model.compile(loss='mse', optimizer='adam',
            metrics=['accuracy'])
model.fit(x,y, epochs=100)

loss, acc = model.evaluate(x, y)
print("acc :", acc)
print("loss:", loss)

y_predict = model.predict(X2)
print(y_predict)

# acc :  1.0
# loss :  0.0008499999530613422
# [[10.960396]
#  [11.951141]
#  [12.941887]
#  [13.932631]
#  [14.923343]]

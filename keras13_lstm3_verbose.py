from numpy import array
from keras.models import Sequential
from keras.layers import Dense, LSTM

#1.데이터
x = array([[1,2,3], [2,3,4], [3,4,5],[4,5,6],[5,6,7],[6,7,8],[7,8,9],[8,9,10],[9,10,11],[10,11,12],
        [20,30,40],[30,40,50],[40,50,60]])
y = array([4,5,6,7,8,9,10,11,12,13,50,60,70])

print("x.shape : ", x.shape)
print("y.shape : ", y.shape)

x = x.reshape((x.shape[0], x.shape[1], 1))
print(x)
print("x.shape : ", x.shape)

#2. 모데 구성
model = Sequential()
model.add(LSTM(200, activation='relu', input_shape=(3,1))) #10 노드의 개수 column 3  몇개씩 잘라서 할건가 1
model.add(Dense(195))
model.add(Dense(185))
model.add(Dense(175))
model.add(Dense(165))
model.add(Dense(155))
model.add(Dense(145))
model.add(Dense(135))
model.add(Dense(125))
model.add(Dense(115))
model.add(Dense(105))
model.add(Dense(95))
model.add(Dense(85))
model.add(Dense(75))
model.add(Dense(65))
model.add(Dense(55))
model.add(Dense(45))
model.add(Dense(35))
model.add(Dense(25))
model.add(Dense(15))
model.add(Dense(5))
model.add(Dense(1))


#. 실행
model.compile(optimizer='adam', loss='mse')
model.fit(x,y, epochs=100, verbose=2)
# predict용 데이터
x_input = array([25,35,45]) # 1,3,????
x_input = x_input.reshape((1,3,1))

yhat = model.predict(x_input)
print(yhat)
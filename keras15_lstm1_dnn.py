import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM

#1.데이터
a = np.array(range(1,11))

size = 5
def split_x(seq, size):
    aaa = []
    for i in range(len(seq)- size + 1):
        subset = seq[i:(i+size)]
        aaa.append([item for item in subset])
    print(type(aaa))
    return np.array(aaa)

# a = 10    range seq = 10-5+1 =6   subset seq 0: 0+5(0,1,2,3,4)이지만 실직적인값은 
# 이걸로들어감 -> (1,2,3,4,5) aaa subset = [1,5] 를 5번 돌린다  이러고 다시 for 문으로
# i =0 i = 1 i=0... 이런식으로 5번

dataset = split_x(a, size)
print("========================")
print(dataset)

x_train = dataset[:,0:-1]   
y_train = dataset[:,-1]      

print(x_train.shape)  # (6,4)
print(y_train.shape)  # (6, )

model = Sequential()
model.add(Dense(333, input_shape=(4, )))
model.add(Dense(1))
# model.summary()

model.compile(loss='mse', optimizer='adam')
model.fit(x_train, y_train, epochs=10)


#모델을 마무리 해서 완성하시오 fit까지

x2 = np.array([7,8,9,10])   #(4, ) => (1, 4)
x2 = x2.reshape((1,4))

y_pred = model.predict(x2)
print(y_pred)

#y_pred를 구하시오
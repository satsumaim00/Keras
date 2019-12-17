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
from keras.models import Sequential
from keras.layers import Dense
model = Sequential()

# model.add(Dense(1800, input_dim=1, activation='relu'))
model.add(Dense(800, input_shape=(1, ), activation='relu'))
model.add(Dense(500))
model.add(Dense(300))
model.add(Dense(150))
model.add(Dense(100))
model.add(Dense(50))
model.add(Dense(10))
model.add(Dense(5))
model.add(Dense(1))

#model.summary()

model.save('./save/savetest01.h5')
print("저장됨")

# #3.훈련
# model.compile(loss='mse', optimizer='adam', #metrics=['accuracy']
#                  metrics=['mse'])

# # model.fit(x_train,y_train, epochs=100)
# model.fit(x_train,y_train, epochs=100,batch_size=1,validation_data=(x_val, y_val))
# # print("acc : ", acc)
# lose, mse = model.evaluate(x_test, y_test, batch_size=1)
# print("mise : ", mse)

# y_predict = model.predict(x_test)
# print(y_predict)

# # loss, mse = model.evaluate(x_test, y_test) # a[0], a[1]
# # print("mse : ", mse)    #1.0
# # print("loss : ", loss)  #0.0012...


# # RMSE 구하기
# from sklearn.metrics import mean_squared_error
# def RMSE (y_test, y_predict):
#     return np.sqrt(mean_squared_error(y_test, y_predict))
# print("RMSE : " ,RMSE(y_test, y_predict))

# #R2 구하기
# from sklearn.metrics import r2_score
# r2_y_predict = r2_score(y_test, y_predict)
# print("R2 : ", r2_y_predict)

# [  1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18
#   19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36
#   37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54
#   55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72
#   73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90
#   91  92  93  94  95  96  97  98  99 100]
# Using TensorFlow backend.
# 2019-12-17 18:05:12.579044: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was
# not compiled to use: AVX2
# 저장됨
#1.데이터
import numpy as np

x1 = np.array([range(100), range(311,411), range(100)])
y1 = np.array([range(501,601), range(711,811), range(100)])

x2 = np.array([range(100,200), range(311,411), range(100)])
y2 = np.array([range(501,601), range(711,811), range(100)])

x1 = np.transpose(x1)
y1 = np.transpose(y1)
x2 = np.transpose(x2)
y2 = np.transpose(y2)

print(x1.shape)
print(x2.shape)
print(y1.shape)
print(y2.shape)

from sklearn.model_selection import train_test_split
x1_train, x1_test, y1_train, y1_test = train_test_split(x1, y1, random_state=33, test_size=0.4, shuffle=False)
x1_val, x1_test, y1_val, y1_test = train_test_split(x1_test, y1_test, random_state=33, test_size=0.5, shuffle=False)

from sklearn.model_selection import train_test_split
x2_train, x2_test, y2_train, y2_test = train_test_split(x2, y2, random_state=33, test_size=0.4, shuffle=False)
x2_val, x2_test, y2_val, y2_test = train_test_split(x2_test, y2_test, random_state=33, test_size=0.5, shuffle=False)

print(x2_test.shape)
#2.모델구성
from keras.models import Sequential, Model
from keras.layers import Dense, Input
#model = Sequential()

input1 = Input(shape=(3,))
dense1 = Dense(11, activation='relu')(input1)
dense2 = Dense(3)(dense1)
dense3 = Dense(10)(dense2)
dense4 = Dense(5)(dense3)
dense5 = Dense(8)(dense4)
dense6 = Dense(9)(dense5)
dense7 = Dense(2)(dense6)
dense8 = Dense(7)(dense7)
dense9 = Dense(6)(dense8)
dense10 = Dense(4)(dense9)
middle1 = Dense(3)(dense10)

input2 = Input(shape=(3,))
xx = Dense(14, activation='relu')(input2)
xx = Dense(3)(xx)
xx = Dense(10)(xx)
xx = Dense(5)(xx)
xx = Dense(8)(xx)
xx = Dense(9)(xx)
xx = Dense(2)(xx)
xx = Dense(7)(xx)
xx = Dense(6)(xx)
xx = Dense(4)(xx)
middle2 = Dense(3)(xx)

from keras.layers.merge import concatenate
merge1 = concatenate([middle1, middle2]) #2개이상 인풋 --> 리스트

output1 = Dense(30)(merge1)
output1 = Dense(13)(merge1)
output1 = Dense(3)(output1)

output2 = Dense(15)(merge1)
output2 = Dense(32)(merge1)
output2 = Dense(3)(output2)

model = Model(inputs = [input1,input2], outputs= [output1,output2])
model.summary()

#3.훈련
#model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
model.compile(loss='mse', optimizer='adam',metrics=['mse'])
# model.fit(x,y, epochs=100, batch_size=3)
model.fit([x1_train, x2_train], [y1_train, y2_train], epochs=10, batch_size=1, 
            validation_data=([x1_val, x2_val], [y1_val, y2_val]))


##4.평가 예측
mse = model.evaluate([x1_test,x2_test], [y1_test,y2_test], batch_size=1)
print("mse : ", mse[0])
print("mse : ", mse[1])
print("mse : ", mse[2])
print("mse : ", mse[3])
print("mse : ", mse[4])


y1_predict, y2_predict = model.predict([x1_test,x2_test])
print(y1_predict, y2_predict)

# loss, mse = model.evaluate(x_test, y_test) # a[0], a[1]
# print("mse : ", mse)    #1.0
# print("loss : ", loss)  #0.0012...


# # RMSE 구하기
# from sklearn.metrics import mean_squared_error
# def RMSE (y1_test, y2_test, y1_predict, y2_predict):
#     return np.sqrt(mean_squared_error(y1_test, y2_test, y1_predict,y2_predict))
# print("RMSE : " ,RMSE(y1_test, y2_test, y1_predict,y2_predict)

# #R2 구하기
# from sklearn.metrics import r2_score
# r2_y_predict = r2_score(y1_test, y2_test, y1_predict,y2_predict)
# print("R2 : ", r2_y_predict)

#RMSE 구하기
from sklearn.metrics import mean_squared_error
def RMSE(xxx, yyy):
    return np.sqrt(mean_squared_error(xxx, yyy))
RMSE1 = RMSE(y1_test, y1_predict)
RMSE2 = RMSE(y2_test, y2_predict)
print("RMSE1 : ", RMSE1)
print("RMSE2 : ", RMSE2)
print("RMSE1 : ", (RMSE1 + RMSE2)/2)

#R2 구하기
from sklearn.metrics import r2_score
r2_y1_prodict = r2_score(y1_test, y1_predict)
r2_y2_prodict = r2_score(y2_test, y2_predict)

print("R2_1 : ", r2_y1_prodict)
print("R2_2 : ", r2_y2_prodict)
print("R2 : ", (r2_y1_prodict + r2_y2_prodict)/2)

# mse :  6778.95146484375
# mse :  3718.15625
# mse :  3060.79541015625
# mse :  3718.15625
# mse :  3060.79541015625
# [[624.56006  850.9953    29.198538]
#  [626.3303   853.17487   29.399996]
#  [628.10065  855.35443   29.601316]
#  [629.87085  857.53375   29.802753]
#  [631.6411   859.71326   30.004103]
#  [633.4116   861.8929    30.20552 ]
#  [635.1818   864.0723    30.40696 ]
#  [636.9523   866.25195   30.608395]
#  [638.7224   868.43115   30.809862]
#  [640.4927   870.6108    31.011112]
#  [642.2631   872.79034   31.212477]
#  [644.03345  874.96985   31.41388 ]
#  [645.8037   877.14935   31.615345]
#  [647.57404  879.32874   31.816698]
#  [649.3444   881.5084    32.018127]
#  [651.1147   883.6878    32.219555]
#  [652.8851   885.8674    32.42097 ]
#  [654.6552   888.0468    32.622314]
#  [656.4256   890.2264    32.8237  ]
#  [658.19604  892.406     33.02518 ]] [[604.6735   855.20013   36.780746]
#  [606.25037  857.40186   37.028812]
#  [607.8276   859.6037    37.27694 ]
#  [609.40466  861.8056    37.524952]
#  [610.9821   864.0073    37.773018]
#  [612.5592   866.2092    38.021175]
#  [614.1366   868.411     38.269207]
#  [615.71356  870.6127    38.517155]
#  [617.2907   872.81445   38.765327]
#  [618.868    875.0164    39.01326 ]
#  [620.4452   877.21826   39.26133 ]
#  [622.02246  879.42      39.50944 ]
#  [623.5997   881.6218    39.757572]
#  [625.17676  883.82367   40.00558 ]
#  [626.75397  886.02545   40.253624]
#  [628.3314   888.22705   40.501736]
#  [629.90845  890.42883   40.749695]
#  [631.4856   892.6307    40.997826]
#  [633.0628   894.8325    41.245777]
#  [634.64026  897.03455   41.493935]]
# RMSE1 :  60.97666649997051
# RMSE2 :  55.32442978681192
# RMSE1 :  58.15054814339122
# R2_1 :  -110.82417616386846
# R2_2 :  -91.05391071386111
# R2 :  -100.93904343886479
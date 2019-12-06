#1.데이터
import numpy as np

x1 = np.array([range(100), range(311,411), range(100)])
x2 = np.array([range(501,601), range(711,811), range(100)])

y1 = np.array([range(100,200), range(311,411), range(100)])
y2 = np.array([range(501,601), range(711,811), range(100)])
y3 = np.array([range(401,501), range(211,311), range(100)])

x1 = np.transpose(x1)
y1 = np.transpose(y1)
x2 = np.transpose(x2)
y2 = np.transpose(y2)
y3 = np.transpose(y3)

print(x1.shape) # (100, 3)
print(x2.shape)
print(y1.shape)
print(y2.shape)
print(y3.shape)

from sklearn.model_selection import train_test_split
x1_train, x1_test, y1_train, y1_test = train_test_split(x1, y1, random_state=33, test_size=0.4, shuffle=False)
x1_val, x1_test, y1_val, y1_test = train_test_split(x1_test, y1_test, random_state=33, test_size=0.5, shuffle=False)

from sklearn.model_selection import train_test_split
x2_train, x2_test, y2_train, y2_test = train_test_split(x2, y2, random_state=33, test_size=0.4, shuffle=False)
x2_val, x2_test, y2_val, y2_test = train_test_split(x2_test, y2_test, random_state=33, test_size=0.5, shuffle=False)

from sklearn.model_selection import train_test_split
y3_train, y3_test = train_test_split(y3, random_state=66, test_size=0.4, shuffle=False)
y3_val, y3_test = train_test_split(y3_test, random_state=66, test_size=0.5, shuffle=False)

print(y3_test.shape)

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
output1 = Dense(13)(output1)
output1 = Dense(3)(output1)

output2 = Dense(15)(merge1)
output2 = Dense(32)(output2)
output2 = Dense(3)(output2)

output3 = Dense(15)(merge1)
output3 = Dense(32)(output3)
output3 = Dense(3)(output3)


model = Model(inputs = [input1,input2], outputs= [output1,output2,output3])
model.summary()

#3.훈련
#model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
model.compile(loss='mse', optimizer='adam',metrics=['mse'])
# model.fit(x,y, epochs=100, batch_size=3)
model.fit([x1_train, x2_train], [y1_train, y2_train, y3_train], epochs=100, batch_size=1, 
            validation_data=([x1_val, x2_val], [y1_val, y2_val, y3_val]))


##4.평가 예측
mse = model.evaluate([x1_test,x2_test], [y1_test,y2_test,y3_test], batch_size=1)
print("mse : ", mse[0])
print("mse : ", mse[1])
print("mse : ", mse[2])
print("mse : ", mse[3])
print("mse : ", mse[4])


y1_predict, y2_predict, y3_predict = model.predict([x1_test,x2_test])
print(y1_predict, y2_predict, y3_predict)

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
RMSE3 = RMSE(y3_test, y3_predict)

print("RMSE1 : ", RMSE1)
print("RMSE2 : ", RMSE2)
print("RMSE3 : ", RMSE3)
print("RMSE : ", (RMSE1 + RMSE2 + RMSE3)/3)

#R2 구하기
from sklearn.metrics import r2_score
r2_y1_prodict = r2_score(y1_test, y1_predict)
r2_y2_prodict = r2_score(y2_test, y2_predict)
r2_y3_prodict = r2_score(y3_test, y3_predict)

print("R2_1 : ", r2_y1_prodict)
print("R2_2 : ", r2_y2_prodict)
print("R2_3 : ", r2_y3_prodict)
print("R2 : ", (r2_y1_prodict + r2_y2_prodict + r2_y3_prodict)/3)


# mse :  6.475951664697277e-07
# mse :  1.7176208189084718e-07
# mse :  2.297136205697825e-07
# mse :  2.4611944127173047e-07
# mse :  1.7176208189084718e-07
# [[180.00053  391.0003    80.000336]
#  [181.00056  392.00037   81.000305]
#  [182.00052  393.00037   82.00029 ]
#  [183.0005   394.00034   83.000305]
#  [184.00053  395.0004    84.00027 ]
#  [185.0005   396.0003    85.00031 ]
#  [186.00053  397.0003    86.00039 ]
#  [187.00046  398.00034   87.000275]
#  [188.00052  399.00037   88.00022 ]
#  [189.00053  400.00034   89.000206]
#  [190.00052  401.00027   90.00022 ]
#  [191.0005   402.0003    91.00034 ]
#  [192.00047  403.00027   92.00022 ]
#  [193.00056  404.0004    93.00023 ]
#  [194.00066  405.0004    94.000336]
#  [195.00058  406.00037   95.00021 ]
#  [196.00053  407.00034   96.00027 ]
#  [197.00053  408.00043   97.00026 ]
#  [198.00064  409.0004    98.00037 ]
#  [199.00066  410.0005    99.00028 ]] [[581.00024  791.0007    80.0003  ]
#  [582.00037  792.0007    81.000275]
#  [583.0003   793.0005    82.00022 ]
#  [584.00037  794.0006    83.000206]
#  [585.00037  795.0006    84.00026 ]
#  [586.0002   796.0008    85.00021 ]
#  [587.00037  797.0005    86.000244]
#  [588.00024  798.0005    87.00025 ]
#  [589.0004   799.0006    88.00026 ]
#  [590.00024  800.0005    89.000206]
#  [591.0002   801.00055   90.00021 ]
#  [592.0001   802.00055   91.00029 ]
#  [593.0001   803.0005    92.000206]
#  [594.0004   804.00055   93.00026 ]
#  [595.0004   805.0008    94.00028 ]
#  [596.0003   806.0008    95.00017 ]
#  [597.00024  807.00073   96.00024 ]
#  [598.0004   808.0008    97.0003  ]
#  [599.0004   809.0007    98.000305]
#  [600.0005   810.0008    99.0003  ]] [[480.99985  291.00046   80.00068 ]
#  [481.9999   292.00046   81.00065 ]
#  [482.9999   293.00052   82.00068 ]
#  [483.99994  294.00043   83.00068 ]
#  [484.99988  295.0005    84.000725]
#  [485.99988  296.0005    85.00064 ]
#  [486.99985  297.00043   86.00063 ]
#  [487.99976  298.00043   87.00068 ]
#  [489.       299.00046   88.00062 ]
#  [489.99982  300.0005    89.000694]
#  [490.9998   301.00046   90.00062 ]
#  [491.9998   302.0005    91.00067 ]
#  [492.99976  303.0004    92.00062 ]
#  [493.99988  304.00052   93.00063 ]
#  [494.99982  305.00055   94.000755]
#  [495.99988  306.00052   95.000694]
#  [496.99985  307.0005    96.00071 ]
#  [497.9998   308.00052   97.00065 ]
#  [498.9999   309.0005    98.0007  ]
#  [499.99994  310.0006    99.00071 ]]
# RMSE1 :  0.00041167400362457666
# RMSE2 :  0.00044224830291968544
# RMSE3 :  0.0004875744233650263
# RMSE :  0.00044716557663642943
# R2_1 :  0.9999999949029929
# R2_2 :  0.9999999941177876
# R2_3 :  0.9999999928502611
# R2 :  0.9999999939570139
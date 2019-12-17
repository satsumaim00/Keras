from keras.models import Sequential

filter_size = 32
kernel_size = (3,3)

from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
model = Sequential()
model.add(Conv2D(7, (2,2), #padding='same',    2개씩 잘린다
                input_shape =(28, 28, 1)))     # 1 = feature(특징) 28 가로 28 세로
# model.add(Conv2D(16,(2,2)))
# model.add(MaxPooling2D(3,3))
# model.add(Conv2D(8,(2,2)))
model.add(Flatten())                    #flatten 쭈욱 피는거 
model.add(Dense(10))
model.add(Dense(10))

model.summary()

# ________________________________________________________________
# Layer (type)                 Output
# Shape              Param #
# =================================================================
# conv2d_1 (Conv2D)            (None,
# 27, 27, 7)         35
# _________________________________________________________________
# flatten_1 (Flatten)          (None,
# 5103)              0
# _________________________________________________________________
# dense_1 (Dense)              (None,
# 10)                51040
# _________________________________________________________________
# dense_2 (Dense)              (None,
# 10)                110
# =================================================================
# Total params: 51,185
# Trainable params: 51,185
# Non-trainable params: 0
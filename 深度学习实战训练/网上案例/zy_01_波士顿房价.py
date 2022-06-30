# 一维卷积神经网络实现波士顿房价预测，数据集为boston房价与周边环境等因素，参照网上的例子
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 加载boston房价数据集
boston = tf.contrib.learn.datasets.load_dataset('boston')
X_train, Y_train = boston.data, boston.target
# ==============================对数据集的格式进行解析=======================================
# boston数据集的X为506行，13列，分别为影响房价的诸多因素，Y为506行，1列，即房价
print('数据加载成功！')
print('boston.type is', type(boston))
print('X_train.type =', type(X_train))
print('X_train.ndim =', X_train.ndim)
print('X_train.shape =', X_train.shape)
print('X_train.dtype =', X_train.dtype)
print('X_train 的行数 m = {0}, 列数 n = {1}'.format(X_train.shape[0], X_train.shape[1]))
print('Y_train.type =', type(Y_train))
print('Y_train.ndim =', Y_train.ndim)
print('Y_train.shape =', Y_train.shape)
print('Y_train 的行数 m = {0}, 列数 n = None'.format(Y_train.shape[0]))
print('Y_train.dtype =', Y_train.dtype)


# ==========================================================================================
# 定义归一化函数
def normalize(X):
    mean = np.mean(X)  # 均值
    std = np.std(X)  # 默认计算每一列的标准差
    X = (X - mean) / std
    return X


X_train = normalize(X_train)  # 对输入变量按列进行归一化
# ==============================网络参数=====================================================
# parameters超参数
learning_rate = 0.001
training_iters = 500  # 训练次数
batch_size = 10  # 批训练样本大小
display_step = 10  # 打印训练结果的Iter的步长
# Network Parameters
n_input = 13  # X_train的列数
# ==========================================================================================
# 为训练数据申明占位符
x = tf.placeholder(tf.float32, [None, n_input])
y = tf.placeholder(tf.float32)


# keep_prob = tf.placeholder(tf.float32) #keep_prob用于激活某些神经元，防止过拟合
# 定义一个输入为x，权值为w，偏置为b，给定步幅的卷积层，激活函数是ReLu，padding设为SAMEM模式
def conv2d(x, w, b, strides=1):
    x = tf.nn.conv2d(x, w, strides=[1, strides, strides, 1],
                     padding='SAME')
    x = tf.nn.bias_add(x, b)
    return tf.nn.relu(x)


# 定义一个输入是x的maxpool层，卷积核为ksize并且padding为SAME
def maxpool2d(x, k=2):
    return tf.nn.max_pool(x, ksize=[1, k, k, 1], strides=[1, k, k, 1],
                          padding='SAME')


# 定义卷积神经网络，其构成是两个卷积层，一个droup层，最后是输出层
def conv_net(x, weights, biases):
    # reshape the input picture
    x = tf.reshape(x, shape=[-1, 13, 1, 1])  # 将输入数据变为4-D张量
    # First convolution layer
    conv1 = conv2d(x, weights['wc1'], biases['bc1'])
    fc1 = tf.reshape(conv1, [-1,
                             weights['wd1'].get_shape().as_list()[0]])
    # Fully connected layer
    fc1 = tf.add(tf.matmul(fc1, weights['wd1']), biases['bd1'])
    fc1 = tf.nn.relu(fc1)
    # Fully connected layer
    fc2 = tf.add(tf.matmul(fc1, weights['wd2']), biases['bd2'])
    fc2 = tf.nn.relu(fc2)
    # output the class prediction
    out = tf.add(tf.matmul(fc1, weights['out']), biases['out'])
    return out


# 定义网络层的权重和偏置，第一个conv层有一个5*5的卷积核，一个输入和32个输出。第二个
# conv层有1个5*5的卷积核，32个输入和64个输出。全连接层有1024个输入和10个输出对应于最后
# 的数字数目。所有的权重和偏置用randon_normal分布完成初始化：
weights = {
    # 5*5 conv ,1 input, and 32 outputs
    'wc1': tf.Variable(tf.random_normal([5, 5, 1, 32])),
    # fully connected, 13*32 inputs, and 128 outputs
    'wd1': tf.Variable(tf.random_normal([13 * 32, 128])),
    'wd2': tf.Variable(tf.random_normal([128, 128])),
    # 128 inputs, 10 outputs for class digits
    'out': tf.Variable(tf.random_normal([128, 1]))
}
biases = {
    'bc1': tf.Variable(tf.random_normal([32])),
    'bd1': tf.Variable(tf.random_normal([128])),
    'bd2': tf.Variable(tf.random_normal([128])),
    'out': tf.Variable(tf.random_normal([1]))
}
# 建立一个给定权重和偏置的convnet。定义均方根误差的损失函数，并用Adam优化器进行损失最小化。
# 优化后，计算精度：
pred = conv_net(x, weights, biases)
cost = tf.reduce_mean(tf.square(y - pred))  # 损失函数，均方误差
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)
init_op = tf.global_variables_initializer()
# 启动计算图，并迭代train_iterats次，其中每次输入batch_size个数据进行优化，请注意，用从mnist数据集分离出的
# mnist.train数据进行训练，每进行display_step次迭代，会计算当前的精度，最后，在2048个测试图片上计算精度，
# 此时无dropout
total = []  # 定义一个空列表，用于存储每一次Epoch的误差
with tf.Session() as sess:
    sess.run(init_op)  # 初始化变量
    for i in range(training_iters):
        _, l = sess.run([optimizer, cost], feed_dict={x: X_train, y: Y_train})
        # acc = sess.run([pred],feed_dict={x:X_train,y:Y_train})
        total.append(l)
        print('Epoch {0}: Loss {1}'.format(i, l))

# 绘制损失函数
plt.figure(num=1)
plt.title('loss curve')
plt.xlabel('Epoch', color='red')
plt.ylabel('loss', color='blue')
plt.plot(total)
plt.show()
import numpy as np
import pandas as pd
import mxnet as mx
import logging

logging.basicConfig(level=logging.DEBUG)


train1=pd.read_csv('train.csv')
train1.shape
train1.iloc[0:4, 0:15]
train=np.asarray(train1.iloc[0:33600,:])
cv=np.asarray(train1.iloc[33600:,:])
trainx=train[:,1:]
trainx.shape
cvx=cv[:,1:]
cvx.shape
trainx=np.reshape(trainx, (trainx.shape[0],1,28,28))/255
cvx=np.reshape(cvx, (cvx.shape[0],1,28,28))/255
trainy=np.asarray(train[:,0])
cvy=np.asarray(cv[:,0])
trainy.shape

# CONVOLUTIONAL NEURAL NETWORK
data = mx.sym.var('data')
Y= mx.symbol.Variable('softmax_label') 

# first conv layer
conv1 = mx.sym.Convolution(data=data, kernel=(5,5), num_filter=20)
nlin1 = mx.sym.Activation(data=conv1, act_type="relu")
pool1 = mx.sym.Pooling(data=nlin1, pool_type="max", kernel=(2,2), stride=(2,2))
drop1 = mx.symbol.Dropout(data=pool1,p=0.5)
# second conv layer
conv2 = mx.sym.Convolution(data=drop1, kernel=(5,5), num_filter=40)
nlin2 = mx.sym.Activation(data=conv2, act_type="relu")
pool2 = mx.sym.Pooling(data=nlin2, pool_type="max", kernel=(2,2), stride=(2,2))
drop2 = mx.symbol.Dropout(data=pool2,p=0.5)
# first fullc layer
flatten = mx.sym.flatten(data=drop2)
fc1 = mx.symbol.FullyConnected(data=flatten, num_hidden=500)
nlin3 = mx.sym.Activation(data=fc1, act_type="relu")

# output fullc
fc2 = mx.sym.FullyConnected(data=nlin3, num_hidden=10)
# Softmax output
CNN = mx.symbol.SoftmaxOutput(data=fc2, label=Y,name="CCN")
CNN_model = mx.mod.Module(symbol=CNN, label_names =['softmax_label'], context=mx.cpu())
batch_size = 100
train_iter = mx.io.NDArrayIter(trainx, trainy, batch_size, shuffle=True)
val_iter = mx.io.NDArrayIter(cvx, cvy, batch_size)

CNN_model.fit(train_iter,  # train data
              eval_data=val_iter,  # validation data
                optimizer='sgd',
                optimizer_params={'learning_rate':0.05, 'momentum': 0.9},
                eval_metric='acc', 
                batch_end_callback = mx.callback.Speedometer(batch_size=batch_size, frequent=200),              
                num_epoch=20)

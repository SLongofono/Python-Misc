import numpy as np
from tensorflow.contrib.keras import layers, models, optimizers, backend

target = "Hello, World"
target = np.array([ord(x) for x in target])

def buildNetwork():
    inp = layers.Input(shape[12], name="input")
    myNN = layers.Dense(64, activation="relu")(inp)
    myNN = layers.Dropout(0.1)(myNN)
    myNN = layers.Dense(128, activation="relu")(myNN)
    outp = layers.Dense(12, activation="linear")(myNN)
    model = models.Model(inputs=[inp], outputs=outp)
    model.compile(optimizers.SGD(0.001), loss="mse")
    return model
  
def train(model):
    inputVecs = np.random.rand(2048,12)
    targets = np.tile(target, (2048,1))
    result = ""
    while result != target:
        model.fit(x=inputVecs, y=targets, epochs=1, batch_size=512)
        result = model.predict(np.random.rand(1,12))
        result = "".join([chr(x) for x in result[0]])
        print(result)
    
myModel = buildNetwork()
train(myModel)  

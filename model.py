import tensorflow as tf

class FullyConnected:
    def build():

        model = tf.keras.models.Sequential()
        
        model.add(tf.keras.layers.Dense(20, input_shape=(9,), activation='relu'))
        model.add(tf.keras.layers.Dense(5, activation='relu'))
        model.add(tf.keras.layers.Dense(1, activation='linear'))
        return model
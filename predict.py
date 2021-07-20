import os
import tensorflow as tf
import json
import numpy as np

# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # or any {'0', '1', '2'}
tf.get_logger().setLevel('ERROR')

with open('api/ml/model-mnist.json', 'r') as json_file:
    model_json = json_file.read()

model = tf.keras.models.model_from_json(model_json)
model.load_weights('api/ml/model-mnist.h5')

with open('data-mnist.json', 'r') as f:
    data = json.load(f)
    X = np.array(data['data'])

pred = model.predict(X)
print(np.argmax(pred, axis=1))

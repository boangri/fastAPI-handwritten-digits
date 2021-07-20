import tensorflow as tf
import numpy as np


class Model:
    def __init__(self, model_path: str = None):
        with open(model_path + 'json', 'r') as json_file:
            model_json = json_file.read()

        self._model = tf.keras.models.model_from_json(model_json)
        self._model.load_weights(model_path + 'h5')
        self._model_path = model_path

    def train(self, X: np.ndarray, y: np.ndarray):
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        return self._model.predict(X)

    def save(self):
        pass

    def load(self):
        return self


def get_model():
    return model


n_features = 28

if __name__ == "__main__":
    model_path = 'api/ml/model-mnist.'

    model = Model(model_path)

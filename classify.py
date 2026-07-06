from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

def load_marubozu_model(path):
    return load_model(path)

def preprocess(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    arr = image.img_to_array(img) / 255.0
    arr = np.expand_dims(arr, axis=0)
    return arr

def predict(model, img_path, threshold=0.85):
    x = preprocess(img_path)
    prob = float(model.predict(x)[0][0])
    is_marubozu = prob > threshold
    return prob, is_marubozu


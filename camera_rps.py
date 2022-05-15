from configparser import Interpolation
from ctypes import resize
from xml.etree.ElementPath import prepare_predicate
from xmlrpc.server import list_public_methods

import cv2
from keras.models import load_model
import numpy as np

def get_prediction():

    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    labels = ['Rock','Paper','Scissors','Nothing']
    output = []

    while True:
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        output = prediction
        break
    cap.release()
    # Destroy the camera window
    cv2.destroyAllWindows()
    
    cv_pred_arr = output[0].tolist()
    index = cv_pred_arr.index(max(cv_pred_arr))

    return labels[index]

from configparser import Interpolation
from ctypes import resize
from xml.etree.ElementPath import prepare_predicate
from xmlrpc.server import list_public_methods

import cv2, time
from keras.models import load_model
import numpy as np

def get_prediction(array):
    #RPS options in a list - for easy indexing
    labels = ['Rock','Paper','Scissors','Nothing']
    #conversion from array to list
    out = array[0].tolist()
    prob = max(out)
    index = out.index(prob)
    #results - fetching the item at a particular index of the RPS list
    return labels[index]

#Outputting through a function that will pick output of the camera and predict r,p or s.
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
start = time.time()

while True:
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 #Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    end = time.time()
    e_time = round(4  - (end - start))
    #Script will end after 3 seconds of running
    if e_time <= 0:
        user_prediction = get_prediction(prediction)
        print(f"You played: {user_prediction}")
        break
    print(f"Countdown: {e_time}")

#After the loop release the cap object
cap.release()
#Destrop all the windows
cv2.destroyAllWindows()
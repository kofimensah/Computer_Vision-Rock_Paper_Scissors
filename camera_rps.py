from configparser import Interpolation
from ctypes import resize
from encodings import normalize_encoding
from xml.etree.ElementPath import prepare_predicate
from xmlrpc.server import list_public_methods

import cv2, time, random
from keras.models import load_model
import numpy as np


#Function to obtain computer choice
def get_computer_choice():
    rps_options = ['Rock', 'Paper', 'Scissors']
    cp_choice = random.choice(rps_options)
    return cp_choice


#Function to convert openCV output into user prediction
def get_prediction(array):
    #RPS options in a list - for easy indexing
    labels = ['Rock','Paper','Scissors','Nothing']
    #conversion from array to list
    out = array[0].tolist()
    prob = max(out)
    index = out.index(prob)
    #results - fetching the item at a particular index of the RPS list
    return labels[index]

def camera_write (frame, text, org):
    # font
    font = cv2.FONT_HERSHEY_SIMPLEX
    # FontScale 
    fontScale = 1.5
    # Blue color in BGR
    color = (255, 0,0)
    #line thickness
    thickness = 2

    return cv2.putText(frame, text, org, font, fontScale,color, thickness, cv2.LINE_AA, False)


#Function to obtain user choice from webcam using openCV
def get_user_choice():

    #Initializing CV2 object and frame
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    start = time.time()
    new_time = 0

    while True:
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 #Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        end = time.time()
        e_time = round(4  - (end - start))
        text = camera_write(frame,f"Countdown: {e_time}",(0,100))
        cv2.imshow('RPS Game', text)
        
        #Script will end after 3 seconds of running
        if cv2.waitKey(1) and e_time <= 0:
            user_choice = get_prediction(prediction)
            print(f"You played: {user_choice}")
            break
        if e_time != new_time:
            new_time = e_time
        else:
            continue

    #After the loop release the cap object
    cap.release()
    #Destrop all the windows
    cv2.destroyAllWindows()

    return user_choice 

#Function to determine winner
def get_winner(computer_choice, user_choice):
    user = "User Wins Round"
    comp = "Computer Wins Round"
    print(f"Computer = {computer_choice}, User = {user_choice}")
    if computer_choice == "Rock" and user_choice == "Paper":
        print(user)
        return "User Wins"
    elif computer_choice == "Rock" and user_choice == "Scissors":
        print(comp)
        return "Computer Wins"
    elif computer_choice == "Paper" and user_choice == "Rock":
        print(comp)
        return "Computer Wins"
    elif computer_choice == "Paper" and user_choice == "Scissors":
        print(user)
        return "User Wins"
    elif computer_choice == "Scissors" and user_choice == "Rock":
        print(user)
        return "User Wins"
    elif computer_choice == "Scissors" and user_choice == "Paper":
        print(comp)
        return "Computer Wins"
    else:
        print("Try Again")
        return


#Play function to run entire game
def play():
    comp_choice = get_computer_choice()
    user_choice = get_user_choice()
    return get_winner(comp_choice, user_choice)

#Function to play a number of rounds to determine the winner
def rounds():
    computer_wins = 0
    user_wins = 0
    no_rounds = 1
    #Checking the number of wins per computer or user
    while computer_wins < 3 and user_wins < 3:
        print(f"------------------------------ROUND: {no_rounds}---------------------------")
        result = play()
        #debugging infinite loop part 1
        print(f"The result is {result}")
        no_rounds += 1
        if result == "Computer Wins":
            computer_wins += 1
            print(f"Computer Score: {computer_wins}") #checking commulation
        elif result == "User Wins":
            user_wins += 1
            print(f"User Score: {user_wins}") #checking commulation
    else:
        if computer_wins == 3:
            print("Computer Won")
        else:
            print("User Won")

rounds()


"""
Method 1: Initializes cv object and frame in script. This prevents CV object from reopening every round.
Downside is that we lose the few seconds of pause before the next round.

Method 2: The cv object and frame are initalized within the get_user_choice function. This causes the frame to restart in a split second for every round.
"""

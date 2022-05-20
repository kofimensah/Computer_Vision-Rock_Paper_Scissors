# Computer_Vision-Rock_Paper_Scissors
This Computer vision project uses OpenCV, Tensorflow and the time module to replicate the Rock Paper Scissors game where the computer randomly picks between Rock, Paper and Scissors to play against the user who will be playing by indicating a rock object, paper object or scissor object to the webcamera.

Milestone One
Using the teachable machine web tool, a model is trianed using ~200 images showing hand gestures of a rock, a paper and scissors. The model is exported in tensor flow format and saved in †he project folder.

Milestone Two
Using the conda instalation tool in terminal, a virtual environment is created within which the necessary dependencies and required modules (mainly pip, tensorflow, opencv and ipykernel) are installed without affecting the main desktop environment. The downloaded tensor flow model from milestone one is then run in the virtual enviroment and integrated with opencv to read user hand gestures and out an array of values, indicating the probability of the hand gesture being a rock, paper, scissor or nothing, respectively.

Milestone Three
To begin the actual game creation, a manual rock, paper, scissors game is initially created where the user choice is obtained through the input function in python. Two main functions are created within this script, get_user_choice and get_computer_choice to respectively obtain the users choice and the computers prediction. Using functions and if conditions, I cre various scenarios for the game choice pairing. A final fucntion called play, is then created to play the game, taking in user_choice and computer_choice as arguments.

Milestone Four
A separate script is created using the manual rps script as a foundation, to integrate the opencv and tensor flow model with the manual rps functions created. The get_user_choice is updated to use opencv to capture hand gestures and return either rock, paper or scissors. Another function is then created to introduce a countdown and a number of rounds. To finally win the game, either the user or the computer has to win 3 times to win. For each round, the user will have 3 seconds to finalize their hand gesture. This all comes together to create a beautiful Rock Paper Scissors game.

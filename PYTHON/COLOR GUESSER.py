
import random

color = random.randint(1,7)
if color == 1:

    color = "yellow"
    
if color == 2:
    color = "green"
    
if color == 3:
    color = "orange"
    
if color == 4:
   color = "blue"
  
if color == 5:
    color = "red"
    
if color == 6:
    color = "purple"

    

    
user_choice = input("Choose a color from the rainbow...so think about those 6 colors, ONLY!!")


if user_choice == color:
    print("good job! you guessed correctly")
else:
    print("THE COMPUTER THOUGHT OF SOMETHING DIFFERENT, SORRY....") 
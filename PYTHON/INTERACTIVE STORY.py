import random
descicions = ["A" , "B"]
print("youre inside a jail cell and you need to escape...")
ud1 = input('Make a Descision...type "2" to go somewhere or type "1" to go somwewhenre else')
ud2 = input('scenario #1: you see a screwdriver or a hammer...type "1" for the screwdriver and "2" for the hammer')  
if ud2 == "2":
    print(" you chose the hammer....that was too loud and the guards caught you ")
    ud3 = input("DO you want to kill the guard with the hammer?... or run. Press 1 to kill the guard and press 2 to run")
    if ud3 == "1":
        print("GOOD JOB! you killed the guard!")
elif ud2 == "1":
    print("you chose the screwdriver... good job you unscrewed the vent and crawled thru")
    print("okay...you have the biggest descision of your life.... you are underground right now....")
    print(" you can go thru the sewage pipe full of poop and gross stuff or...You can go thru the chlostophobic vent blowing cold air at your face")
    ud4 = input(" Press 1 to go thru the pipe or Press 2 to go through the vent")
    
    if ud4 == "1":
        print("Godd job you escaped....my advice to you is to get a new identity")
    if ud4 == "2":
        print("uhh ohh you didnt escape the vent broke....looks like you arent getting out anytime soon")
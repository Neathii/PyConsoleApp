print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower().strip() != "yes":
    quit()

print("Okay! Let's play :) ")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower().strip() == "central processing unit":
    print('Correct!')
    score +=1
    print('Hurray!  You received a point! :)')
else:
    print("Incorrect!")
    print('Oops!  You lost a point! :(')
    

answer = input("What does GPU stand for? ")
if answer.lower().strip() == "graphics processing unit":
    print('Correct!')
    score +=1
    print('Hurray!  You received a point! :)')
else:
    print("Incorrect!")
    print('Oops!  You lost a point! :(')
    
answer = input("What does RAM stand for? ")
if answer.lower().strip() == "random access memory":
    print('Correct!')
    score +=1
    print('Hurray!  You received a point! :)')
else:
    print("Incorrect!")
    print('Oops!  You lost a point! :(')

answer = input("What does PSU stand for? ")
if answer.lower().strip() == "power supply unit":
    print('Correct!')
    score +=1
    print('Hurray!  You received a point! :)')
else:
    print("Incorrect!")
    print('Oops!  You lost a point :(')

print("Your score is: ", score)

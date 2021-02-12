# Introduction
print('Welcome to Survival!!')

name = input("What is your name? ")

print("Let's get started", name + "!")
print("Your health is at 100!")


# Storyline
def story(health):

  decision_1 = input("Which direction would you like to go? (left/right) ")

  if decision_1 == "left" or decision_1 == "Left":
    if health == 50:
      print('Really? You just did that... I literally told you how much health you had...')
      print('You can do the math... you know what this means. Game over... ')
    else:
      print("Welp, you tripped on a rock and lost 50 health...")
      health = health - 50
      print("You have:", health, "health")

      path1_2 = input("You found a river! Would you like to swim across or go back? (across/back)")

      if path1_2 == 'across':
        print("You got caught by the tide and drowned :(")
      elif path1_2 == 'back':
        story(health)

  elif decision_1 == "right" or decision_1 == "Right":
    path2_2 = input("You have run into a bear! Would you like to fight or run? (fight/run)")
    path2_5 = '' # temporarily empty
    if path2_2 == "fight":
      print("YOU HIT THE BEAR WITH A RIGHT HOOK AND HE IS STUNNED")
      path2_3 = input("Would you like to keep fighting? (yes/no)")
      if path2_3 == "yes":
        print('THE BEAR PUTS HIS FISTS UP AND IS READY TO FIGHT')
        print('YOU TRY TO PUNCH HIM AGAIN BUT HE DODGES AND HITS YOU WITH A LEFT HOOK')
        health = health - 50
        print('YOU JUST TOOK 50 DAMAGE AND YOU NOW HAVE:', health, 'health')
        
        if health == 0:
          print('You died.. Game Over')
          return
        else:
          path2_4 = input('Would you like to kick the bear in the shin or step on his toes? (shin/toes)')

        if path2_4 == "shin":
          print('YOU KICKED HIM IN THE SHIN BUT HE KICKED YOU BACK AND LOST 20 HEALTH')
          health = health - 20
          print('You now have:', health, 'health')

          path2_5 = input("would you like to try to run or kick him again? (run/kick)")
          if path2_5 == 'kick':
            print("oh.. good job.. you've pissed him off even more.. well.. good luck.")
            print("theres no hope for you anymore...")
            print("the bear has now put you in a head lock... its game over for you")
            print("yup.. the bear just killed you... good job... you're dead")
        
        elif path2_4 == "toes":
          print('THE BEAR IS ANGUISHED AND YOU RUN AWAY')
          print('CONGRATULATIONS YOU WON!')
           
      if path2_2 == "run" or path2_5 == "run":
        print("THE BEAR CHASED YOU annndd now you're dead...")
      if path2_3 == "no":
        print('ohhh boy the bear is chasing you!!')
        print('HE JUST THREW A ROCK AT YOU')
        print('You tumbled and died... Game Over.')

  else:
    print("Unfortunately that is not a path! Try again.")
    return story(health)


health = 100
story(health)
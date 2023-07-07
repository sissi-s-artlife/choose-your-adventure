print("Welcome to the Apocalypse in 2200.Your mission is to survive the apocalypse.Choose wisely!")
time_machine=input("There is a time machine it can only send you to the future or past to an unknown time period.\nType 'future' to go the future or 'past' to go to the past.").lower()
if time_machine=="future":
  planet_choice=input("You did it!You are in another planet.You can either go for a space travel or stay in the planet and work as a miner.\nType 'travel' to go for a space travel or 'stay' to work as miner in the planet.").lower()
  if planet_choice=="travel":
    last_3=input("You chose wisely and reached to another planet.There are last 3 options.\nType 'marry' to marry the prime minister.\n'hunt' to hunt criminal men for feminist revolution\n'monastery' to live in the monastery as a monk.").lower()
    if last_3=="marry":
      print("Prime minister died of a deadly contagious disease and you died along with him.")
    elif last_3=="hunt":
      print("Revolution has been succesful.You are the leader of the next hunt.Good luck :)")
    elif last_3=="monastery":
      print("The monastery was attacked by anti-religious groups.You died during the attack :(")
    else:
      print("You made a choice that does not exist in the boundaries of this universe.")
  elif planet_choice=="stay":
    print("Miners made a revolution in which you died with honour.")
  else:
    print("You made a choice that does not exist in the boundaries of this universe.")
elif time_machine=="past":
  print("The past is dark and full of terrors!\nYou chose poorly and dommed to repeat the mistakes of yesterday.")
else:
  print("You made a choice that does not exist in the boundaries of this universe.")

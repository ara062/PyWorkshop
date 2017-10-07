print()
print("What is your name?")

name = input(">")

print("Hello %s, welcome to the dungeon!" % (name))
print("Do you go through door 1 od door 2?")

def wrong_input():
	print("You are not so good with nnumbers, are you?")

def dead(death_message):
	print("You are dead.", death_message)

door = input(">")

if door == "1":
	print("There is a nice vampire asking you if you enjoy life.")
	print("What do you do?")
	print("1. Smile and nod")
	print("2. Scream and run")

	vampire = input("> ")

	if vampire =="1":
		print("Congratulations %s, you found a new friend!"% (name))
	elif vampire =="2":
		dead("Sorry %s, the vampire is faster. You become a dinner."% (name)) 
	else:
		wrong_inpput()

elif door == "2":
	print("There is a new room with 3 doors")
	print("What do you do?")
	print("1. You take a door 1")
	print("2. You take a door 2")
	print("3. You take a door 3")

	island = input(">")

	if island =="1":
		print("Congratulations, you found a island with a hotel.")
	elif island =="2":
		print("Ouch, you found a desert island.") 
	elif island =="3":
		dead("Es tut mir leid, du bist tot.")
	else:
		wrong_input()

else:
	wrong_input()
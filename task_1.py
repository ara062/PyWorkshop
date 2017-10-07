print()
print("Welcome to the dungeo!")
print("Do you go through door 1 or door 2?")

door = input(">")

if door == "1":
	print("There is a nice vampire asking you if you enjoy life.")
	print("What do you do?")
	print("1. Smile and nod")
	print("2. Scream and run")

	vampire = input("> ")

	if vampire =="1":
		print("Congratulations, you found a new friend!")
	elif vampire =="2":
		print("Sorry, the vampire is faster. You become a dinner.")
	else:
		print("You are not so good with numbers, are you?")

elif door == "2":
	print("There is a new room with 2 doors")
	print("What do you do?")
	print("1. You take a door 1")
	print("2. You take a door 2")

	island = input(">")

	if island =="1":
		print("Congratulations, you found a island with a hotel")
	elif island =="2":
		print("Ouch, you found a desert island")
	else:
		print("You are not so good with numbers, are you?")

else:
	print("You are not so good with numbers, are you?")
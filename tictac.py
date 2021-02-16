import itertools

def game_board(game_map, player=0, row=0, column=0, just_display=False):
	try:
		if game_map[row][column] != 0:
			print("This position is already taken! Try another.")
			return game_map, False
		print("   "+"  ".join([str(i) for i in range(len(game_map))]))
		if not just_display:
			game_map[row][column] = player
		for count, row in enumerate(game_map):
			print(count, row)
		return game_map, True

	except IndexError as e:
		print("Error: make sure you input row/column as a valid number", e)
		return game_map, False

	except Exception as e:
		print("Something went wrong!", e)
		return game_map, False

#checks for a winner
def win(current_game):
	
	def all_same(l):
		if l.count(l[0]) == len(l) and l[0] != 0:
			return True
		else:
			return False

	#checks for horizontal winner
	for row in game:
		print(row)
		#checks if the count of the consecutive appearance of a character = the length of the row
		if all_same(row):
			print(f"Player {row[0]} is the winner horizontally!")
			return True

	#checks for vertical winner
	for col in range(len(game)):
		#creates a list which will be used to store values from each row
		check = []

		for row in game:
			check.append(row[col])

		if all_same(check):
			print(f"Player {check[0]} is the winner vertically!")
			return True

	#checks for forward diagonal winner
	diags = []
	for ix in range(len(game)):
		diags.append(game[ix][ix])
	if all_same(diags):
		print(f"Player {diags[0]} is the winner diagonally!")
		return True

	#checks for reverse diagonal win
	diags = []
	for col, row in enumerate(reversed(range(len(game)))):
		diags.append(game[row][col])
	if all_same(diags):
		print(f"Player {diags[0]} is the winner reverse diagonally!")
		return True

	return False

play = True
players = [1, 2]
while play:
	game = [[0, 0, 0],
			[0, 0, 0],
			[0, 0, 0],]

	game_size = int(input("What size game of tic tac toe? "))
	game = [[0 for i in range(game_size)] for i in range(game_size)]
	game_won = False
	game, _ = game_board(game, just_display=True)
	player_choice = itertools.cycle([1, 2])
	while not game_won:
		current_player = next(player_choice)
		print(f"Current player: {current_player}")
		played = False

		while not played:
			column_choice = int(input("What column do you want to play? (e.g. 0, 1, 2): "))
			row_choice = int(input("What row do you want to play? (e.g. 0, 1, 2): "))
			game, played = game_board(game, player = current_player, row = row_choice, column = column_choice)

		if win(game):
			game_won = True
			again = input("The game is over, would you like to play again? (y/n)")
			if again.lower() == "y":
				print("restarting...")
			elif again.lower() == "n":
				print("goodbye!")
				play = False
			else: 
				print("Not a valid answer! Bye!")
				play = False




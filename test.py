
highestGoal = 0 # The highest goal of userTeam
userTeamName = str(input("Enter your team name: ")) # The name of user`s Team

totalPoints = 0 # Total points for all games of the user's Team


# Creating a function
def askGoal():
    playAgain = "Y" # Variable for asking user to play again
    global goals # Making variable Global
    global highestGoal # Making variable Global
    global totalPoints # Making variable Global
    countGames = 0 # Variable for counting games
    goals = 0 # Total goals of user`s team in each game
    pointsPerGame = 0 # Points of user`s team in each game
    oppositionTeamName = str(input("\nEnter a code of enemy team: ")) # Entering a code of opposition team

    # Creating a while loop that runs as long as the user wants to add new games
    while playAgain == "Y" or playAgain == "y":
        validInt1 = False # Variable for try except
        validInt2 = False # Variable for try except
        userTeamGoals = 0 # Number of goals for user`s team
        oppositionTeamGoals = 0 # Number of goals for opposition team
        countGames += 1 # Variable which counting a number of games
        while not validInt1:
            try:
                userTeamGoals = int(input("How many goals your team scored: ")) # Asking user to enter a number of goals
            except ValueError:
                print("\nYou should use only numbers.\n") # In case of entering not a digit
            else:
                validInt1 = True
        while not validInt2:
            try:
                oppositionTeamGoals = int(input("How many goals enemy team scored: ")) # Asking opposition team to
                # enter a number of goals
            except ValueError:
                print("\nYou should use only numbers.\n") # In case of entering not a digit
            else:
                validInt2 = True
        goals = goals + userTeamGoals # Summarising a numbers of goals for each game for user`s team
        if userTeamGoals > oppositionTeamGoals:
            pointsPerGame += 3 # Adding points in case of win
        elif userTeamGoals == oppositionTeamGoals:
            pointsPerGame += 1 # Adding points in case of draw
        else:
            pointsPerGame = pointsPerGame
        if userTeamGoals >= highestGoal: # Checking for the highest goal
            highestGoal = userTeamGoals
        playAgain = str(input(print("If you plaid more enter 'Y', if not enter 'N': "))) # Asking a user to enter again
    totalPoints += pointsPerGame # Adding a total points for all games
    print('{:68s}'.format("\n\nOpposition team code: "), oppositionTeamName) # Output a name of opposition team
    print('{:66s}'.format("Games played: "), countGames) # Output a number of games played
    print('{:66s}'.format("Goals for: "), goals) # Output a number of goals
    print('{:66s}'.format("Points: "), pointsPerGame) # Output of points


askGoal() # Calling function
askGoal()
askGoal()


print('{:69s}'.format("\n\n\nUser`s team name: "), userTeamName) # Output a name of user team
print('{:66s}'.format("Points: "), totalPoints) # Output of total points for all games
print('{:50s}'.format("Highest number of goals scored by user`s team in a single match:  "), highestGoal) # Output a
# highest number of goals

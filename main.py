
highestGoal = 0
userTeamName = str(input("Enter your team name: "))
totalPoints = 0
goals = 0
highestGoal = 0
def askGoal():
    againFirst = "Y"

    global goals
    global totalPoints
    global highestGoal
    points = 0
    count = 0
    goals = 0
    enemyTeamFirst = str(input("\nEnter a code of enemy team: "))

    while againFirst == "Y" or againFirst == "y":
        userTeam = 0
        firstTeamScore = 0
        count += 1
        userTeam = int(input("How many goals your team scored: "))
        enemyTeam = int(input("How many goals enemy team scored: "))
        goals = goals + userTeam
        if userTeam > enemyTeam:
            points = points + 3
        elif userTeam == enemyTeam:
            points = points + 1
        else:
            points = points
        totalPoints = totalPoints + points
        if goals >= highestGoal:
            highestGoal = goals
        againFirst = str(input(print("If you want play enter 'Y', if you want stick 'N': ")))
    print("\n\nOpposition team code: ", enemyTeamFirst)
    print("Games played: ", count)
    print("Goals for: ", goals)
    print("Points: ", points)


askGoal()
askGoal()
askGoal()


print("\n\n\nUser`s team name: ", userTeamName)
print("Points: ", totalPoints)
print("Highest number of goals scored by user`s team in a single match: ", highestGoal)
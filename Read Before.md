# PythonAssignment2
This task is much easier than the first one. This is the first time I have used a function.

Also for this task we should test the program and create a documentation. There is no point in sharing the documentation, but if you ask me, I will send you a copy.


Below you can see a program specification.

An application allows a user to enter data for matches played by their team and display a summary of results.
The team plays 3 other teams a number of times (it may play some teams more than others).
The program will accept data for all matches played by the user’s team and display suitable output
as detailed below.

The results for all matches against one of the 3 teams are entered one after the other.
The program then moves on to the next team and accepts data for each match played against that team and so on until data for all matches played by the user’s team has been entered.

The program begins by prompting the user for the name of their team.
Next, the user is prompted for the code, (e.g. CFC), for the first team played.
Then for each match against that team, the program prompts the user to enter the goals scored by their own team followed by the goals scored by the other team.

The user is then asked if another game was played.
• If yes, the user is again prompted for goals scored by each team as described above.
• If no, the user is prompted to enter the code for the next team and so on until scores for all
the matches against all 3 other teams have been entered
After all scores for all matches against a particular team are entered the following results are
displayed:
Opposition team code: <OPPOSITION TEAM CODE>, 
Games played: <number of games played>;
Goals for: <total number of goals scored by user’s team>, 
Points: < user team number of points>
After all scores for all matches against all the teams are entered, the following results are displayed:
User’s team name: <user’s team name> 
Points: <total number of points (user team)> 
Highest number of goals scored by user’s team in a single match: < number of goals scored >
  Note:
• The program will not prompt for the number of matches played against a team and no number should be assumed
• The following are not to be used anywhere in the program: break, continue.
• Points are awarded as follows: 3 for a win, 1 for a draw, 0 for a loss.
• The program will handle non-numeric data entered for the goals scored by user’s team by
re-prompting the user. No other data entered by the user needs to be verified.
• You can assume that at least one match will be played against each of the 3 other teams
• Prompts should be consistent, clear and as helpful as possible to the user
• All output should be well formatted and consistent (spelling, upper/lower case etc.)

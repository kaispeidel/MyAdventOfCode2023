def main():
    import os
    os.chdir("/Users/kai/Documents/code/AdventOfCode")  # Change the current working directory

    myfile = "tag4.txt"  # Set the filename to "tag4.txt"

    # Function to process the cards from a file
    def MyCards(filename):
        delimiter = "|"
        with open(filename) as f:
            lines = f.readlines()
            cleaned = []
            for line in lines:
                index = line.find(delimiter)
                cleaned.append(line[index+1:-1])
            cleaned = [x.replace("  ", " ") for x in cleaned]
            cleaned = [x.replace(" ", ",") for x in cleaned]

            clean = []

            for i in cleaned:
                mylist = i.split(",")
                int_list = []
                for item in mylist:
                    try:
                        # Attempt to convert each item to an integer
                        int_value = int(item)
                        int_list.append(int_value)
                    except ValueError:
                        # If conversion fails, skip the instance
                        pass
                clean.append(int_list)

        return clean

    # Function to process the winning numbers from a file
    def Winning(filename):
        delimiter = "|"
        game = []
        with open(filename) as f:
            lines = f.readlines()
            cleaned = []
            count = 1
            for line in lines:
                index = line.find(delimiter)
                index2 = line.find(":")
                cleaned.append(line[index2+1:index])
                game.append(count)
                count += 1
            cleaned = [x.replace("  ", " ") for x in cleaned]
            cleaned = [x.replace(" ", ",") for x in cleaned]

            clean = []

            for i in cleaned:
                mylist = i.split(",")
                int_list = []
                for item in mylist:
                    try:
                        # Attempt to convert each item to an integer
                        int_value = int(item)
                        int_list.append(int_value)
                    except ValueError:
                        # If conversion fails, skip the instance
                        pass
                clean.append(int_list)
        return clean, game

    mycards = MyCards(myfile)  # Process the cards from the file
    winingcard = Winning(myfile)[0]  # Process the winning numbers from the file
    game = Winning(myfile)[1]  # Get the game numbers

    # Function to play the game and calculate points
    def PlayGame(mycards, winingcard, game):
        output = ""
        total = 0
        for i in range(len(mycards)):
            points = 0
            nums = []
            for j in range(len(mycards[i])):
                if mycards[i][j] in winingcard[i]:
                    nums.append(mycards[i][j])
                    if points == 0:
                        points += 1
                    else:
                        points *= 2
            output += f"Card {game[i]} has {points} points, and the numbers are {nums} \n"
            total += points
        return total

    output1 = PlayGame(mycards, winingcard, game)  # Play the game and calculate points

    # Function to create a dictionary of games
    def game_dic(mycards, winingcard, game):
        dic = {}
        for i in range(len(game)):
            bubu = {}
            bubu["w"] = winingcard[i]
            bubu["c"] = mycards[i]
            dic[game[i]] = bubu
        return dic

    games = game_dic(mycards, winingcard, game)  # Create a dictionary of games

    cards_won = 0

    # Function to play the second game and track the cards won
    def PlayGame2(games, starting_index):
        cards = games[starting_index]
        copys = []
        ww = cards["w"]
        ccc = cards["c"]
        num_of_wins = 0
        for num in ccc:
            if num in ww:
                num_of_wins += 1
                copys.append(starting_index + num_of_wins)
        return copys

    tot_copys = game  # Initialize the list of copied games

    # Play the second game for each game and update the list of copied games
    for g in game:
        tot_copys.extend(PlayGame2(games, g))

    solutionpart1 = output1  # Store the solution for part 1
    solutionpart2 = len(tot_copys)  # Store the solution for part 2

    print(solutionpart1)  # Print the solution for part 1 #23235
    print(solutionpart2)  # Print the solution for part 2 #5920640

if __name__ == "__main__":
    main()

#! Determine which games would have been possible if the bag had been 
#! loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. 
#!  What is the sum of the IDs of those games?

def main():
    import os
    import re
    
    os.chdir("/Users/kai/Documents/code/AdventOfCode")
    
    with open("input2.txt") as f:
        data = f.read().splitlines()
        #print(data)

    game_dict = {}
    solution_dict = {}
    
    for line in data:
        game_dict[line[:line.find(":")]] = [line[line.find(":")+1:]]

    
    for element in game_dict:
        liste = re.split(r'[,;]', game_dict[element][0])
        
        for i in range(len(liste)):
            liste[i] = liste[i].strip()
            liste[i] = liste[i].split(" ")
            liste[i][0] = int(liste[i][0])
            liste[i][1] = liste[i][1].strip()
            liste[i] = tuple(liste[i])
            
        game_dict[element] = liste
     #*   print(liste)
     
    games = {}
    
    for x in game_dict.items():
        g = x[0]
        for index in range(len(g)):
            if g[index].isdigit():
                g = g[index:]
                break
                

        value = x[1]
        red_vals = []
        green_vals = []
        blue_vals = []
        for i in range(len(value)):
            if value[i][1] == "red":
                red_vals.append(value[i][0])
            elif value[i][1] == "green":
                green_vals.append(value[i][0])
            elif value[i][1] == "blue":
                blue_vals.append(value[i][0])

        highest_col = {}
        highest_col["red"] = max(red_vals)
        highest_col["green"] = max(green_vals)
        highest_col["blue"] = max(blue_vals)

        games[int(g)] = highest_col

    #! part one:
    input = (12, "red"), (13, "green"), (14, "blue")
    items = games.keys()
    solution = []
    bububububu = 0

    for g in items:
        count = 0
        colors = games[g]
        for i,j in input:
            if colors[j] > i:
                break
            else:
                count += 1
        if count == 3:
            solution.append(f"Game {g} is possible")
            bububububu += g
            
    #! part two:
    solution2 = 0

    for y in items:
        one = 1
        power = []
        vals = games[y]
        for i,j in vals.items():
            power.append(j)
        for nummer in power:
            one *= nummer
        solution2 += one
        
    print(solution2)
            
    
        
    
    
    #print(solution)
    #print(bububububu)

    
        
   
         
     


    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()
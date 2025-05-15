f = open("day2.txt", "r")

test = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]

# 12 red, 13 green, 14 blue

def getNum(str):
    str = str.split(" ")
    num = int(str[0])
    return num

def isPossible(red, green, blue):
    if red > 12: return False
    if green > 13: return False
    if blue > 14: return False
    return True

def getGameNum(line):
    line = line.split(":")
    return int(line[0].split(" ")[1])


total = 0
#lines in the file
for line in f:
    toAdd = getGameNum(line)

    line = line.split(":")[1].strip()
    #split line by ; to get each set
    sets = line.split(";")
    
    #loop through the sets
    for set in sets:
        set = set.strip()
        red = green = blue = 0
        #split each set by , to get number of cubes in one set
        cubes = set.split(",")
        for cube in cubes:
            cube = cube.strip()
            if "red" in cube:
                red = getNum(cube)
            if "blue" in cube:
                blue = getNum(cube)
            if "green" in cube:
                green = getNum(cube)
        
        #check if any of the nums exceed 
        if not isPossible(red, green, blue):
            toAdd = 0
            break

    total += toAdd

print("total: " , total)
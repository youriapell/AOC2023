def countColours(game):
    colours = {'red':0, 'green':0, 'blue':0}
    for roll in game:
        for cube in roll:
            if int(cube[0]) > colours.get(cube[1]):
                colours[cube[1]] = int(cube[0])
    return colours

def solution(part):
    with open("day2\input.txt") as input:
        games = [[[cubes.split(" ") for cubes in roll.split(", ")] for roll in game.split(": ")[1].split("; ")] for game in input.read().strip().split("\n")]
        output = 0
        for gameIndex in range(len(games)):
            gameColours = countColours(games[gameIndex])
            if(part == 1):
                if gameColours.get('red') <= 12 and gameColours.get('green') <= 13 and gameColours.get('blue') <= 14:
                    output += gameIndex + 1
            if (part == 2):
                output += gameColours.get('red') * gameColours.get('green') * gameColours.get('blue')
        return output

if __name__ == "__main__"  :
    print(solution(1))
    print(solution(2))
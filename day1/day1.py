def getDigits(calibration):
    for character in calibration:
        if character in "1234567890":
            firstNumber = int(character)
            break
    for character in calibration[::-1]:
        if character in "1234567890":
            secondNumber = int(character)
            break
    return 10*firstNumber + secondNumber

def solution():
    answer = 0
    with open("day1\input.txt") as input:
        calibrations = input.read().strip().split("\n")
        for i in calibrations:
            answer += getDigits(i)
    return answer

if(__name__ == "__main__"):
    print(solution())
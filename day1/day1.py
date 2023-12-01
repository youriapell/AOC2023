def findFirstStringDigit(calibration):
    stringDigits = ["one","two","three","four","five","six","seven","eight",'nine']
    firstDigit = None
    firstDigitLocation = -1
    for digit in stringDigits:
        digitLocation = calibration.find(digit)
        if (digitLocation < firstDigitLocation or firstDigitLocation == -1) and digitLocation != -1:
            firstDigit = digit
            firstDigitLocation = digitLocation
    return firstDigit

def findLastStringDigit(calibration):
    stringDigits = ["one","two","three","four","five","six","seven","eight",'nine']
    lastDigit = None
    lastDigitLocation = -1
    for digit in stringDigits:
        digitLocation = calibration.rfind(digit)
        if (digitLocation > lastDigitLocation or lastDigitLocation == -1) and digitLocation != -1:
            lastDigit = digit
            lastDigitLocation = digitLocation
    return (lastDigit,lastDigitLocation)


def getDigits(calibration):
    for character in calibration:
        if character in "1234567890":
            firstDigit = int(character)
            break
    for character in calibration[::-1]:
        if character in "1234567890":
            lastDigit = int(character)
            break
    return 10*firstDigit + lastDigit

def getAllDigits(calibration):
    firstStringDigit = findFirstStringDigit(calibration)
    lastStringDigit = findLastStringDigit(calibration)
    firstIntDigit = getDigits(calibration) //10
    lastIntDigit = getDigits(calibration) % 10

    stringDigits = ["one","two","three","four","five","six","seven","eight",'nine']
    if firstStringDigit != None and calibration.find(firstStringDigit) < calibration.find(str(firstIntDigit)):
        firstDigit = stringDigits.index(firstStringDigit) + 1
    else: 
        firstDigit = firstIntDigit

    if lastStringDigit[0] != None and lastStringDigit[1] > calibration.rfind(str(lastIntDigit)):
        lastDigit = stringDigits.index(lastStringDigit[0]) + 1
    else: 
        lastDigit = lastIntDigit

    #print(f"{10*firstDigit + lastDigit}|{calibration}")
    return 10*firstDigit + lastDigit

def solution(part):
    answer = 0
    with open("day1\input.txt") as input:
        calibrations = input.read().strip().split("\n")
        if part == 1:
            for i in calibrations:
                answer += getDigits(i)
        if part == 2:
            for i in calibrations:
                answer += getAllDigits(i)
    return answer

if(__name__ == "__main__"):
    print(f"Part 1 solution: {solution(1)}")
    print(f"Part 2 solution: {solution(2)}")
    print(getAllDigits("foursixn8two7srvbbdldpbtwo"))
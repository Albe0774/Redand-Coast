import random

InputTemp = 12
AvTemp = 5
numberofdays = 10

days = 1
for x in range(numberofdays):

    Diceroll = random.randint(1,8)
    TempDiff = InputTemp - AvTemp

    if TempDiff >= 8:
        match Diceroll:
            case 1:
                    DeltaTemp = 0
            case roll if 2 <= roll <= 3:
                    DeltaTemp = -1
            case roll if 4 <= roll <= 5:
                    DeltaTemp = -2
            case roll if 6 <= roll <= 8:
                    DeltaTemp = -3

    elif 5 <= TempDiff <= 7:
        match Diceroll:
            case 1:
                    DeltaTemp = 1
            case 2:
                    DeltaTemp = 0
            case 3:
                    DeltaTemp = -1
            case roll if 4 <= roll <= 5:
                    DeltaTemp = -2
            case roll if 6 <= roll <= 8:
                    DeltaTemp = -3

    elif 2 <= TempDiff <= 4:
        match Diceroll:
            case 1:
                    DeltaTemp = 2
            case 2:
                    DeltaTemp = 1
            case 3:
                    DeltaTemp = 0
            case roll if 4 <= roll <= 5:
                    DeltaTemp = -1
            case roll if 6 <= roll <= 7:
                    DeltaTemp = -2
            case 8:
                    DeltaTemp = -3

    elif -1 <= TempDiff <= 1:
        match Diceroll:
            case 1:
                    DeltaTemp = 3
            case 2:
                    DeltaTemp = 2
            case 3:
                    DeltaTemp = 1
            case roll if 4 <= roll <= 5:
                    DeltaTemp = 0
            case 6:
                    DeltaTemp = -1
            case 7:
                    DeltaTemp = -2
            case 8:
                    DeltaTemp = -3

    elif -4 <= TempDiff <= -2:
        match Diceroll:
            case 1:
                    DeltaTemp = 3
            case roll if 2 <= roll <= 3:
                    DeltaTemp = 2
            case roll if 4 <= roll <= 5:
                    DeltaTemp = 1
            case 6:
                    DeltaTemp = 0
            case 7:
                    DeltaTemp = -1
            case 8:
                    DeltaTemp = -2
            
    elif -7 <= TempDiff <= -5:
        match Diceroll:
            case roll if 1 <= roll <= 3:
                    DeltaTemp = 3
            case roll if 4 <= roll <= 5:
                    DeltaTemp = 2
            case 6:
                    DeltaTemp = 1
            case 7:
                    DeltaTemp = 0
            case 8:
                    DeltaTemp = -1

    elif TempDiff <= -8:
        match Diceroll:
            case roll if 1 <= roll <= 3:
                    DeltaTemp = 3
            case roll if 4 <= roll <= 5:
                    DeltaTemp = 2
            case roll if 6 <= roll <= 7:
                    DeltaTemp = 1
            case 8:
                    DeltaTemp = 0


    NewTemp = InputTemp + DeltaTemp
    InputTemp = NewTemp

    print("On day", days, "the temp. is", NewTemp, "degree Celsius")
    
    days = days + 1
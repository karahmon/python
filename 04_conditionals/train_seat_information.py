seat_selection = input ("Enter your prefered seat type (sleeper / AC / general / luxary) : ").lower()

match seat_selection :
    case "sleeper" :
        print("Sleeper - No AC, beds Available")
    case "ac" :
        print("AC- Air Conditioned, beds Available")
    case "general" :
        print("general - No AC, No beds Available")
    case "luxary" :
        print("luxary - Air Conditioned, luxary beds Available")
    case _ :
        print("Invalid Seat Type")


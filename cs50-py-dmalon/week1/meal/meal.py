def main():
    time = input("Enter the time in format HH:MM > ")
    # time = "13:23"
    # time = "7:30"
    # time = "18:45"
    # time = "07:1"
    # time = "21:45"

    decimalTime = convert(time)

    if 7 <= decimalTime <= 8:
        print("breakfast time")
    elif 12 <= decimalTime <= 13:
        print("lunch time")
    elif 18 <= decimalTime <= 19:
        print("dinner time")
    else:
        None    

def convert(time):
    hours, minutes = time.strip().split(":")
    timeF = int(hours) + int(minutes) / 60
    return timeF

# def convert(time):
#     # Split the time string into hours and minutes
#     hours, minutes = map(int, time.split(':'))
#     timeF = hours + minutes / 60
#     return timeF

if __name__ == "__main__":
    main()
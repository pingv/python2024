def main():
    while True:
        fraction = input("Fraction: ").strip()
        try:
            percentage = convert(fraction)
            gauge_value = gauge(percentage)
            print(gauge_value)
            break  # Exit the loop if input is valid
        except (ValueError, ZeroDivisionError) as e:
            print(e)  # Print error message and prompt again

def convert(fraction):
    x, y = fraction.split('/')
    try:
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError("Y must be greater than 0.")
        if x > y:
            raise ValueError("X cannot be greater than Y.")
        percentage = round((x / y) * 100)
        return max(0, min(percentage, 100))  # Ensure the percentage is within 0 to 100
    except ValueError:
        raise ValueError("X and Y must be integers.")

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()

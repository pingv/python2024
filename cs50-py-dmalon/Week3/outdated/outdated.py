from datetime import datetime

def main():
    month_array = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    get_date(month_array)

def get_date(month_array):
    while True:
        try:
            date_input = input("Date: ").strip()
            date_obj = None
            
            # Try parsing the date in the format 'Month day, year'
            try:
                date_obj = datetime.strptime(date_input, '%B %d, %Y')
            except ValueError:
                pass

            # Try parsing the date in the format 'month/day/year' or 'month-day-year'
            if date_obj is None:
                for fmt in ('%m/%d/%Y', '%m-%d-%Y'):
                    try:
                        date_obj = datetime.strptime(date_input, fmt)
                        break
                    except ValueError:
                        continue

            if date_obj is None:
                raise ValueError("")

            a_month = date_obj.month
            a_date = date_obj.day
            a_year = date_obj.year

            # print("Month:", a_month)
            # print("Day:", a_date)
            # print("Year:", a_year)

            # The below code to validate is unnecessary as the date object does the validation and throws the error
            # # Validate year
            # if not isinstance(a_year, int):
            #     print("Enter a proper year in the format month 9/8/1636 or September 8, 1636")
            #     continue

            # # Validate month
            # if not ((1 <= a_month <= 12)):
            #     print("Enter a proper month between 1 & 12 - in the format month 9/8/1636 or September 8, 1636")
            #     continue

            # # Validate day
            # if not (1 <= a_date <= 31):
            #     print("Enter a proper day between 1 & 31 - in the format month 9/8/1636 or September 8, 1636")
            #     continue

            # a_month_str = f"{a_month:02}"
            # a_day_str = f"{a_day:02}"
            
            # Convert numeric month to month name - Not required here as only month in digit needs to be printed
            a_month_name = month_array[a_month - 1]
            print(f"{a_year}-{a_month:02}-{a_date:02}")

            break

        except ValueError as e:
            # print(e)
            continue

if __name__ == "__main__":
    main()
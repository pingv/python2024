def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    #return
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    #print('dollars_to_float', d)
    dollarsInFloat = float( d.strip('$'))
    #print('Float Val ', dollarsInFloat)
    return dollarsInFloat




def percent_to_float(p):
    # TODO
    #print('percent_to_float',p) 
    percentInFloat = float(p.strip('%'))/100
    #print('Float Percent ', percentInFloat)
    return percentInFloat

main()

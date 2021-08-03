# Date picker for a website: gather the start year and end year from the user and print a list with the years
# between them. Example: 2005 - 2011; print 2005, 2006, 2007, 2008, 2009, 2010

def datepicker(val1, val2):
    """Method to return the list with years between 2 given dates"""
    years = list(range(val1, val2))
    # if the start year is higher than the end year, printing a list starting with the end year
    if val1 > val2:
        years = list(range(val2, val1))
    print("The list with years between the selected dates is: {}".format(years))


correct_years = True
while correct_years:
    try:
        start_year = int(input("Enter the start year -> "))
        end_year = int(input("Enter the end year -> "))
    except ValueError:
        print("Incorrect years")
        correct_years = False
    else:
        datepicker(start_year, end_year)
        break

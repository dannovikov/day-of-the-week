# This program implements an algorithm for figuring
# out which day of the week a given date is.

# Initializing global variables used for calculation:

month, day, year = 0, 0, 0

# first two and last two digits of the year
f2_year, l2_year = 0, 0

# algorithm requires specific numbers for month and century
month_code, century_code = 0, 0

# Dictionaries:
month_codes = {
    1: 1,           # January
    2: 4,           # February
    3: 4,
    4: 0,
    5: 2,
    6: 5,
    7: 0,
    8: 3,
    9: 6,
    10: 1,
    11: 4,
    12: 6           # December
}

century_codes = {
    17: 4,          #1700s
    18: 2,
    19: 0,
    20: 6           #2000s
}

day_codes = {
    0: "Saturday",
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday"
}


# to get valid user input
def get_input():
    x = input('Please enter a date, in MM/DD/YYYY format:\n')
    while len(x) < 10:
        print('Please follow the input format MM/DD/YYYY:\n')
    parse_input(x)


# to parse input for date
def parse_input(user_input):

    str_month, str_day, str_year = '', '', ''
    refined_input = user_input.replace('/', '')

    #refined_input is now a string of 8 numbers with slashes removed

    for i in range(len(refined_input)):
        if i < 2:
            str_month += refined_input[i]
        elif i < 4:
            str_day += refined_input[i]
        else:
            str_year += refined_input[i]

    parse_year(str_year)

    global month, day, year, month_code, century_code
    month, day, year = \
        int(str_month),\
        int(str_day), \
        int(str_year)

    month_code = month_codes[month]

    if year < 1700:
        while year < 1700:
            year += 400
        # print(f'Year has been converted to {year} for calculations.')
    elif year > 2100:
        while year > 2100:
            year -= 400
        # print(f'Year has been converted to {year} for calculations.')

    parse_year(str(year))
    century_code = century_codes[f2_year]


def parse_year(str_year):
    str_f2y, str_l2y = '', ''
    for i in range(len(str_year)):
        if i < 2:
            str_f2y += str_year[i]
        else:
            str_l2y += str_year[i]
    global year, f2_year, l2_year
    f2_year = int(str_f2y)
    l2_year = int(str_l2y)
    year = int(str_year)


# calculate day of the week
def calculate_day():
    global day, l2_year, month, year, month_code, century_code

    f = l2_year
    f = int(f/4)
    f += day
    f += month_code

    if month == 1 or month == 2:
        if check_leap(year) == True:
            f -= 1

    f += century_code
    f += l2_year

    f = f % 7

    return day_codes[f]


def check_leap(year):
    result = False
    if year % 4 == 0:
        result = True
        if year % 100 == 0:
            result = False
            if year % 400 == 0:
                result = True
    return result


try_again = 'y'
while try_again == 'y':
    get_input()
    DayResult = calculate_day()
    print(f'This date falls on a {DayResult}.\n')
    try_again = input('Would you like to try another date? y/n: \n')
    while try_again != 'y' and try_again != 'n':
        print('Please write either \'y\' or \'n\'')
        try_again = input('Would you like to try another date? y/n: \n')

print('Thank you!')






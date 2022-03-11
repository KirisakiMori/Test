import sys
sys.path.append('../Test')
from mydates import Dates
from mydates import print_test

birth_day = '1999-11-09'
wedding_day = '2030-05-09'

mydays = Dates.Important_Dates(birth_day,wedding_day)

mydays.getDaysPassedInMyLife()

mydays.get_days_passed_in_marriage()

print_test()
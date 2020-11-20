import datetime as d



###EXAMPLE
##def calculate_age( year_of_birth):
##    this_year = d.datetime.now().year
##    age = this_year - year_of_birth
##    return age
##
##
###MAIN
##birth_year = int(input("Enter the year you were born"))
##
##age_this_year = calculate_age(birth_year)
##
##print(f'You will turn {age_this_year} in 2020')



###EXAMPLE
##import math
##
##
##def hypotenuse(a, b):
##    
##    c = math.sqrt(a**2 + b**2)
##    return c
##
##
###main
##side_1 = float(input("Enter side 1 of triangle"))
##side_2 = float(input("Enter side 2 of triangle"))
##
##hyp = hypotenuse(side_1, side_2)
##print(f'Triangle with sides {side_1} & {side_2} has hypotenuse {hyp:.1f}')
##
##
##
##
###EXAMPLE
##def calculate_one_rep_max(weight, num_reps):
##
##    one_rep_max = weight / (1.0278 - (0.0278 * num_reps))
##    return one_rep_max     
##
###MAIN
##weight_lifted = 215
##number_reps = 6
##
##result = calculate_one_rep_max(weight_lifted, number_reps)
##
##print(f'Based on {weight_lifted} lbs for {number_reps} reps')
##
##print(f'Your 1 rep max is: {result:.0f} lbs')

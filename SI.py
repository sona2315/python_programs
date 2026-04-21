# The task of calculating Simple Interest in Python 
# involves taking inputs for principal amount, time period in years,
#  and rate of interest per annum, applying the Simple Interest formula and displaying the result.
# For example, if p = 1000, t = 2 (years), and r = 5%, the Simple Interest is 
# calculated using the formula and resulting in Simple Interest = 100.0.

# Simple interest formula :

#  Simple Interest = (P x T x R)/100

#method 1
Pr_amount=int(input("Enter principal amount: "))
Time_period=int(input("Enter Time period in yrs: "))
RI=int(input("Enter rate of interest per annum: "))

total = Pr_amount*Time_period*RI
SI=total/100
print(SI)

#method 2
p, t, r = 8, 6, 8

si = [p * t * r / 100][0]
print(si)
# use a named constant
# by using 2.0 as its value, it is automatically storeed as a float
# because we defined it at the top level, it is available to any function
# in our program 
COST_PER_HOUR = 2.0 

def calculate_estimated_parking_cost(parked_hours):
    estimated cost = parked_hours
    return estimated_cost

# define the main logic of my program 
def main():
    #(input)
    # create a variable in which I will store user-entered parked hours
    # a variable is a named space in memory
    parked_hours = input ("how many houts will you be parked / have you parked?")

# call our function (processing)
Estimated cost = calculate_estimated_parking_cost(parked_hours)

# (estimated cost)
print(cost)

# call my main function and execute the logic of the program 
main()

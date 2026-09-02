days = int(input("Enter the amount of days you are staying in the hotel: "))
city = "New york"
days_ride = int(input("Enter the amount of days you rode the car: "))

def cost_of_stay(days):
    cost_of_stay = days*200
    return cost_of_stay
the_cost_of_stay = cost_of_stay(days) 
def cost_of_plane(city):
    if city == "New york":
        cost_of_ride = 20000
        return cost_of_ride
    elif city == "London":
        cost_of_ride = 15000
        return cost_of_ride
    elif city == "Paris":
        cost_of_ride = 10000
        return cost_of_ride
    else:
        pass
cost_of_theplane = cost_of_plane(city)
def cost_of_car(days_ride):
    if days_ride > 7:
        cost_of_car = 10*days
        return cost_of_car
    elif days_ride > 5:
        cost_of_car = 20*days
        return cost_of_car
    elif days_ride > 3:
        cost_of_car = 30*days
        return cost_of_car
    else:
        cost_of_car = 40*days
        return cost_of_car
cost_for_car = cost_of_car(days_ride)
total = cost_of_theplane + cost_for_car + the_cost_of_stay
print("Your expenditure for staying at the hotel is:  ₹", the_cost_of_stay)
print("Your expendeiture for flying to", city, "is:  ₹", cost_of_theplane)
print("Your expenditure for riding the car for, ", days_ride, "is:  ₹", cost_for_car)
print("Your total expenditure will be:  ₹", total, "\nThanks for using our softawre!")

    



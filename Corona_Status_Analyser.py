import sys
import datetime
import random

my_dict = {}
d= 1
city_number = int(input("Enter number of cities to check Corona status: "))
if city_number < 3:
    sys.exit("Please enter minimum 3 or more number of cities")

days = int(input("Enter number of days to check Corona status: "))
if days < 5:
    sys.exit("Please enter minimum 5 or more number of days")

temp=days

def cases():                                            # function to generating random number
    c = random.randint(1, 1000)                         # for particular day
    for i in range(1):                                  # it will generate random number between 1 to 1000
        return c


for i in range(city_number):                            # For loop will iterate based on number of Cities given in input
    city_name = str(input("Enter City name: "))
    day_1 = datetime.date.today()                       # Function to get Today's date
    num1 = cases()
    print(city_name, " Corona Patient Number On - ", day_1, ":", num1)
    count = 1
    sum1 = 0
    sum1 = sum1 + num1

    for i in range(days-1):                             # For loop will iterate based on number of Days given in input
        day_2 = day_1 - datetime.timedelta(days=d)      # Function to get the date in decremental for number of
        num = cases()                                   # days given in input
        print(city_name, " Corona Patient Number On - ", day_2, ":", num)
        d = d + 1
        sum1 = sum1 + num
        count = count + 1

    # print("Total sum:", sum1)
    # print("Total count:", count)
    avg = sum1 / count                                  # Counting average cases for particular city
    # print("Average cases in", city_name, "is :", avg)
    my_dict.update({city_name: avg})                    # Creating dictionary, City name in Key & Average in Value
    d=1
print(my_dict)
max_avg = max(my_dict, key=my_dict.get)                 # Finding maximum average number from the dictionary
print(" ***** [Result ] The Most Affected City is :   ", max_avg, "  *****")

min_avg = min(my_dict, key=my_dict.get)                 # Finding minimum average number from the dictionary
print("***** [Result ] The Least Affected City is :   ", min_avg, "  *****")

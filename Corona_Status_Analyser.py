# Exercise Name -   Corona Status Analyser

# Steps  -
# Users have to provide a minimum 3 number of cities. If it is less than 3 then the program should be terminated. (Hint : use sys.exit() to terminate)
# After successful completion of the step-1, Users have to provide a minimum 5 days time period. If it is less than 5 then the program should be terminated.
# After successful completion of the step-2, Users have to provide the city name and "corona patient" number for each descending date starting from the date of execution.  (Hint : use "datetime" or "time"  library)
# The program will show the output as the safest city and most affected city for a given time period based on averaging the "corona patient" number.
# Please check the Output-5 below as the final output of this exercise.
# The program should be dynamic. It should work with any "n" number of cities and any "t" number of time periods for any "c" cities.

# OUTPUT:

'''
How Many cities do you want to include for Analysis ? : 4
How Many days do you want for Analysis ? : 7

Please Enter city name : Delhi
Delhi's Corona Patient Number On - 01/10/2020 : 895
Delhi's Corona Patient Number On - 30/09/2020 : 754
Delhi's Corona Patient Number On - 29/09/2020 : 853
Delhi's Corona Patient Number On - 28/09/2020 : 851
Delhi's Corona Patient Number On - 27/09/2020 : 658
Delhi's Corona Patient Number On - 26/09/2020 : 365
Delhi's Corona Patient Number On - 25/09/2020 : 451

Please Enter city name : Ahmedabad
Ahmedabad's Corona Patient Number On - 01/10/2020 : 256
Ahmedabad's Corona Patient Number On - 30/09/2020 : 221
Ahmedabad's Corona Patient Number On - 29/09/2020 : 269
Ahmedabad's Corona Patient Number On - 28/09/2020 : 361
Ahmedabad's Corona Patient Number On - 27/09/2020 : 321
Ahmedabad's Corona Patient Number On - 26/09/2020 : 369
Ahmedabad's Corona Patient Number On - 25/09/2020 : 350

Please Enter city name : Mumbai
Mumbai's Corona Patient Number On - 01/10/2020 : 1234
Mumbai's Corona Patient Number On - 30/09/2020 : 695
Mumbai's Corona Patient Number On - 29/09/2020 : 987
Mumbai's Corona Patient Number On - 28/09/2020 : 956
Mumbai's Corona Patient Number On - 27/09/2020 : 876
Mumbai's Corona Patient Number On - 26/09/2020 : 1123
Mumbai's Corona Patient Number On - 25/09/2020 : 1023

Please Enter city name : Bangalore
Bangalore's Corona Patient Number On - 01/10/2020 : 245
Bangalore's Corona Patient Number On - 30/09/2020 : 236
Bangalore's Corona Patient Number On - 29/09/2020 : 253
Bangalore's Corona Patient Number On - 28/09/2020 : 221
Bangalore's Corona Patient Number On - 27/09/2020 : 196
Bangalore's Corona Patient Number On - 26/09/2020 : 156
Bangalore's Corona Patient Number On - 25/09/2020 : 159

 ***** [Result ] The Least Affected City is :   Bangalore  *****
 ***** [Result ] The Most Affected City is :   Mumbai  *****
'''
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

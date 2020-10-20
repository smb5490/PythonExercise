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
total_sum = 0
count = 0

# Function will generate and return random cases from range 1 to 1000 on every call
def cases():
    c = random.randint(1, 1000)
    for i in range(1):
        return c

# Function will generate date from the day of execution to given number in descending order on every call.
# Date will in the form of IST i.e. DD/MM/YY
def date_format():
    date = datetime.date.today() - datetime.timedelta(days=j)
    indian_format = date.strftime("%d/%m/%Y")
    return indian_format


city_number = int(input("Enter number of cities to check Corona status: "))
if city_number < 3:
    sys.exit("Please enter minimum 3 or more number of cities")

days = int(input("Enter number of days to check Corona status: "))
if days < 5:
    sys.exit("Please enter minimum 5 or more number of days")

# Loop will iterate for given number_of_city times
for i in range(city_number):
    city_name = str(input("Enter City name: "))
    if len(city_name) == 0:
        sys.exit("City name shouldn't empty, please rerun the application and provide city name")
    # Loop will iterate for given_number_of_days times
    for j in range(days):
        case_num = cases()
        print(city_name, " Corona Patient Number On - ", date_format(), ":", case_num)
        total_sum = total_sum + case_num
        count = count + 1
    # Count average of all city
    avg_city = total_sum / count
    print("Average cases in", city_name, "is :", avg_city)
    count = 0
    total_sum = 0

    my_dict.update({city_name: avg_city})
# To find most affected city
print(my_dict)
max_avg = max(my_dict, key=my_dict.get)
print("***** [Result ] The Most Affected City is  : ", max_avg, " *****")
# TO find least affected city
min_avg = min(my_dict, key=my_dict.get)
print("***** [Result ] The Least Affected City is : ", min_avg, " *****")

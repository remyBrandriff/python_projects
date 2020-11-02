'''

date = input("Enter a date in the format 'MM-DD-YYY': ")
date.split('-') 


months = { "January" : 01,
           "February" : 02,
           "March" : 03,
           "April" : 04,
           "May" : 05,
           "June" : 06,
           "July" : 07,
           "August" : 08,
           "September" : 09,
           "October" : 10,
           "November" : 11,
           "December" : 12 }





def meal_total_cost(meal_price, tip_percen):
    tip = meal_price/tip_percen
    round(tip,2)
    return tip

meal_price = float(input("Enter the meal price: "))
tip_percen = int(input("Enter the percentage for the tip: "))

tip = (meal_total_cost(meal_price, tip_percen))
meal_cost = meal_price + tip
print("The total cost of the meal is $", (meal_cost))




list1 = ("Seattle", "red", "Evelyn", "fox", "Moral Disorder")

def list_sort(list1):
    first_item = list1[0]
    last_item = list1[-1]
    middle_item = list1[2]
    print("The first item in the list is %s" % (first_item))
    print("The last item in the list is %s" % (last_item))
    print("The middle item in the list is %s" % (middle_item))
    print(list1)

list_sort(list1)

'''

def user_input(glossary):
    name = input("Enter your name: ")
    hometown = input("Enter your hometown: ")
    fav_col = input("Enter your favorite color: ")


glossary = { }

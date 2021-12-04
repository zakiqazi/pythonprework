#1
def hello_name(username):
    print(f"hello_{username.upper()}")

hello_name("username")
#2
def first_odds():
    for x in range(1,101):
        if x % 2 != 0:
            print(x)
first_odds() #calling function

#3
def max_num_in_list(a_list):
    print(max(a_list))
max_num_in_list([5, 50]) # put [] inside () so it can read the list

#4

def is_leap_year(a_year):
   
    if a_year % 4 == 0 and a_year % 100 != 0:
        if a_year % 400 == 0:
            return True
    elif a_year % 4 != 0:
        return False
    return True # if it doesnt catch any of the ones above
print(is_leap_year(1968))
    
    
#5

def is_consecutive(a_list):
    counter= a_list[0]
    for num in a_list:
        if num != counter:
            return False
        counter += 1
        # num
    return True

print(is_consecutive([2,3,4,5,6,7]))
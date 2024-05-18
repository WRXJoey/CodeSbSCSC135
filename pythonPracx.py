import math
import random
#Python/parameters and return
def circle_area (Radius):
    return math.pi*Radius*Radius
test1 = circle_area(1)
print("The area of the circle is:", test1)

#Python/parameters and return
def average_of_2(one,two):
    return((one+two)/2)
test2 = average_of_2(100,20)
print("The average of 2 is:", test2)

#Python/if else
def median_of_3(n1, n2, n3):
    if n1 < n2 < n3 or n3 < n2 < n1:
        return n2
    elif n2 < n1 < n3 or n3 < n1 < n2:
        return n1
    else:
        return n3
test3 = median_of_3(100, 50, 30)
print("Median of 100,50,30 is:", test3)

def count_digits(n1):
    n1 = abs(n1)
    result = 0
    while(n1):
        result = result+1
        n1 = n1 // 10
    return result
test4 = (333)
print("count digits: ", test4)

def box_of_stars(width, height):
    for i in range(height):
        if i == 0 or i == height - 1:
            print('*' * width)
        else:
            print('*' + ' ' * (width - 2) + '*')
test5 = box_of_stars(3,3)
print(test5)

def coin_flip(k, side):
    if k < 0 or (side != 'H' and side != 'T'):
        print("ERROR!")
        return
    
    streak = 0
        
    while streak < k:
        result = random.choice(['H', 'T'])
        print(result, end=' ')
            
        if result == side:
            streak += 1
    print(f"\nYou got {side} {k} times in a row!")
test6 = coin_flip(4, 'T')
print(test6)

def average_length(strings):
    total = sum(len(ele) for ele in strings)
    avg = total / len(strings)
    return avg
test7 = average_length(["belt", "hat", "jelly", "bubble gum"])
print(test7)

def is_palindrome(strings):
    return strings == strings[::-1]
test8 = is_palindrome(["alpha", "beta", "gamma", "delta", "gamma", "beta", "alpha"])
print(test8)

def max_length(set_of_strings):
    if not set_of_strings:
        return 0
    else:
        max_total = max(len(ele) for ele in set_of_strings)
        return max_total
test9 = max_length({"four score", "and", "seven", "years ago our forefathers"})
print(test9)
def collapse(num):
    new_list = []
    for i in range(0, len(num), 2):
        if i+1 < len(num):
            new_list.append(num[i] + num[i+1])
        else:
            new_list.append(num[i])
    return new_list       
test10 = collapse([7, 2, 8, 9, 4, 13, 7, 1, 9, 10])
print(test10)

def is_stack_sorted(stack):
    if len(stack) <= 1:
        return True
    
    temp_stack = []
    is_sorted = True
    
    while len(stack) > 1:
        current_ele = stack.pop()
        next_ele = stack[-1]
        
        if current_ele > next_ele:
            is_sorted = False
        
        temp_stack.append(current_ele)
    
    while temp_stack:
        stack.append(temp_stack.pop())
    
    return is_sorted
test11 = is_stack_sorted([20, 20, 17, 11, 8, 8, 3, 2])
print(test11)

def has_duplicate_value(dictionary):
    if len(dictionary) <=1:
        return False
    
    u_values = set()
    for value in dictionary.values():
        if value in u_values:
            return True
        else:
            u_values.add(value)
    return False
test12 =  has_duplicate_value({'Marty': 'Stepp', 'Stuart': 'Reges', 'Jessica': 'Miller', 'Amanda': 'Camp', 'Hal': 'Perkins'})
print(test12)

def remove_duplicates(string_list):
    retain = set()
    string_list[:] = [i for i in string_list if not (i in retain or retain.add(i))]
test13 = remove_duplicates([4, 0, 2, 9, 4, 7, 2, 0, 0, 9, 6, 6])
print(test13)


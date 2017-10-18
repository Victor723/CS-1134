"""
@author: Zhoukx.joseph
"""

# Question 3

def print_triangle(n):
    if n == 0:#base statement
        return
    print_triangle(n-1)#recursion first, then print, to make the shape a triangle.
    print(n*'*')


def print_oposite_triangles(n):
    if n == 0:return#base statement
    print(n*'*')
    print_oposite_triangles(n-1)#make the recursion in the middle, to make the 
    print(n*'*') #shape of an opposite triangle


def print_rulers(n):
    if n == 0: return#base statment
    print_rulers(n-1)#It's pretty similar to the solution of haoni
    print(n*'-')
    print_rulers(n-1)#it recurs 2**n times, so two recursions inside one function
    #can make the shape of the rulers.

# Question 4

def list_min(lst,low,high):
    if low == high: return lst[low]#base statement
    if lst[low] > lst[low+1]:#checking whether it's lower than the next one or not
        return list_min(lst,low+1,high)
    else:
        lst[low+1]=lst[low]#if yes, assign the current one to the next one
        return list_min(lst,low+1,high)

# Question 5(a)

def count_lowercase(s,low,high):
    if low>high:#base statment
        return 0
    else:
        if s[low].islower():#checking if it's lowercase
            return 1+ count_lowercase(s,low+1,high)#if yes, count+1
        else:
            return 0+ count_lowercase(s,low+1,high)#if no, +0

# Question 5(b)
        
def is_number_of_lowercase_even(s, low, high):
    if low == high:
        return s[low].isupper()#let even be true, odd be false.
    else:#count from the last one, if it's lowercase, return False
    #then compare it to the second last one, if it's also lowercase, return True
        return s[low].isupper()==is_number_of_lowercase_even(s,low+1,high)

# Question 6

def appearance(s,low,high):
    if low > high:#base statement
        return {}
    dict=appearance(s,low+1,high)
    if s[low] not in dict:#checking if the item in s is in dict or not
        dict[s[low]]=1
    else:
        dict[s[low]]+=1
    return dict#return dict

# Question 7

def flat_list(nested_lst,low,high):
    if low > high:#base statement
        return []
    if isinstance(nested_lst[low],list):#check if it's a list inside a list
        return flat_list(nested_lst[low],0,len(nested_lst[low])-1)+flat_list(nested_lst,low+1,high)
    else:
        return [nested_lst[low]]+flat_list(nested_lst,low+1,high)

L=[[1,2],2,3,[4,5,[6,7],8]]
print(flat_list(L,1,2))










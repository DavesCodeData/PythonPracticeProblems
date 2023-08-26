def generate_fibonacci(n):
    fib_sequence = [0,1] #wrong
    for i in range(2,n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[1-2])
    return fib_sequence

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) +1):#wrong forgot it must be int
        if num % i == 0:
            return False
    return True

#def reverse_string(s): ALL wrong will return orginal string in same order
#    reversed_str = ""
#    for char in s:#wrong tried to use range
#        reversed_str = reversed_str + char
#    return reversed_str

def is_palindrome(s):
    s = "".join(c.lower()for c in s if c.isalnum())
    return s==s[::-1]

def return_middle(string):
    halfList = len(string)
    if halfList % 2 == 0:
        return "no center sting"
    return string[int(halfList / 2)]

def my_revered_string(s):
    return s[::-1]

def swap_letters(string):
    front = string[0]
    back = string[-1]
    middle = string[1:-1]
    return back + middle + front   
    #return string[-1]+string[1:-1]+string[0]

def find_sequence(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i:i+3] == [1, 2, 3]:
            count +=1
    return count
    #return "no sequence or not a list"

#def find_sequence(lst):
#    sequence = [1, 2, 3]
#    for i in range(len(lst) - 2):
#        if lst[i:i+3] == sequence:
#            return lst
#    return "no such sequence"

#def find_sequence(lst):
#    for i in range(len(lst) - 2):
#        if lst[i:i+3] == [1, 2, 3]:
#            return lst
#    return "no such sequence"

def frizzBuzz(n, num1, num2):
    for num in range(2,n+1):
        if num % num1 == 0 and num % num2 ==0:
            print("FrizzBuzz")
        elif num % num1 == 0:
            print("Frizz")
        elif num % num2 == 0:
            print("Buzz")
        else:
            print(num)

def is_anagram(str1, str2):
    str1 = str1.lower().replace(" ","")
    str2 = str2.lower().replace(" ","")
    if (sorted(str1) == sorted(str2)):
        return print("Is an anagram")
    return print("Is not an anagram")

def my_is_anagram(str1, str2):
    str1 = str1.lower().replace(" ","")
    str2 = str2.lower().replace(" ","")
    if str2 == str1:
        return print("Is an anagram")
    return print("Is not an anagram")

def anagram(str1,str2):#this doesn't work if there is a capital letter
    return sorted(str1) == sorted(str2)

def first_three(a):
    front = a[:3]
    return front * 3

def first_three_list(a):
    front = a[:3]
    return front * 3

def cat_dog(string):
    catCount = string.count("cat")
    dogCount = string.count("dog")
    return catCount == dogCount

def count_hi(string):
    count = 0
    for i in range(len(string)):
        if string[i:i+2] == "hi":
            count += 1
    return count

def my_palindrome(string):
    return string==string[::-1]

def find_max_num(numList):
    var = numList[0]
    for nums in numList:
        if nums > var:
            var = nums
    return var

def find_common_elements(list1, list2):
    elementList = []
    for items in list1:
        if items in list2 and items not in elementList:
            #elementList += items #can be used on strings but not lists or tuples
            elementList.append(items) #can be used on strings, lists, and tuples
    return elementList

def find_unqiue_elements(var1):
    unique = []
    for items in var1:
        if items not in unique:
            unique.append(items)
    return unique

def calculate_average(num):
    return (sum(num)/len(num))

def count_index_of_number(num):#len() cannot create a list of integer
    return len(num)

def count_integers(num):
    return [i for i in range(num)]

def reverse_number(num):#reverse an integer
    reverse = int(str(num)[::-1])
    return reverse

a = 'radar'#string
b = 25#integer
c = ('a', 'b', 'c', 'd', 'e')#tuple
d = (0,1,4,3)
e = 'python'
f = [0,1,2,3,7,3,10,1,2,3]#list
list1 = [1,5,3,6,4,3,5,3]
g = (0,1,2,3,5)
avg= [2,2]
h = " simPle"
i = "siMple "
k = "not simple"
catdogTrue = ("cat","dog")
catdogFalse = ("bir","dog")
hihi ="hihihi"
pal="radar"
listen = "listen"
silent = "silent"
#print(generate_fibonacci(b))
#print(is_palindrome(a))
#print(reverse_string(e)) ALL wrong will return orginal string in same order
#print(is_prime(b))
#print(return_middle(c))
#print(my_revered_string(d))
#print(swap_letters(e))
#print(find_sequence(f))
#print(frizzBuzz(25,7,5))
print(is_anagram(h,k))
#print(first_three(a))
#print(first_three_list(c))
#print(cat_dog(catdogFalse))
#print(count_hi(hihi))
#print(my_is_anagram(h,i))
#print(my_palindrome(pal))
#print(find_max_num(f))
#print(find_common_elements(g,list1))
#print(calculate_average(avg))
#print(find_unqiue_elements(list1))
#print(anagram(listen,silent))
#print(count_index_of_number(b))
#print(count_integers(b))
#print(reverse_number(b))
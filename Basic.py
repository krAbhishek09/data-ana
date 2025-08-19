# # # # # a=3+4
# # # # # print(a)
# # # # age=32
# # # # if age>30:

# # # #     print(age)

# # # # print(age)


# # # # calculator
# # # num1 = float(input("enter 1st number : "))
# # # num2 = float(input("enter 2nd number:"))


# # # sum = num1+num2
# # # sub = num1-num2
# # # pro = num1*num2
# # # div = num1/num2
# # # print("sum:", sum)
# # # print("sub:", sub)
# # # print("pro:", pro)
# # # print("div:", div)


# # # a=10
# # # b=10
# # # prin
# # # t(type(a==b))


# # # f = 1
# # # n = int(input("Enter any number: "))

# # # for i in range(1, n + 1):
# # #     f *= i

# # # print("Factorial is:", f)

# # # number = float(input("Enter a number: "))
# # # if number > 0:
# # #     print("The number is positive.")
# # # elif number < 0:
# # #     print("The number is negative.")
# # # else:
# # #     print("The number is zero.")


# # #  print a number to 1 to 10
# # # for i in range (1,10):
# # #     print(i)


# # # for i in range(5):
# # #     for j in range(5):
# # #         print( "*", end=" ")
# # #     print()

# # # print("\n")


# # # for i in range(5):
# # #     for j in range(5):
# # #         print("*", end=" ")
# # #     print()


# # #  create a set
# # # my_set={1,2,3,4,5,6}
# # # print(my_set)
# # # print(type(my_set))

# # # my_set.add(9999)
# # # print(my_set)

# # # my_set.remove(9999)
# # # print(my_set)


# # #  sets:-  sets are a build-in data type in  python used to store collection of unique items .They are unordered, meaning that the elements do not follow a specific
# #         #  order , and they do not allow duplicate elemenets .Sets are useful for membership tests,eliminating duplicate entires,and performing mathematical set operation like
# #         #  union , intersection , difference ,and symmetic differnce.


# # # set1={2,3,4,5}
# # # set2={6,7,8,9}
# # # # print(set.difference(set2))
# # # #  is subset
# # # print(set1.issubset(set2))
# # # print(set1.issuperset(set2))


# # # counting unique words in text

# # # text = " Hy Thiss is Abhishek so i will do something amazing and now we do extra hard work "
# # # words=text.split()


# # # convert list of words to set to get unique words

# # # unique_words=set(words)
# # # print(unique_words)
# # # print(len(unique_words))


# # # create dict...
# # # empty_dict={"name":"Abhishek","age":"24","sex":"male"}
# # # print(empty_dict["age"])

# # # empty_dict["address"]="india"
# # # print(empty_dict)

# # # empty_dict["last name "]="Devil"
# # # print(empty_dict)

# # # del empty_dict['last name ']
# # # print(empty_dict)


# # #  create a to do list  to kep track of task
# # to_do_list=["By Gro.", "clean the house ","paybil"]


# # #  add to task
# # to_do_list.append("fixed meeting")
# # print(to_do_list)


# # # remove the task ...
# # to_do_list.remove("By Gro.")
# # print(to_do_list)


# # #  cheking if task is in the list
# # # if "paybill" in to_do_list:
# # #         print("dont forgot to pay the bills")

# # # print("To do list reming ")
# # # for task in to_do_list:
# # #         print(f"{task}")


# #  Function :- A function is a block of code that perform a specific task function
# #       functions help in organizing code ,reusing code , and imporve the readability,

# # example:--

# # num = 24
# # if num % 2 == 0:
# #         print("The number is even ")
# # else:
# #         print("The number is odd")


# def even_odd(num):
#         if num%2==0:
#                 print("The number is even")
#         else:
#                 print("The number is odd")

# #  calll the function 
# even_odd(9)

# def add(a,b):
#         return a+b

# result =add(2,4)
# print(result)


# #  default parameter:

# def greet(name):
#     print(f"hello {name}")

# greet("krish")


# def print_details(*args, **kwargs):
#     for val in args:
#         print(f"Positional arg: {val}")   # fixed with f-string

#     for key, value in kwargs.items():
#         print(f"{key}: {value}")  # fixed with f-string


# # Example call (trace)
# print_details(10, 20, 30, name="Abhishek", role="Developer")



#  return function ....


def mul(a, b):
    return a * b

mul(2, 4)
# print(mul)
print(mul(2, 4))
# print(mul(2, 4))
# print(mul(2, 4))

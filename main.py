
#
# def default_example(a=9,b=10,c=20):
#     print(a+b+c)
# default_example(1,2)
# default_example(1,2,3)
# default_example(1)
# def calculatetax(salary,percent=20):
#     taxamount=(salary*percent)/100
#     print(taxamount)
# salary=int(input("salary:"))
# percent=float(input("tax percent:"))
# calculatetax(salary)
# calculatetax(salary, percent)
# def largestnumber(*numbers):
#     m=numbers[0]
#     for num in numbers:
#         if num>m:
#             m=num
#             print("largest:",m)
            #lambda
x=lambda a : a + 10
print(x(5))
x=lambda a,b : a * b
print(x(5,6))
x=lambda a,b,c : a+b+c
print(x(5,6,7))
area=lambda r:3.14*r*r
print(area(2.3))
def myfunc(n):
    return lambda a:a*n
mydoubler=myfunc(2)
print(mydoubler(11))
tax=lambda salary:salary*20/100
salary=int(input("please enter your salary:"))
print("tax to be paid is : ")
doublenum=lambda x:x*2
a=int(input("a:"))
print(doublenum(a))
def addition(n):
    return n+4
numbers=(1,2,3,4)
result=map(addition,numbers)
print(list(result))
numebers=(1,2,3,4)
result=map(lambda x:x+x,numbers)
print(list(result))
















































































































# python dates:
#Import the datetime module and display the current date:
import datetime
x=datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A")) #"%A" обозначает дни недели.

#Create a date object:

x=datetime.datetime(2005,6,4)
print(x)
print(x.strftime("%B")) #выведет месяц в полном текстовом формате.

#Write a Python program to subtract five days from current date:
import datetime
x=datetime.datetime.now()
print(int(x.strftime("%D"))-5)
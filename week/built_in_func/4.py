#Write a Python program that invoke square root function after specific milliseconds.
from time import sleep
def mil(n,t):
    sleep(n/1000)
    print(f"Square root of {n} after {t} milliseconds is {n**0.5}")
user_input_n=int(input("Enter a number:"))
user_input_t=int(input("Enter the delay time in milliseconds:"))
mil(user_input_n, user_input_t )
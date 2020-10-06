#This program gives the whois info of the entered domain
import whois

UserInput = input("Enter a Domain: ")
w = whois.whois(UserInput)
print (w)

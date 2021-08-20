import phonenumbers as pn
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

number = "+916238985867"
number = pn.parse(number)
print(timezone.time_zones_for_number(number))
print(carrier.name_for_number(number, "en"))
print(geocoder.description_for_number(number, "en"))

#to check whether a phone number is valid
if(pn.is_valid_number(number)):
	print("The phone number is valid")
else:
	print("The phone number is not valid")
	
#to check whether a number is possible or not
if(pn.is_possible_number(number)):
	print("The phone number is possible")
else:
	print("The phone number is not possible")

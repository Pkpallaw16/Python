import phonenumbers
from phonenumbers import geocoder
from phonenumbers import timezone
number="+919035104513"
ch_number=phonenumbers.parse(number)
phoneNumber = phonenumbers.parse(number)
timeZone = timezone.time_zones_for_number(phoneNumber)
print(timeZone)
print(geocoder.description_for_number(ch_number,"en"))

from phonenumbers import carrier
service_provider=phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

# Validating a phone number
phone_number = phonenumbers.parse("+91987654321")
valid = phonenumbers.is_valid_number(phone_number)

# Checking possibility of a number
possible = phonenumbers.is_possible_number(phone_number)

# Printing the output
print(valid)
print(possible)
# pip install phonenumbers
import phonenumbers
from phonenumbers import geocoder,carrier

mobile="+9203081074466"
phone_mobile=phonenumbers.parse(mobile,"CH")

valid=phonenumbers.is_valid_number(phone_mobile)
print(valid)
print(geocoder.description_for_number(phone_mobile,"en"))

service_provider=carrier.name_for_number(phone_mobile,"en")
print(service_provider)
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

#Insert the token to contact the API
token = input("Insert the token from the Twilio API: ")

user_number = input("Insert your phone number: ")

text = input("Insert the body of the message that you want to receive: ")
account = "AC2303255323b60928ed3ea0fec8d44dfe"
client = Client(account, token)


try:
  message = client.messages.create(to=user_number, from_="+12052705757",
                                   body=text)
except TwilioRestException as e:
  print(e)

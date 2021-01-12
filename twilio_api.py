from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

user_number = input("Insert your phone number: ")

text = input("Insert the body of the message that you want to receive: ")
account = "AC2303255323b60928ed3ea0fec8d44dfe"
token = "e50e3aeb2c631614d7080d127d85d3b1"
client = Client(account, token)


try:
  message = client.messages.create(to=user_number, from_="+12052705757",
                                   body=text)
except TwilioRestException as e:
  print(e)
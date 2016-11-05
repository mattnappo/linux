from twilio.rest import TwilioRestClient
accountSID = "ACe720baa9e626dfca8768f5e7775c47ac"
authToken = "63c394a6f48ec86d6f6366fd321fbf04"
twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = "+19143713266"
myCellPhone = "+19144142874"
message = twilioCli.messages.create(body=input("Enter Message: "), from_=myTwilioNumber, to=myCellPhone)
print("Message Sent!")
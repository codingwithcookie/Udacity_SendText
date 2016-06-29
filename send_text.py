from twilio.rest import TwilioRestClient

account_sid = "hidden" # Your Account SID from www.twilio.com/console
auth_token  = "secret"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="My name is Ron Burgandy?",
    to="+11234567890",    # Replace with your phone number
    from_="+11234567890") # Replace with your Twilio number

print(message.sid)

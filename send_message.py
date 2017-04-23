from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC4d9d8e80c87dedb786decf0c170bfe4a"
# Your Auth Token from twilio.com/console
auth_token  = "fc3b29511d2af5d6ba9eabc5d3549b00"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+917013633685",
    from_="+917995637548",
    body="Hello from Vasudev!")

print(message.sid)

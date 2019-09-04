import time, os
import slack

token = os.environ.get("SLACK_TOKEN")
sc = slack.WebClient(token)


print((sc.api_call("api.test"))) 


get_info = sc.api_call("conversations.history", channel ="G0L0V05GF")
print(type(get_info)) 
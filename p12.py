import time, os
import slack

token = os.environ.get("SLACK_TOKEN")
sc = slack.WebClient(token)


print((sc.api_call("api.test"))) 


get_info = sc.api_call("conversations.history", channel ="XXXXXXX", limit=100, default=0)
print(type(get_info)) 

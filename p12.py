import time, os
import slack

token = os.environ.get("SLACK_TOKEN")
sc = slack.WebClient(token)
messages = []

#print(sc.api_call("auth.test")) 

get_info = sc.conversations_history (channel ="XXXXXXX", limit=100, default=0)
#print(get_info)
messages.extend(get_info['messages'])
#messages.sort(key = lambda message: message['ts'])
#print(messages)
response = ""
with open("out.txt",'w') as f:
  for msg in messages:
    response = 'UserId:' + msg['user']+' , Timestamp :' + msg['ts']+' , Text : msg['text']
    print(response)
    f.write(response)


from slackclient import SlackClient
import os
import array

#slack_token = os.environ["SLACK_API_TOKEN"]
#print(slack_token)
sc = SlackClient('T0GRT2TH8')
channel = "adops"
timestamp = None

def history():
        history_call = sc.api_call("channels.history",channel=channel,latest=timestamp,oldest = 0,count=1500)
        print(history_call)
        if history_call.get('ok'):
                history=history_call['messages']
                print(history)
                return history
        return []

history1=history()
for c in history1:
        text=(c['text'])
        print(text)


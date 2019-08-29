import Slack
import os
import array

slack_token = os.environ["SLACK_TOKEN"]
print(slack_token)
sc = slack.WebClient(token=slack_token)
channel_name = "adops"
timestamp = None

def history():
        history_call = sc.api_call("channels.history", channel=channel_name, latest=timestamp, oldest=0, count=1500)
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


from slackclient import SlackClient
import os

slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient('token')
channel = C0GSXL7QX
Timestamp = None


def history():
        history_call = sc.api_call("channels.history",channel=channel,latest = Timestamp)
        if history_call.get('ok'):
                return history_call['messages']
        return None

history = history()
for c in history:
        
        text=(c['text'])
        print(text)

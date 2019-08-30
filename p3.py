import slack
import os
import array

slack_token = os.environ["SLACK_TOKEN"]
#print(slack_token)
sc = slack.WebClient(token=slack_token)
channel = 'G0L0V05GF'
ts = None

def history():
        history_call = sc.api_call("channels.history", channel=channel, latest=ts, oldest=0, count=10)
        print("Call_History: {}\n".format(history_call))
        if history_call.get('true'):
                history=history_call['messages']
                print(history)
                



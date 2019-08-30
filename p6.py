
import slack
import os
import array

slack_token = os.environ["SLACK_TOKEN"]
#print(slack_token)
sc = slack.WebClient(token = slack_token)
channel = 'adops'
ts = None

while True:
       response = sc.api_call('channels.history', channel=channel, count=10,latest=ts, oldest=0)
       allmsgs = response['messages']
       print(len(allmsgs))

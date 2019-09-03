
import slack
import os
import array

slack_token = os.environ["SLACK_TOKEN"]
#print(slack_token)
sc = slack.WebClient(token=slack_token)

def list_channels():
    channels = sc.channels_list()
    for channel in channels:
        channel = 'adops'
        print(channel)

list_channels()




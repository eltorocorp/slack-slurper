
import slack
import os
import array

slack_token = os.environ["SLACK_TOKEN"]
sc = slack.WebClient(token=slack_token)

def list_channels():
    response = sc.conversations_list()
    channels = response.data["channels"]
    channels.sort(key=lambda c: c["name"])
    for channel in channels:
        print(channel["name"])

list_channels()




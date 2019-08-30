import slack
import os
import array
import json
import argparse
import os
import io
import shutil
import copy
from datetime import datetime
from time import sleep
from slacker import Slacker


slack_token = os.environ["SLACK_TOKEN"]
print(slack_token)
sc = slack.WebClient(token=slack_token)
channel_name = "adops"
slack1 = Slacker(slack_token)
#lastTimestamp = None

def getHistory(pageableObject, channelId, pageSize = 100):
    messages = []
    lastTimestamp = None

    while(True):
        response = pageableObject.history(
            channel = channelId,
            latest    = lastTimestamp,
            oldest    = 0,
            count     = pageSize
        ).body

        messages.extend(response['messages'])

        if (response['has_more'] == True):
            lastTimestamp = messages[-1]['ts'] # -1 means last element in a list
            sleep(1) # Respect the Slack API rate limit
        else:
            break

    messages.sort(key = lambda message: message['ts'])

    return messages

def list_channels():
    channels = sc.channels_list()
    for channel in channels:
    #    print(channel)
         messages1 = getHistory(sc.channels_history, channel['id'])


list_channels()

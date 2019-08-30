import slack
from time import sleep
import datetime as dt
import os

slack_token = os.environ["SLACK_TOKEN"]
sc = slack.WebClient(token = slack_token)
#print(slack_token)
channels_info = sc.api_call(channel = 'C0GSXL7QX')






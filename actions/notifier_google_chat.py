#!/usr/bin/env python
#
# Description:
#     This will help us to post a message to Google Chat.
#
import json
import requests
from st2common.runners.base_action import Action
from httplib2 import Http
from json import dumps
import ast


google_chat_webhook = "https://chat.googleapis.com/v1/spaces/AAAAvHM70pY/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=hDed1AOuUr9N5s3GaJE1GyWZpeKFaeo629oDSMw3Xlg%3D"

class Notifier_Google_Chat(Action):

    def google_post_message(self, notification_message):
        try:
            #print(ast.literal_eval(notification_message)['Hello'])
            #print("notification type : " + str(type(notification_message)))
            url = google_chat_webhook
            bot_message = {
                'text': str(ast.literal_eval(notification_message)['body']['notification_message'])}
            message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
            http_obj = Http()
            response = http_obj.request(
                uri=url,
                method='POST',
                headers=message_headers,
                body=dumps(bot_message),
            )
            print(response)
        except Exception as this_post_exception:
            print("Exception in google_post_message : " + str(this_post_exception))

    def run(self, triggers):
        try:
            # Any logic on message comes here
            self.google_post_message(triggers)
        except Exception as Notifier_Google_Chat_run_exception:
            print("Exception in Notifier_Google_Chat_run : " + str(Notifier_Google_Chat_run_exception))
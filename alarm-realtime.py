#! -*- coding: utf-8 -*-

import json
from slacker import Slacker
from mns.account import Account
from mns.mns_exception import MNSExceptionBase

from config import SLACK_TOKEN, SLACK_CHANNEL, QUEUE_NAME, END_POINT, ACCESS_KEY_ID, ACCESS_KEY_SECRET

account = Account(END_POINT, ACCESS_KEY_ID, ACCESS_KEY_SECRET)
slack = Slacker(SLACK_TOKEN)
queue = account.get_queue(QUEUE_NAME)


def run():
    while True:
        try:
            recv_msg = queue.receive_message(wait_seconds=10)
            message = json.loads(recv_msg.message_body)['message']
            print message
            if message['levelDescription'] == u'恢复正常':
                color = 'good'
            else:
                color = 'danger'
            post_slack(message['dimensions'], message['metricName'], message['expression'], color)
            queue.delete_message(recv_msg.receipt_handle)
        except MNSExceptionBase, e:
            print e.message


def post_slack(text, subject, body, color):
    obj = slack.chat.post_message(
        channel=SLACK_CHANNEL,
        text=text,
        as_user=False,
        attachments=[{"pretext": subject, "text": body, "color": color}])
    return obj.successful


if __name__ == '__main__':
    run()

#! -*- coding: utf-8 -*-

import json
from mns.account import Account
from mns.mns_exception import MNSExceptionBase
from utils import post_slack

from config import QUEUE_NAME, END_POINT, ACCESS_KEY_ID, ACCESS_KEY_SECRET

account = Account(END_POINT, ACCESS_KEY_ID, ACCESS_KEY_SECRET)
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


if __name__ == '__main__':
    run()

import json
from datetime import datetime, timedelta
from slacker import Slacker
from aliyunsdkcore.client import AcsClient
from aliyunsdkcms.request.v20170301.ListAlarmHistoryRequest import ListAlarmHistoryRequest
from aliyunsdkcms.request.v20170301.ListAlarmRequest import ListAlarmRequest
from utils import post_slack

from config import SLACK_TOKEN, AKId, AKSecret, REGION

client = AcsClient(AKId, AKSecret, REGION)
slack = Slacker(SLACK_TOKEN)


def get_alarm_history_within_one_minute():
    request = ListAlarmHistoryRequest()
    one_minute_ago = (datetime.now() - timedelta(minutes=1000)).strftime("%Y-%m-%d %H:%M:%S")
    request.set_StartTime(one_minute_ago)
    response = client.do_action_with_exception(request)
    return json.loads(response)['AlarmHistoryList']['AlarmHistory']


def get_alarm(alarm_id):
    request = ListAlarmRequest()
    request.set_Id(alarm_id)
    request.set_Namespace('acs_ecs_dashboard')
    response = client.do_action_with_exception(request)
    return json.loads(response)['AlarmList']


def run():
    alarms = get_alarm_history_within_one_minute()
    for alarm in alarms[:2]:
        print alarm
        print alarm['Name']
        print alarm['Value']
        print alarm['State']
        # print get_alarm(alarm['Id'])
        # post_slack(alarm['Name'], alarm['Value'], "warning")


if __name__ == '__main__':
    run()

from slacker import Slacker

from config import SLACK_TOKEN, SLACK_CHANNEL

slack = Slacker(SLACK_TOKEN)


def post_slack(text, subject, body, color):
    obj = slack.chat.post_message(
        channel=SLACK_CHANNEL,
        text=text,
        as_user=False,
        attachments=[{"pretext": subject, "text": body, "color": color}])
    return obj.successful

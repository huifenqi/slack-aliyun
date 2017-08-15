[program:slack-aliyun]
environment=NEW_RELIC_CONFIG_FILE=/data/www/slack-aliyun/configs/newrelic.ini
directory=/data/www/slack-aliyun/configs
command=newrelic-admin run-program /usr/bin/python /data/www/slack-aliyun/alarm-realtime.py
autostart=true
autorestart=true
stopsignal=QUIT
killasgroup=true
stdout_logfile=/data/logs/slack-aliyun/alarm-realtime.stdout.log
stderr_logfile=/data/logs/slack-aliyun/alarm-realtime.stderr.log
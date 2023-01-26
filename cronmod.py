# This file reads the cron file and modifies it
from crontab import CronTab

system_cron = CronTab(tabfile='/etc/crontabdummy', user=False)
job = system_cron[1]
system_cron.new(command='new_command', user='root')

system_cron.write()
print(system_cron)
print(job)

# Use croniter to make the time human readable

# Read the crontab file
# Modify the crontab file
# Delete jobs from the crontab file
# Add jobs to the crontab file


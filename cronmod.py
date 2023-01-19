# This file reads the cron file and modifies it
from crontab import CronTab

system_cron = CronTab(tabfile='/etc/crontab', user=False)
job = system_cron[1]
system_cron.new(command='new_command', user='root')

system_cron.write()
print(system_cron)
print(job)

# Read the cron file
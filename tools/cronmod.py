# This file reads the cron file and modifies it
from crontab import CronTab
from datetime import datetime


def get_cron_jobs():
    system_cron = CronTab(tabfile='/etc/crontab', user=False)
    crons = {}
    for indx, job in enumerate(system_cron):
        crons[indx] = {}
        schedule = job.schedule(date_from=datetime.now())
        next_exec = schedule.get_next()
        command = job.command
        comment = job.comment
        crons[indx]['next_exec'] = next_exec
        crons[indx]['command'] = command
        crons[indx]['comment'] = comment

    return crons

# Read the crontab file

# Modify the crontab file
#system_cron = CronTab(tabfile='/etc/crontab', user=False)
#job = system_cron[1]
#system_cron.new(command='new_command', user='root')
#system_cron.write()

# Delete jobs from the crontab file
# Add jobs to the crontab file


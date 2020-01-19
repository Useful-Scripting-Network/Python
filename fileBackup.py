import distutils.log
import distutils.dir_util
import schedule, time, click

src_dir = "C:\\scripts"
dst_dir = "D:\\backups\\scripts"

def job():
    click.clear()
    print(f'Copying {src_dir} to {dst_dir}')

    distutils.log.set_verbosity(distutils.log.DEBUG)
    distutils.dir_util.copy_tree(
        src_dir,
        dst_dir,
        update=1,
        verbose=1,
    )
    print(f'Done... Waiting to start again at the top of the hour...')

#set schedule
schedule.every().hour.at(":00").do(job)

#start upon launch
job()

#run schedules
while True:
    schedule.run_pending()
    time.sleep(1)

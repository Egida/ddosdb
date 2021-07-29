from django.core.management.base import BaseCommand, CommandError
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Clean and initialize celery (beat) tasks'

    def handle(self, *args, **kwargs):
        try:
            # put startup code here
            logger.info("manage.py celery command")
            # importing model classes
            from django_celery_beat.models import PeriodicTask, IntervalSchedule, CrontabSchedule

            intervals = IntervalSchedule.objects.all()
            i = 0
            for iv in intervals:
                i += 1
                logger.info("Interval {}: {}".format(i, iv))

            periodic_tasks = PeriodicTask.objects.all()
            i = 0
            for pt in periodic_tasks:
                i += 1
                logger.info("Periodic Task {}: {}".format(i, pt))

            logger.info("Deleting all ddosdb tasks")
            PeriodicTask.objects.filter(task='ddosdb.tasks.check_to_sync').delete()
            PeriodicTask.objects.filter(task='ddosdb.tasks.push_sync').delete()
            PeriodicTask.objects.filter(task='ddosdb.tasks.pull_sync').delete()

            logger.info("Creating the default ddosdb push/pull sync tasks")
            schedule, created = IntervalSchedule.objects.get_or_create(
                every=1, period=IntervalSchedule.HOURS)
            PeriodicTask.objects.get_or_create(
                interval=schedule,
                name='Remote pull sync',  # Description
                task='ddosdb.tasks.pull_sync',  # name of task.
            )
            PeriodicTask.objects.get_or_create(
                interval=schedule,
                name='Remote push sync',  # Description
                task='ddosdb.tasks.push_sync',  # name of task.
            )

            # Delete all backup cleaning tasks and create a new one
            # logger.info("Deleting all celery.backend_cleanup tasks")
            # PeriodicTask.objects.filter(task='celery.backend_cleanup').delete()

            # schedule, created = IntervalSchedule.objects.get_or_create(
            #     every=5, period=IntervalSchedule.MINUTES)
            #
            # pt = PeriodicTask.objects.get_or_create(
            #     interval=schedule,
            #     name='Cleanup task',  # Description must be unique
            #     task='celery.backend_cleanup',  # name of task.
            # )

            # logger.info("Created celery.backend_cleanup task : {}".format(pt))
        except:
            raise CommandError('Initalization failed.')

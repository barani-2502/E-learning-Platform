import datetime
from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.mail import send_mass_mail
from django.contrib.auth.models import User
from django.db.models import Count
from django.utils import timezone

class Command(BaseCommand):
    help = 'Sends an email reminder to users registered more than N days that are not enrolled into any courses yet'

    def add_arguments(self, parser):
        parser.add_argument('--days', dest='days', type=int, required=True)

    def handle(self, *args, **options):
        emails = []
        subject = 'Enroll in a course'
        date_limit = timezone.now() - datetime.timedelta(days=options['days'])

        users = User.objects.annotate(
            course_count=Count('courses_joined')
        ).filter(
            course_count=0,
            date_joined__lte=date_limit
        )

        for user in users:
            message = f"""Dear {user.first_name},
            We noticed that you didn't enroll in any courses yet.
            What are you waiting for?"""
            emails.append((subject,
                           message,
                           settings.DEFAULT_FROM_EMAIL,
                           [user.email]))

        if emails:
            send_mass_mail(emails)
            self.stdout.write(f'Sent {len(emails)} reminders')
        else:
            self.stdout.write('No users to send reminders to.')

from distutils.text_file import TextFile
from random import choices
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from multiselectfield import MultiSelectField
from django.db import models
from django.conf import settings
from datetime import datetime, timedelta
from django.utils import timezone


good = (
    (1,'커피맛'),
    (2,'인테리어'),
    (3,'디저트'),
    (4,'감성'),
    (5,'힙한'),
    (6,'집중'),
    (7,'데이트'),
    (8,'뷰'),
)


class Cafe(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    map_url = models.TextField(default='')
    telephone = models.TextField()
    opening = models.TextField()
    picture1 = ProcessedImageField(upload_to='images/', blank=True,
                        processors=[ResizeToFill(1200, 960)],
                        format='JPEG',
                        options={'quality': 100},
                        max_length=1000)
    picture2 = ProcessedImageField(upload_to='images/', blank=True,
                        processors=[ResizeToFill(1200, 960)],
                        format='JPEG',
                        options={'quality': 100},
                        max_length=1000)
    picture3 = ProcessedImageField(upload_to='images/', blank=True,
                        processors=[ResizeToFill(1200, 960)],
                        format='JPEG',
                        options={'quality': 100},
                        max_length=1000)
    score = models.IntegerField(default=0)
    hits = models.IntegerField(default=0)
    bookmarks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='bookmarksuser')
    
    #해시태그
    taste = models.IntegerField(default=0)
    interior = models.IntegerField(default=0)
    dessert = models.IntegerField(default=0)
    emotion = models.IntegerField(default=0)
    hip = models.IntegerField(default=0)
    study = models.IntegerField(default=0)
    love = models.IntegerField(default=0)
    sight = models.IntegerField(default=0)

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    picture = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(1200, 960)],
                                format='JPEG',
                                options={'quality': 80})
    picture2 = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(1200, 960)],
                                format='JPEG',
                                options={'quality': 80})
    picture3 = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(1200, 960)],
                                format='JPEG',
                                options={'quality': 80})
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    tag = MultiSelectField(choices=good, max_choices=6, blank=True)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likeuser')

    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return "방금 전"
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + "분 전"
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + "일 전"
        else:
            return False
    @property
    def is_updated(self):
        time = self.updated_at - self.created_at
        if time < timedelta(seconds=10):
            return False
        else:
            return True

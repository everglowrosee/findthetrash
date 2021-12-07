from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField('연락처', max_length=30, blank=True, null=True)
    greenpoint = models.IntegerField('초록점수', blank=True, null=True)
    coupon = models.IntegerField('쿠폰', blank=True, null=True)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.greenpoint = 10
        instance.profile.coupon = 0

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


#작업중

class PointsEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField(null=True)
    reason = models.TextField(null=True)

    def __str__(self):
        return str(self.date) + "-" + str(self.user)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        relatedEntries = PointsEntry.objects.filter(user=self.user)
        self.user.profile.greenpoint = sum([entry.points for entry in relatedEntries])
        self.user.save()



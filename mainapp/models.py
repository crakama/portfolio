from django.db import models

# Create your models here.


class Main(models.Model):
    email = models.EmailField(unique=True)
    reffered_by = models.ForeignKey("self",
                                    related_name='referral',
                                    null=True, blank=True)

    ref_id = models.CharField(max_length=120,
                              default='ReferenceID', unique=True)
    ip_address = models.CharField(max_length=120, default='IPAddress')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "{}".format(self.email)

    class Meta:
        unique_together = ("email", "ref_id", )


class FriendViews():
    email = models.OneToOneField(Main, related_name="ProfileRef")
    friends = models.ManyToManyField(Main,
                                     related_name="Friendview",
                                     null=True, blank=True)
    emailall = models.ForeignKey(Main, related_name='emailall')

from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('todo_todo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('todo_todo_update', args=(self.pk,))

    def __str__(self):
        return self.text
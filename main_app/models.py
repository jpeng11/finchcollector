from django.db import models

# Create your models here.
LastSeen = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)
class Tree(models.Model):
  name = models.CharField(max_length=50)
  height = models.IntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('trees_detail', kwargs={'pk': self.id})

class Finch(models.Model):
    name = models.CharField(max_length=50)
    scientific_name = models.CharField(max_length=100)
    mass = models.IntegerField()
    length = models.IntegerField()

    trees = models.ManyToManyField(Tree)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})

class Last(models.Model):
  date = models.DateField('The date you seen Finch')
  time = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=LastSeen,
    # set the default value for meal to be 'B'
    default=LastSeen[0][0]
  )
  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

  class Meta:
        ordering = ['-date']

  def __str__(self):
    return f"{self.get_time_display()} on {self.date}"

    
from django.db import models


# Create your models here.
class Project(models.Model):
    db_table = "projects"

    # Attributes
    name = models.CharField(max_length=100)
    image_path = models.ImageField(upload_to='images/', default='images/default-project.jpg')

    def characteristics(self):
        return ProjectCharacteristic.objects.filter(project=self.id)

    def __str__(self):
        return f"{self.name}"


class ProjectCharacteristic(models.Model):
    db_table = "project_characteristics"

    # Attributes
    text = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text}"


class Hobby(models.Model):
    db_table = "hobbies"

    # Attributes
    name = models.CharField(max_length=70)
    image_path = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.name}"
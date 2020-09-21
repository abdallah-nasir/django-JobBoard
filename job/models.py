from django.db import models

# Create your models here.

'''
# django models fields:

    -html widget
    -validation
    -db size

    '''


 #----------this is what job contains----------------------#
JOB_TYPE=(
("Full Time","Full Time"),
("Part Time","Part Time"),
)


class job(models.Model):    #table=class       
   
    title=models.CharField(max_length=100) #column
    # location

    job_type=models.CharField(max_length=15,choices=JOB_TYPE)

    description=models.TextField(max_length=1000)

    published_at=models.DateTimeField(auto_now=True)

    vacany=models.IntegerField(default=1)

    salary=models.IntegerField(default=0)

    experiance=models.IntegerField(default=1)

    #category has a realationship with a class
    category=models.ForeignKey('Category',on_delete=models.CASCADE)

    def __str__(self):        #if you want yo show the title
        return self.title


class Category(models.Model):   

    name=models.CharField(max_length=25)

        
    def __str__(self):        #if you want yo show the name
            return self.name

   





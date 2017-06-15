from django.db import models
from django.db.models import F, Sum
# Create your models here.


class Domain(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name='nom')
    code = models.CharField(max_length=5, blank=False)
    ordering_field = models.IntegerField(blank=True, verbose_name='tri')
    
    def __str__(self):
        return '{0} - {1}'.format(self.code, self.name)
    
    class Meta:
        ordering=('ordering_field',)

        
class Situation(models.Model):
    name = models.CharField(max_length=250, blank=False, verbose_name='nom')
    code = models.CharField(max_length=5, blank=False)
    ordering_field = models.IntegerField() 
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    sem1 = models.IntegerField(default=0)
    sem2 = models.IntegerField(default=0)
    sem3 = models.IntegerField(default=0)
    sem4 = models.IntegerField(default=0)
    sem5 = models.IntegerField(default=0)
    sem6 = models.IntegerField(default=0)
    
    cie1 = models.FloatField(default=0)
    cie2 = models.FloatField(default=0)
    cie3 = models.FloatField(default=0)
    cie4 = models.FloatField(default=0)
    cie5 = models.FloatField(default=0)
    cie6 = models.FloatField(default=0)
    
    practice1 = models.BooleanField(default=False)
    practice2 = models.BooleanField(default=False)
    practice3 = models.BooleanField(default=False)
    practice4 = models.BooleanField(default=False)
    practice5 = models.BooleanField(default=False)
    practice6 = models.BooleanField(default=False)
    
    evaluation = models.BooleanField(default=False)
     
    class Meta:
        ordering = ('ordering_field',)
        
    def __str__(self):
        return '{0}- {1}'.format(self.code, self.name)

    def get_total_hours_s1(self):
        return  self.cours_set.filter(semestre__name='Sem.1').aggregate(Sum(F('teaching_hours')))['teaching_hours__sum']
    
    def get_cours(self):
        foo = [self.sem1, self.sem2,self.sem3,self.sem4,self.sem5,self.sem6 ]
        return foo  
    
    def get_cie(self):   
        foo = [self.cie1, self.cie2,self.cie3,self.cie4,self.cie5,self.cie6 ]
        return foo 
    
    def get_practice(self):   
        foo = [self.practice1, self.practice2,self.practice3,self.practice4,self.practice5,self.practice6 ]
        return foo 
    
        
class Semestre(models.Model):
    name = models.CharField(max_length=10, blank=False)
    
    def __str__(self):
        return self.name
        
            
class Cours(models.Model):
    situation = models.ForeignKey(Situation, on_delete=models.CASCADE)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)    
    teaching_hours = models.IntegerField(default=0)
    kind = models.CharField(max_length=20, choices=(('Nor', 'Normal'),('CIE', 'Cours IE')))
    
    class Meta:
        ordering = ('semestre',)
        
    def __str__(self):
        return '{0}-{1} ({2})'.format(self.semestre.name, self.situation.name, self.kind)
    

                            
from django.db import models
from django.utils import timezone
import datetime
from django.utils import timezone
import os
from django.conf import settings
from django.contrib.auth.models import User
from os import listdir
from os.path import isfile, join
import numpy as np


# Create your models here.
    
class Question(models.Model):
    
    question_text = models.CharField(max_length=200)
    
    is_last = models.BooleanField(default=True)
    
    image_class = models.CharField(max_length=200, default='unknown')
    image_authenticity = models.CharField(max_length=200, default='unknown')
    
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to="polls_224")
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
class Choice(models.Model):
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    
class Voter(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  
    choice_text = models.CharField(max_length=200, default='unknown')
    
    
##############################################################

def create_questions_set():
        
        # CREATE FILENAMES LIST AND RANDOMLY SHUFFLE
        basepath = os.path.join(settings.BASE_DIR, './media/polls_224')
        allfiles = np.array([f for f in listdir(basepath) if isfile(join(basepath, f))])
        np.random.shuffle(allfiles)
        
        
        # DEFINE A QUESTION/CHOICE PROTOTYPE 
        def create_question_choice_couple(img_path, img_name, img_indx, is_last = False):
                                
            question = Question()
                                
            question.question_text = str(img_indx)+'/-This image corresponds to a...'
            question.image = img_path
            question.pub_date = timezone.now()
                                
            if 'B' in img_name: question.image_class = 'B'
            else: question.image_class = 'A'
            
            if 'fake' in img_name: question.image_authenticity = 'fake'
            else: question.image_authenticity = 'authentic'
            
            question.is_last = is_last
            
            question.save()

            for text in ['fake class A', 'fake class B',
                         'authentic class A', 'authentic class B',
                         '? class A', '? class B',
                         'fake class ?', 'authentic class ?']:
                choice = Choice()
                choice.question = question
                choice.choice_text = text
                                
                choice.save()

        # Create question set
        max_=5
		
        for idx in range(0, max_):
            
            file = allfiles[idx]
            
            if idx == max_-1:
                create_question_choice_couple(os.path.join(basepath, file), file, idx, is_last=True)
            else:
                create_question_choice_couple(os.path.join(basepath, file), file, idx, is_last=False)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

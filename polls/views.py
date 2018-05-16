from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question, Voter


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
                        pub_date__lte=timezone.now()
                        ).order_by()[:]
         
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class EndFormView(generic.DetailView):
    model = Question
    template_name = 'polls/end_form.html'
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
    
def vote(request, question_id):
    
    question = get_object_or_404(Question, pk=question_id)
    
    if Voter.objects.filter(question_id=question.id, user_id=request.user.id).exists():
        
        return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "Sorry but you already voted.",})
    
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
        v = Voter(user=request.user, question=question, choice_text = selected_choice.choice_text) 
        v.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        
        if question.is_last:
            return HttpResponseRedirect(reverse('polls:end_form', args=(question.id,)))
        else:
            return HttpResponseRedirect(reverse('polls:detail', args=(question.id+1,)))

def get_finalacc(request):
        ''' Compute the final result of the MCQ '''
        
        class_acc = 0
        authenticity_acc = 0
        total_= 0
        
        local_class_acc = 0
        local_authenticity_acc=0
        local_tot = 0
    
        for question in Question.objects.all():
            
            if Voter.objects.filter(question_id=question.id, user_id=request.user.id).exists():
                
                v = Voter.objects.get(question_id=question.id, user_id=request.user.id)
                
                if question.image_class in v.choice_text:
                    local_class_acc+= 1

                if question.image_authenticity in v.choice_text:
                    local_authenticity_acc+= 1

                local_tot += 1
            
            
            for choice in question.choice_set.all():

                if question.image_class in choice.choice_text:
                    class_acc+= choice.votes

                if question.image_authenticity in choice.choice_text:
                    authenticity_acc+= choice.votes

                total_ += choice.votes

        if total_ == 0: total_+=1
        if local_tot == 0: local_tot+=1
        
        local_class_acc = local_class_acc/local_tot
        local_authenticity_acc = local_authenticity_acc/local_tot
        
        class_acc = class_acc/total_
        authenticity_acc = authenticity_acc/total_
        
        return render(request, 'polls/fresults.html', {
            'class_acc': class_acc*100,
            'authenticity_acc': authenticity_acc*100,
            'local_class_acc': local_class_acc*100,
            'local_authenticity_acc': local_authenticity_acc*100
        })
            
   
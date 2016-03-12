from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete, pre_delete

from ..models import Question, Answer, QuestionComment, AnswerComment, Stream, Heart

# create a signal for creating notifications to followers when a user posts a question

@receiver(post_save, sender=Question)
def add_ques_to_stream(instance, created, **kwargs):
    if created:
        Stream.objects.create(type='Q', ques=instance)

# # #

@receiver(post_save, sender=Answer)
def add_ans_count_to_ques(instance, created, **kwargs):
    ques = instance.ques
    if created:
        ques.answers += 1
        ques.save()

@receiver(post_save, sender=Answer)
def add_ans_to_stream(instance, created, **kwargs):
    if created:
        Stream.objects.create(type='A', ans=instance)

# # #

@receiver(post_delete, sender=Answer)
def del_ans_count_from_ques(instance, **kwargs):
    ques = instance.ques
    ques.answers -= 1
    ques.save()

# # #

@receiver(post_save, sender=QuestionComment)
def add_comm_count_to_ques(instance, created, **kwargs):
    ques = instance.ques
    if created:
        ques.comments += 1
        ques.save()

@receiver(post_delete, sender=QuestionComment)
def del_comm_count_from_ques(instance, **kwargs):
    ques = instance.ques
    ques.comments -= 1
    ques.save()

# # #

@receiver(post_save, sender=AnswerComment)
def add_comm_count_to_ans(instance, created, **kwargs):
    ans = instance.ans
    if created:
        ans.comments += 1
        ans.save()

@receiver(post_delete, sender=AnswerComment)
def del_comm_count_from_ans(instance, **kwargs):
    ans = instance.ans
    ans.comments -= 1
    ans.save()

# # #

@receiver(post_save, sender=Heart)
def add_heart_count_to_post(instance, created, **kwargs):
    if created:
        if instance.ques:
            ques = instance.ques
            ques.hearts += 1
            ques.save()
        elif instance.ans:
            ans = instance.ans
            ans.hearts += 1
            ans.save()

@receiver(post_delete, sender=Heart)
def del_heart_count_from_post(instance, **kwargs):
    if instance.ques:
        ques = instance.ques
        ques.hearts -= 1
        ques.save()
    elif instance.ans:
        ans = instance.ans
        ans.hearts -= 1
        ans.save()

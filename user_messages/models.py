from django.db import models
from django.db.models import Max
from django.contrib.auth.models import User

class UserMessage(models.Model):
    user = models.ForeignKey(User)
    message = models.TextField(max_length=5000, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    conversation = models.ForeignKey(User, related_name="conversation")
    from_user = models.ForeignKey(User, related_name="from_user")
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return str(self.message)

    @staticmethod
    def send_message(from_user, to_user, message):
        current_user_message = UserMessage( from_user=from_user,
                                            message=message,
                                            user=from_user,
                                            conversation=to_user,
                                            is_read=True,
                                            )
        current_user_message.save()
        UserMessage(from_user=from_user,
                conversation=from_user,
                message=message,
                user=to_user).save()

        return current_user_message

    @staticmethod
    def get_conversations(user):
        conversations = UserMessage.objects.filter(
            user=user).values('conversation').annotate(
                last=Max('date')).order_by('-last')
        users = []

        for conversation in conversations:
            users.append({
                'user':User.objects.get(pk=conversation['conversation']),
                'last':conversation['last'],
                'unread':UserMessage.objects.filter(user=user,
                                                    conversation__pk=conversation[
                                                        'conversation'],
                                                    is_read=False).count(),
            })
        return users

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user_messages.models import UserMessage
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()
from .forms import MessageForm

# Create your views here.

def all_messages(request):

    context = {

    }
    return render(request, 'user_messages/all_messages.html', context)


@login_required
def inbox(request):
    conversations = UserMessage.get_conversations(user=request.user)
    active_conversation = None
    messages = None

    if conversations:
        conversation = conversations[0]
        # print(conversation)
        active_conversation = conversation['user'].username
        messages = UserMessage.objects.filter(  user=request.user,
                                                conversation=conversation['user']
                                                )
        messages.update(is_read=True)

        for conversation in conversations:
            if conversation['user'].username == active_conversation:
                conversation['unread'] = 0

    return render(request, 'user_messages/inbox.html', {
        'messages_':messages,
        'conversations':conversations,
        'active':active_conversation,
        'name':None
    })


@login_required
def new_message(request):
    print("LKJNLK")
    form = MessageForm(request.POST or None, user=request.user)
    if form.is_valid():
        print(form.errors)
        instance = form.save(commit=False)
        instance.user = form.cleaned_data.get("user")
        instance.from_user = request.user
        to_user = User.objects.get(username=instance.user)
        instance.conversation = to_user
        instance.message = form.cleaned_data.get('message')

        instance.send_message(request.user, to_user, instance.message)
        # if len(message.strip()) == 0:
        #     messages.success(request, "you can't send an empty message")
        #     return redirect('accounts:new_message')
        return redirect('accounts:new_message')
    else:
        conversations = UserMessage.get_conversations(user=request.user)
        return render(request, 'user_messages/new_message.html', {'conversations':conversations,'form':form})



@login_required
def messages(request, username):
    convo = User.objects.get(username=username)
    conversations = UserMessage.get_conversations(user=request.user)
    active_conversation = username
    messages = UserMessage.objects.filter(user=request.user,
                                      conversation__username=username)
    messages.update(is_read=True)
    for conversation in conversations:
        if conversation['user'].username == username:
            conversation['unread'] = 0

    return render(request, 'user_messages/inbox.html', {
        'messages_': messages,
        'conversations': conversations,
        'active': active_conversation,
        'name':convo,
        })









# @login_required
# def new_message(request):
#     form = MessageForm(request.POST or None, user=request.user)
#     if request.method == "POST":
#         from_user = request.user
#         to_user_username = request.POST.get("to")
#         try:
#             to_user = User.objects.get(username=to_user_username)
#         except Exception:
#             try:
#                 to_user_username = to_user_username[
#                     to_user_username.rfind('(')+1:len(to_user_username)-1]
#                 to_user = User.objects.get(username=to_user_username)
#             except Exception:
#                 return redirect('accounts:new_message')
#         message = request.POST.get('message')
#         if len(message.strip()) == 0:
#             messages.success(request, "you can't send an empty message")
#             return redirect('accounts:new_message')
#         if from_user != to_user:
#             print("message not yet sent")
#             UserMessage.send_message(from_user, to_user, message)
#             print("message sent")
#         return redirect('accounts:inbox')
#     else:
#         conversations = UserMessage.get_conversations(user=request.user)
#         return render(request, 'user_messages/new_message.html', {'conversations':conversations,'form':form})
#
#     context = {
#         'form':form,
#     }
#     return render(request, 'user_messages/new_message.html', context)
#
#

# @login_required
# def new_message(request):
#     form = MessageForm(request.POST or None, user = request.user)
#     print(form)
#     print("here")
#
#     if form.is_valid():
#         from_user = request.user
#         to_user_username = form.cleaned_data.get('to_user')
#         to_user = User.objects.get(username=to_user_username)
#         message = form.cleaned_data.get('message')
#         print("valid")
#         if len(message.strip()) == 0:
#             messages.success(request, "you can't send an empty message")
#             return redirect('accounts:new_message')
#
#         if from_user != to_user:
#             print("message not yet sent")
#             UserMessage.send_message(from_user, to_user, message)
#             print("message sent")
#         return redirect('accounts:inbox')
#
#     else:
#         conversations = UserMessage.get_conversations(user=request.user)
#         return render(request, 'user_messages/new_message.html', {'conversations':conversations,'form':form})
#
#
#

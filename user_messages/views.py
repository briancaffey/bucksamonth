from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user_messages.models import UserMessage
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()
from .forms import MessageForm, ToUserMessageForm

# Create your views here.

@login_required
def all_messages(request):
    context = {}
    return render(request, 'user_messages/all_messages.html', context)


@login_required
def inbox(request):
    conversations = UserMessage.get_conversations(user=request.user)
    active_conversation = None
    messages = None

    if conversations:
        conversation = conversations[0]
        messages = UserMessage.objects.filter(user=request.user,)
        messages.update(is_read=True)


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
        return redirect('accounts:messages', username=instance.user)
    else:
        conversations = UserMessage.get_conversations(user=request.user)
        return render(request, 'user_messages/new_message.html', {'conversations':conversations,'form':form})

@login_required
def messages(request, username):

    form = ToUserMessageForm(request.POST or None)
    convo = User.objects.get(username=username)
    conversations = UserMessage.get_conversations(user=request.user)
    active_conversation = username
    messages = UserMessage.objects.filter(user=request.user,
                                      conversation__username=username)
    messages.update(is_read=True)
    for conversation in conversations:
        if conversation['user'].username == username:
            conversation['unread'] = 0

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = convo
        instance.from_user = request.user
        to_user = User.objects.get(username=instance.user)
        instance.conversation = to_user
        instance.message = form.cleaned_data.get('message')

        instance.send_message(request.user, to_user, instance.message)
        form = ToUserMessageForm()

    return render(request, 'user_messages/inbox.html', {
        'messages_': messages,
        'conversations': conversations,
        'active': active_conversation,
        'name':convo,
        'form':form,
        })

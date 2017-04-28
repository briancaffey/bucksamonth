from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.models import User
from services.models import Subscription
from accounts.models import UserProfile
from friends.models import Friend

# from services.models import Comment

from accounts.forms import UpdateSubscriptionForm

from django.views.generic import View, TemplateView, DetailView, DeleteView
from django.views.generic.edit import UpdateView



def view_profile(request, username):
	if request.user.username == username:
		return HttpResponseRedirect(reverse('accounts:profile'))
	#get the user we are looking at
	person = get_object_or_404(User, username=username)
	#get the userprofile
	person = person.userprofile
	#get the subscriptions for
	all_subscriptions = Subscription.objects.filter(user=person)
	private = len(all_subscriptions.filter(private=True))
	subscriptions = all_subscriptions.filter(private=False, wishlist=False)
	bucksamonth = sum([subscription.bucksamonth for subscription in all_subscriptions])

	person_friend_object, person_created = Friend.objects.get_or_create(current_user=person)
	user_friends = [friend for friend in person_friend_object.users.all()] #if friend != request.user.userprofile
	follower_count = len(user_friends)

	#get logged_in_user friend model -- this was causing errors for anonymous users

	#initialize this variable for anonymous users
	friend = False

	context = {
		'person':person,
		'subscriptions':subscriptions,
		'bucksamonth':bucksamonth,
		'private':private,
		'friend':friend,
		'follower_count':follower_count,
		'user_friends':user_friends,
	}


	if request.user.is_authenticated():
		friend_object, created = Friend.objects.get_or_create(current_user=request.user.userprofile)
		friends = [friend for friend in friend_object.users.all()] # if friend != request.user.userprofile
		if person in friends:
			friend = True
		else:
			friend = False

	context['friend'] = friend
	


	return render(request, 'users/user_profile_view.html', context)



class UserProfileView(TemplateView):

	template_name = 'users/user_profile_view.html' #'users/user_profile_view.html'

	def get_context_data(self, **kwargs):
		context = super(UserProfileView, self).get_context_data(**kwargs)
		context['user_'] = User.objects.get(id=self.kwargs['pk'])
		context['user_p'] = UserProfile.objects.get(user=context['user_'])
		context['subscriptions'] = Subscription.objects.filter(user=context['user_p'], wishlist=False, private=False)
		private = Subscription.objects.filter(user=context['user_p'], wishlist=False, private=True)
		private = private.count()


		context['private'] = private
		context['wishlist'] = Subscription.objects.filter(user=context['user_p'], wishlist=True)
		context['bucksamonth'] = sum([subscription.bucksamonth for subscription in context['subscriptions']])
		print(context)
		return context



	# 	bucksamonth = Subscription.objects.filter(user=request.user.userprofile)
	# bucksamonth = sum([subscription.bucksamonth for subscription in subscriptions])


class SubscriptionUpdate(UpdateView):
	model = Subscription
	#fields = ['cc_nickname', 'bucksamonth', 'date_created', 'wishlist']
	form_class = UpdateSubscriptionForm
	template_name_suffix = '_update_form'
	success_url = '/account/profile/'

	def get_context_data(self, **kwargs):
		context = super(SubscriptionUpdate, self).get_context_data(**kwargs)
		context['subscription'] = self.object
		return context

	# def get_object(self, *args, **kwargs):
	# 	obj = super(SubscriptionUpdate, self).get_object(*args, **kwargs)
	# 	if obj.user != self.request.user:
	# 		raise HttpResponseForbidden() #or Http404
	# 	return obj

class SubscriptionDeleteView(DeleteView):

	model = Subscription
	success_url = '/account/profile/'

	def get_object(self, queryset=None):

		obj = super(SubscriptionDeleteView, self).get_object()
		if not obj.user.user.id == self.request.user.id:
			raise Http404
		obj.delete()
		return obj

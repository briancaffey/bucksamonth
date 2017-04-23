from django.shortcuts import render, get_object_or_404
from django.http import Http404

from django.contrib.auth.models import User
from services.models import Subscription
from accounts.models import UserProfile
# from services.models import Comment

from accounts.forms import UpdateSubscriptionForm

from django.views.generic import View, TemplateView, DetailView, DeleteView
from django.views.generic.edit import UpdateView



def view_profile(request, pk):
	person = get_object_or_404(UserProfile, pk=pk)
	all_subscriptions = Subscription.objects.filter(user=person.user.id)
	private = all_subscriptions.filter(private=True)
	subscriptions = all_subscriptions.filter(private=True, wishlist=False)
	bucksamonth = sum([subscription.bucksamonth for subscription in all_subscriptions])
	context = {
		'person':person,
		'subscriptions':subscriptions,
		'bucksamonth':bucksamonth,
		'private':private,
	}
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

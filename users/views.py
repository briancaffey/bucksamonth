from django.shortcuts import render
from django.views.generic import View, TemplateView, DetailView
from django.contrib.auth.models import User
from services.models import Subscription
from accounts.models import UserProfile
from django.views.generic.edit import UpdateView

from django.views.generic import DeleteView
from django.http import Http404

# Create your views here.
class UserProfileView(TemplateView):
	
	template_name = 'users/user_profile_view.html' #'users/user_profile_view.html'

	def get_context_data(self, **kwargs):
		context = super(UserProfileView, self).get_context_data(**kwargs)
		context['user_'] = User.objects.get(id=self.kwargs['pk'])
		context['user_p'] = UserProfile.objects.get(user=context['user_'])
		context['subscriptions'] = Subscription.objects.filter(user=context['user_p'])
		context['bucksamonth'] = sum([subscription.bucksamonth for subscription in context['subscriptions']])
		print(context)
		return context



	# 	bucksamonth = Subscription.objects.filter(user=request.user.userprofile)
	# bucksamonth = sum([subscription.bucksamonth for subscription in subscriptions])


class SubscriptionUpdate(UpdateView):
	model = Subscription
	fields = ['cc_nickname', 'bucksamonth', 'date_created']
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
		print("OK")
		if not obj.user.user.id == self.request.user.id:
			raise Http404
		print("seems ok")
		obj.delete()
		return obj




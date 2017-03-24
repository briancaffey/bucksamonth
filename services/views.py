from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View, TemplateView, DetailView, FormView
from services.models import Service, Comment
from services.forms import AddServiceForm
from .forms import AddCommentForm
from django.urls import reverse
from django.http import HttpResponseForbidden
from django.views.generic.detail import SingleObjectMixin
from django import forms
from django.views import View

# Create your views here.


class HomeView(View):
	def get(self, request, *args, **kwargs):
		services = Service.objects.all()
		return render(request, 'services/home.html', {'services':services})

def services(request):
	services = Service.objects.all()
	return render(request, 'services/services.html', {'services':services})


class AddServiceView(TemplateView):
	template_name = 'services/add_service.html'

	def get(self, request):
		form = AddServiceForm()

		args = {'form':form}
		return render(request, self.template_name, args)

	def post(self, request):
		form = AddServiceForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()

			return redirect('services:services')

		args = {'form':form,}
		return render(request, self.template_name, args)

class ServiceView(DetailView):
	template_name = 'services/service_detail.html'
	model = Service


	def get_context_data(self, **kwargs):
		context = super(ServiceView, self).get_context_data(**kwargs)
		context['form'] = AddCommentForm()
		context['comments'] = Comment.objects.filter(service=self.kwargs['pk'])
		return context


class ServiceComment(SingleObjectMixin, FormView):
	template_name = 'services/service_detail.html'
	form_class = AddCommentForm
	model = Service

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return HttpResponseForbidden()
		self.object = self.get_object()
		return super(ServiceComment, self).post(request, *args, **kwargs)

	def form_valid(self, form):
		#added in some extra bits here
		form.instance.user = self.request.user.userprofile
		form.instance.service = self.get_object()
		form.save()
		return super(ServiceComment, self).form_valid(form)

	def get_success_url(self):
		return reverse('services:service', kwargs={'pk': self.object.pk})
	
class ServiceDetailView(TemplateView):

	def get(self, request, *arg, **kwargs):
		view = ServiceView.as_view()
		return view(request, *arg, **kwargs)

	def post(self, request, *args, **kwargs):
		view = ServiceComment.as_view()
		return view(request, *args, **kwargs)




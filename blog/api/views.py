from django.shortcuts import render, get_object_or_404, redirect

from ..models import Post

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions



class PostLikeAPIToggle(APIView):
	authentication_classes = (authentication.SessionAuthentication,)
	permission_classes = (permissions.IsAuthenticated,)

	def get(self, request, slug=None, format=None):
		print("API Working")
		obj = get_object_or_404(Post, slug=slug)
		url_ = obj.get_absolute_url()
		user = self.request.user
		updated = False
		liked = False
		if user.is_authenticated():
			if user in obj.likes.all():
				liked = False
				obj.likes.remove(user)
			else:
				liked = True
				obj.likes.add(user)
			updated = True
		data = {
			'update':updated,
			'liked':liked,
		}

		return Response(data)

from django.contrib import admin
from accounts.models import UserProfile



admin.site.site_header = '💸 bucksamonth 📅 // 🗄📂📤👩🏻 administration 👱🏼🔏📈💰'

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'emoji', 'twitter', 'user_info')

	def user_info(self, obj):
		return obj.description
	def twitter(self, obj):
		return obj.twitter
	def emoji(self, obj):
		return obj.emoji

admin.site.register(UserProfile, UserProfileAdmin)

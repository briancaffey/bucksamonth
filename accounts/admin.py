from django.contrib import admin
from accounts.models import UserProfile



admin.site.site_header = '💸 bucksamonth 📅 // 🗄📂📤👩🏻 administration 👱🏼🔏📈💰'

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'user_info', 'twitter')

	def user_info(self, obj):
		return obj.description
	def twitter(self, obj):
		return obj.twitter

admin.site.register(UserProfile, UserProfileAdmin)
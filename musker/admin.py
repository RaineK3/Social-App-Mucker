from django.contrib import admin
from django.contrib.auth.models import Group,User
from .models import Profile, Meep

#unregister Groups
admin.site.unregister(Group)

#mix profile info into user info
class PorfileInline(admin.StackedInline):
	model = Profile

#extend User Model 
class UserAdmin(admin.ModelAdmin):
	model = User 
	#just display username fields on admin page
	fields = ["username"]
	inlines = [PorfileInline]

#unregister initial user
admin.site.unregister(User)
#register user and profile
admin.site.register(User, UserAdmin)
#admin.site.register(Profile)

#register Meeps
admin.site.register(Meep)



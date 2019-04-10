from django.contrib import admin
from .models import Check

# Register your models here.
class CheckAdmin(admin.ModelAdmin):
	fields=[
		'user',
		'checkIn',
		'checkOut',
	]

	readonly_fields = ['checkIn',]

	class Meta:
		model = Check

admin.site.register(Check, CheckAdmin)

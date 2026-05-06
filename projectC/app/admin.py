from django.contrib import admin
from .models import User, Client, Provider, ServiceCategory, JobRequest, JobAssignment, Payment, Review

admin.site.register(User)
admin.site.register(Client)
admin.site.register(Provider)
admin.site.register(ServiceCategory)
admin.site.register(JobRequest)
admin.site.register(JobAssignment)
admin.site.register(Payment)
admin.site.register(Review)
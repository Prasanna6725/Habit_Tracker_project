from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import Habit  # 👈 Replace with your actual model

class MyAdminSite(AdminSite):
    site_header = "Habit Tracker Admin"
    site_title = "Habit Tracker Portal"
    index_title = "Welcome to Habit Tracker"

    def each_context(self, request):
        context = super().each_context(request)
        context['custom_css'] = 'admin/css/custom_admin.css'
        return context

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        return urls

admin_site = MyAdminSite()

admin_site.register(Habit)  # 👈 This line needs your actual model

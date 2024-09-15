from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # path('',views.student,name='student'),
    path('profile/',views.student_profile,name='student_profile'),
    path('profileedit/',views.profile_edit,name='profile_edit'),
    path('icard/',views.icard,name='student_icard'),
    path('passwordchange/',views.student_passchange,name='student_passchange'),
    path('notifications/',views.student_notifications,name='student_notifications'),
    path('fine/',views.student_fine,name='student_fine'),
    path('pdf/',views.student_pdf,name='student_pdf'),
    path('logout/',views.student_logout,name='student_logout'),
]
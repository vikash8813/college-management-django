from django.urls import path
from django.views.generic import TemplateView
from . import views
urlpatterns=[
    path('profile/',views.teacher_profile,name='teacher_profile'),
    path('logout/',views.teacher_logout,name='teacher_logout'),
    path('profileedit/',views.profile_edit,name='teacher_profileedit'),
    path('icard/',views.icard,name='teacher_icard'),
    path('passwordchange/',views.teacher_passchange,name='teacher_passchange'),
    path('pdfs/',views.teacher_pdf,name='teacher_pdf'),
    path('addpdfs/',views.teacher_addpdf,name='addpdf'),
    path('notifications/',views.notifications,name='addnotification'),
    path('addmessages/',views.message,name='addmessages'),
    path('studentinfo/',views.studentsedit,name='studentinfo'),
    path('addevents/',views.events,name='addevents'),
    path('addcourse/',views.addcourse,name='addcourse'),
    path('pdf_delete/<int:id>/',views.pdf_delete,name='pdf_delete'),
    path('notifydelete/<int:id>/',views.notify_delete,name='notify_delete'),
    path('eventdelete/<int:id>/',views.event_delete,name='event_delete'),
    path('coursedelete/<int:id>/',views.course_delete,name='course_delete'),
    path('messa/<int:id>/',views.message_delete,name='message_delete'),
    path('studentedit/<slug:username>/',views.student_profile_edit,name='student_profile_edit'),
    path('addfine/<slug:username>/',views.student_fine,name='student_add_fine'),
]
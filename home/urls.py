from django.urls import path
from django.views.generic import TemplateView
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    # path('event/',views.events),
    path('event/<int:id>/',views.events,name='events'),
    path('course/<int:id>/',views.course,name='courses'),
    path('admission/',views.admission,name='admission'),
    # path('forgotpass/',views.forgot_password,name='forgotpass'),
    # path('changeforgot/',views.changeforgot,name='changeforgot'),
    path('vcmsg/',TemplateView.as_view(template_name='home/vcmsg.html'),name='vcmsg'),
    path('about/',TemplateView.as_view(template_name='home/about.html'),name='about'),
    path('contact/',TemplateView.as_view(template_name='home/contact.html'),name='contact'),
    path('privacy/',TemplateView.as_view(template_name='home/privacy.html'),name='privacy'),
    # path('gallery/',TemplateView.as_view(template_name='home/gallery.html'),name='gallery'),
    path('register/',views.register_attempt,name='register'),
    path('gallery/',views.gallery,name='gallery'),
    path('login/',views.login_attempt,name='login'),
    path('login/<auth_token>' , views.verify , name="verify"),
    path('feedback/',views.feedbackdata,name='feedback'),
    path('staffs/',views.staffs,name='staffs'),
]
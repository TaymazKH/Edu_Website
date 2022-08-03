from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home_page),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('home/', views.home_page, name='home'),
    path('contactus/', views.send_feedback, name='contactUs'),
    path('feedbacksent/', views.feedback_sent, name='feedbackSent'),
    path('profile/', views.show_profile, name='profile'),
    path('setting/', views.edit_profile, name='setting'),
    path('panel/', views.show_panel, name='panel'),
    path('new_course/', views.new_course, name='newCourse'),
    path('all_courses/', views.show_all_courses, name='allCourses'),

]
# path('vote/<int:question_id>', views.vote, name='vote')

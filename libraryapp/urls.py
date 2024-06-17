from django.contrib import admin
from django.urls import include, path
from django.urls import path
from libraryapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views 



urlpatterns = [
    path('', views.home, name='home'),
    path('main', views.main, name='main'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('student_details', views.student_details, name='student_details'),
    path('staff_display', views.staff_display, name='staff_display'),
    path('login_entry', views.login_entry, name='login_entry'),
    path('login_failure', views.login_failure, name='login_failure'),
    path('logout', views.logout, name='logout'),
    path('login_submit', views.login_submit, name='login_submit'),
    path('staff_dashboard', views.staff_dashboard, name='staff_dashboard'),
    path('student_dashboard', views.student_dashboard, name='student_dashboard'),
    path('book_issue', views.book_issue, name='book_issue'),
    path('book_list', views.book_list, name='book_list'),
    path('book', views.book, name='book'),
    path('Book_entry', views.Book_entry, name='Book_entry'),
    path('submit', views.submit, name='submit'),
    path('registration', views.register, name='register'),
    path('registration_2', views.registration_2, name='registration_2'),
    path('display', views.display, name='display'),
    path('student_displaybook', views.student_displaybook, name='student_displaybook'),
    path('select_book', views.select_book, name='select_book'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('choose/<int:id>', views.choose, name='choose'),
    path('issued_book', views.issued_book, name='issued_book'),
    path('issue_submit', views.issue_submit, name='issue_submit'),
    path('contact_submit', views.contact_submit, name='contact_submit'),
   
    
    
    
    # path('forgot_password', views.forgot_password, name='forgot_password'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete')
   

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

  
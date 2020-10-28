from django.urls import path
from .views import StaffListView, StaffView, TopStaffView

urlpatterns = [
    path('', StaffListView.as_view()),
    path('topstaff', TopStaffView.as_view()),
    path('<pk>', StaffView.as_view()),
]
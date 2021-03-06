from django.urls import path
from match import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('member', views.MemberList.as_view()),
    path('club', views.ClubList.as_view()),
    # path('player/<int:id>/', views.PlayerDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

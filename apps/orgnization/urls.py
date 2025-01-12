from django.urls import path, include

from .views import OrgView, AddUserAskView

urlpatterns = [
    path('list/', OrgView.as_view(), name="org_list"),
    path('add_ask/', AddUserAskView.as_view(), name="add_ask"),
]
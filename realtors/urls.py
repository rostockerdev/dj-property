from django.urls import path
from realtors.views import realtor_detail, realtor_list

app_name = "realtors"

urlpatterns = [
    path("", realtor_list.realtor_list_view, name="realtor-list"),
    path(
        "<str:realtor_slug>",
        realtor_detail.RealtorDetailView.as_view(),
        name="realtor-detail",
    ),
]

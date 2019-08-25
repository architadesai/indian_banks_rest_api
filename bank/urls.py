from django.urls import path

from bank.views import ShowBankDetailFromIFSCView
from .views import ListBranchesView

from rest_framework import routers
router = routers.DefaultRouter()


urlpatterns = [
    path('branches', ListBranchesView.as_view(), name='branches-all'),
    path('banks/<str:ifsc>', ShowBankDetailFromIFSCView.as_view(), name='banks-detail'),
]

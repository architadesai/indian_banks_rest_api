from django.utils.text import slugify
from rest_framework import generics, permissions

from bank.serializers import BranchesBankSerializer
from .models import Branches, Banks


class ListBranchesView(generics.ListCreateAPIView):
    serializer_class = BranchesBankSerializer
    queryset = Branches.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        bank_name = slugify(self.request.query_params.get('bank').lower())
        bank_city = self.request.query_params.get('city').upper()
        bank = Banks.objects.get(slug=bank_name)
        bank_id = bank.id
        branches = Branches.objects.filter(bank=bank_id).filter(city=bank_city)
        return branches


class ShowBankDetailFromIFSCView(generics.RetrieveAPIView):
    serializer_class = BranchesBankSerializer
    lookup_field = 'ifsc'
    queryset = Branches.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)

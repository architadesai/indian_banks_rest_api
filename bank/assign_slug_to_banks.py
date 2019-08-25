from django.template.defaultfilters import slugify

from bank.models import Banks

banks = Banks.objects.all()

for bank in banks:
    bank.slug = slugify(bank.name)
    bank.save()

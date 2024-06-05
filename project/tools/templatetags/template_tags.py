from tools.models import SettingsSite
from django.core.exceptions import ObjectDoesNotExist

def settings(request):
    try:
        return {'setting': SettingsSite.objects.last()}
    except ObjectDoesNotExist:
        pass

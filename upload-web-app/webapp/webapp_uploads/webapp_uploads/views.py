#import logging
from django.http import HttpResponse
from django.views.decorators.http import require_POST

#logger = logging.getLogger('django')

@require_POST
def upload_file(request):
#    real_ip = request.META.get('HTTP_X_REAL_IP')
#    if real_ip:
#        logger.debug(f"X-Real-IP: {real_ip}")
    return HttpResponse("File Uploaded Successfully")

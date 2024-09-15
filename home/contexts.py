from .models import Course

def coursecontext(request):
    courses=Course.objects.order_by('-id')
    return {'courses':courses}
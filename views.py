from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Facultad, Usuario

def index(request):
    latest_question_list = Facultad.objects.order_by('-fct_id')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'intranet/index.html', context)

def login(request):
    pasaporte = request.POST.get('pasaporte')
    password = request.POST.get('password')
    persona = Usuario(usu_usuario = pasaporte, usu_password = password)
    return render(request, 'intranet/portada/login.html')
    if persona is not None:
        login(request, persona)
        # Redirect to a success page.
    else:
        print('error')

def calendario(request):
    return render(request, 'intranet/calendario/calendar.html')

def detail(request, fct_id):
    facultad = get_object_or_404(Facultad, pk=fct_id)
    return render(request, 'intranet/detail.html', {'facultad': facultad})

def results(request, fct_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % fct_id)

def vote(request, fct_id):
    return HttpResponse("You're voting on question %s." % fct_id)    
from django.shortcuts import render
from django.http import HttpResponse
from models import Contenido
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def recurso_get(request):
        htmlBody = '<html><body>'
        htmlBody += 'Introduzca un contenido<br/>'
        htmlBody += '<form method="POST" action="">'
        htmlBody += '<input type = "text" name="ULRs">'
        htmlBody += '<input type ="submit" value="Enviar">'
        htmlBody += '</form></body></html>'
        return HttpResponse(htmlBody)

@csrf_exempt
def recurso(request,identificador):
    if request.method == 'GET':
        try:
            objeto = Contenido.objects.get(id= identificador)
        except Contenido.DoesNotExist:
            return HttpResponse('no se ha encontrado contenido para este ID')
        ans = 'el contenido para este ID es: '+ objeto.contenido
        htmlBody = '<html><body><br/>'
        htmlBody += ans+'<br/>'
        htmlBody +='<br/><br/>'
        htmlBody += 'Introduzca un contenido<br/>'
        htmlBody += '<form method="POST" action="">'
        htmlBody += '<input type = "text" name="ULRs">'
        htmlBody += '<input type ="submit" value="Enviar">'
        htmlBody += '</form></body></html>'
        return HttpResponse(htmlBody)
    elif request.method == 'POST':#Aqui si le llega un POST
        wc = request.body.split('=')[1]
        #wc = request.POST.get('contenido')
        c = Contenido(contenido = wc)
        c.save()
        htmlBody = '****<br/>'
        htmlBody += 'el contenido enviado es: '+wc+'<br/>'
        htmlBody += '****'
        return HttpResponse(htmlBody)
    else:
        return HttpResponse('no hay llegado ni un POST ni un PUT')
def error(request):
    return HttpResponse('HA HABIDO UN ERROR <br/> escriba /recurso/-numero-/')

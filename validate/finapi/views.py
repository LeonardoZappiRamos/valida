from django.shortcuts import render
import requests

def lista_ativos(request):
  "Lista de Ativos na Bolsa"
  req = requests.get('https://brapi.dev/api/quote/list')
  context = {'ativos': req.text}
  return render(request, 'index.html', context,context)
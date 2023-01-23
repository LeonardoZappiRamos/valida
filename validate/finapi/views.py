from django.shortcuts import render
import requests

from . import tables

def lista_ativos(request):
  "Lista de Ativos na Bolsa"
  req = requests.get('https://brapi.dev/api/quote/list')
  
  # Instacia Tabela 
  stocks = req.json()
  stocktable = tables.StockTable(stocks['stocks'], order_by='-close')
  
  # Mudanças na Tabela 
  stocktable.order_by = request.GET.get('sort', 'defaultOrderField') 
  stocktable.paginate(page=request.GET.get("page", 1), per_page=10)
  
  # Contexto
  context = {
    'stocks': stocktable
  }
  
  return render(request, 'finapi/index.html', context)
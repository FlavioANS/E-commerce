from re import template
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from . import models
from django.http import HttpResponse


class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'


class DetalhesProduto(View):
    pass


class Adicionar(View):
    pass


class Remover(View):
    pass


class Carrinho(View):
    pass


class Finalizar(View):
    pass

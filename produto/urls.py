from django.urls import path
from .  import views

app_name = 'produto'

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name="lista" ),
    path('<slug>', views.DetalhesProduto.as_view(), name="detalhe" ),
    path('adicionar/', views.Adicionar.as_view(), name="adicionar" ),
    path('remover/', views.Remover.as_view(), name="remover" ),
    path('carrinho/', views.Carrinho.as_view(), name="carrinho" ),
    path('finalizar/', views.Finalizar.as_view(), name="finalizar" ),
]

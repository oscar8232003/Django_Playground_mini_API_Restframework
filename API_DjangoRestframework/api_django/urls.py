from django.urls import path
from .apiviews import ProductoList, ProductoDetalle, \
                      SubCategoriaSave, CategoriaList,CategoriaDetalle, SubCategoriaList, \
                      SubCategoriaAdd, UserCreate, LoginView

urlpatterns = [
    path('productos/', ProductoList.as_view(), name="listar_productos"),
    path('productos/<int:pk>', ProductoDetalle.as_view(), name="producto_detalle"),
    path('categorias/', CategoriaList.as_view(), name="categoria_save"),
    path('categorias/<int:pk>', CategoriaDetalle.as_view(), name="categoria_list"),
    path('categorias/<int:pk>/subcategorias/', SubCategoriaList.as_view(), name="sc_list"),
    path('categorias/<int:cat_pk>/addsubcategorias/', SubCategoriaAdd.as_view(), name="sc_add"),
    path('usuarios/', UserCreate.as_view(), name="usuario_crear"),
    path('login/', LoginView.as_view(), name="login"),
]
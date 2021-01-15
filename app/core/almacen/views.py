from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from core.almacen.models import Product
# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = 'inicio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Inicio' 
        return context


"""

class index(ListView):
  model = Mensaje
  second_model = Grupos
  template_name = 'agenda/index.html'
  paginate_by = 40

    def get_context_data(self, **kwargs):
        context = super(customerUpdateView,elf).get_context_data(**kwargs)
        context['obj1'] = TuModelo.objects.all()
        context['obj2'] = TuOtroModelo.objects.filter(tipo='eventos')
        return context

"""
class ProductListView(ListView):
    model = Product
    #paginate_by = 100  # if pagination is desired solo en listview aplica esto
    template_name='listProductAlmacen.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Productos'
        return context    
    
from django.shortcuts import render, get_object_or_404
from .models import Menu, Tipo_comida, Plato_extra
from django.contrib.auth.decorators import login_required

# Create your views here.
def carta(request):
    tipo = request.GET.get('tipo_comida')

    if tipo == None:
        menus = Menu.objects.select_related('id_tipo_carta').all()
    else:
        menus = Menu.objects.filter(id_tipo_carta__nombre=tipo)

    tipos_comida = Tipo_comida.objects.all()

    context = {
        'menus': menus,
        'tipos_comida': tipos_comida,
        'tipo_comida_seleccionada': tipo
    }

    return render(request, 'viewCarta.html', context)
@login_required
def detalle_plato(request, tipo_comida, id):
    informacion_plato = get_object_or_404(Menu, id_tipo_carta__nombre=tipo_comida, id_menu=id)

    informacion_extras = Plato_extra.objects.all()
    context = {
        'informacion_plato': informacion_plato,
        'informacion_extras': informacion_extras
    }

    return render(request, 'viewInformacionCarta.html', context)


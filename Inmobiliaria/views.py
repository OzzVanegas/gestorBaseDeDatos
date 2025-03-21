from django.utils import timezone
from django.shortcuts import  render,redirect
from .models import Property, State, City , District , Owner,TyprOwner,PropertyType,TransactionType
from .forms import DeptForm, CityForm, DisctictForm, OwnerForm,OwnerTyperForm
from .forms import PropertyTyperForm ,TransactionForm ,PropertyForm
from django.core.paginator import Paginator

# Create your views here.

def inicio (request):
    return render(request, 'paginas/Inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

#--------------------------------------------------------------
#Gestion de departamentos
def crearDepto(request):
    formu = DeptForm(request.POST or None,request.FILES or None)
    if formu.is_valid():
        formu.save()
        return redirect('listar_departamentos')
    return render(request, 'properties/crearDepto.html', {'formulario': formu})

def listar_departamentos(request):
    departamentos = State.objects.all() 
    paginator = Paginator(departamentos, 8) 
    page_number = request.GET.get('page')
    departamentos = paginator.get_page(page_number)
    return render(request, 'properties/indexDepto.html', {'departamentos': departamentos})

def editarDepto(request,id):
    departamento_editar = State.objects.get(id=id)
    formulario1 =DeptForm(request.POST or None,request.FILES or None, instance=departamento_editar)
    if formulario1.is_valid() and request.POST:
        formulario1.save()
        return redirect('listar_departamentos')
    return render(request, 'properties/editarDepto.html', {'formulario': formulario1})

def borrarDepto(request, id):
    Depto_delete = State.objects.get(id=id) 
    Depto_delete.delete()  
    return redirect('listar_departamentos')
#--------------------------------------------------------------
#Gestion de Ciudades

def crearCiudad(request):
    formu = CityForm(request.POST or None,request.FILES or None)
    if formu.is_valid():
        formu.save()
        return redirect('listar_ciudades')
    return render(request, 'properties/crearCity.html', {'formulario': formu})

def listar_ciudades(request):
    ciudades = City.objects.all()  # Obtener todos los departamentos
    return render(request, 'properties/indexCity.html', {'ciudades': ciudades})

def editarCiudad(request,id):
    ciudad_editar = City.objects.get(id=id)
    formulario =CityForm(request.POST or None,request.FILES or None, instance=ciudad_editar)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('listar_ciudades')
    return render(request, 'properties/editarCity.html', {'formulario': formulario})

def borrarCiudad(request, id):
    ciudad_delete = City.objects.get(id=id) 
    ciudad_delete.delete()  
    return redirect('listar_ciudades')

#--------------------------------------------------------------
#Gestion de Distritos
def crearDistrito(request):
    formu = DisctictForm(request.POST or None,request.FILES or None)
    if formu.is_valid():
        formu.save()
        return redirect('listar_distritos')
    return render(request, 'properties/crearDistrict.html', {'formulario': formu})

def listar_distritos(request):
    distritos = District.objects.all()
    paginator = Paginator(distritos, 12)  # Muestra cant. registros por página
    page_number = request.GET.get('page')
    distritos = paginator.get_page(page_number)
    return render(request, 'properties/indexDistrict.html', {'distritos': distritos})

def editarDistrito(request, id): 
     distrito_editar = District.objects.get(id=id)
     formulario = DisctictForm(request.POST or None, request.FILES or None, instance=distrito_editar)
     if formulario.is_valid() and request.POST:
         formulario.save()
         return redirect('listar_distritos')
     return render(request, 'properties/editarDistrict.html', {'formulario': formulario})

def borrarDistrito(request, id):        
     distrito_delete = District.objects.get(id=id) 
     distrito_delete.delete()  
     return redirect('listar_distritos')
#--------------------------------------------------------------
#Gestion de Tipos de Propietarios

def crearTipoPropietario(request):
    formu = OwnerTyperForm(request.POST or None,request.FILES or None)
    if formu.is_valid():
        formu.save()
        return redirect('listar_tiposPropietarios')
    return render(request, 'properties/crearTypeOwner.html', {'formulario': formu})

def listar_tipos_propietarios(request):
    tipos_propietarios = TyprOwner.objects.all()
    return render(request, 'properties/indexTypeOwner.html', {'tipos_propietarios': tipos_propietarios})    

def editarTipoPropietario(request, id):
    tipo_propietario_editar = TyprOwner.objects.get(id=id)
    formulario = OwnerTyperForm(request.POST or None, request.FILES or None, instance=tipo_propietario_editar)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('listar_tiposPropietarios')
    return render(request, 'properties/editarTypeOwner.html', {'formulario': formulario})

def borrarTipoPropietario(request, id):
    tipo_propietario_delete = TyprOwner.objects.get(id=id)
    tipo_propietario_delete.delete()
    return redirect('listar_tiposPropietarios')

#--------------------------------------------------------------
#Gestion de Propietarios

def crearPropietario(request):
    formu = OwnerForm(request.POST or None,request.FILES or None)
    if formu.is_valid():
        formu.save()
        return redirect('listar_propietarios')
    return render(request, 'properties/crearOwner.html', {'formulario': formu})

def listar_propietarios(request):
    propietarios = Owner.objects.all()
    paginator = Paginator(propietarios, 12)  # Muestra cant. registros por página
    page_number = request.GET.get('page')
    propietarios = paginator.get_page(page_number)
    return render(request, 'properties/indexOwner.html', {'propietarios': propietarios})

def editarPropietario(request, id):
    propietario_editar = Owner.objects.get(id=id)
    formulario = OwnerForm(request.POST or None, request.FILES or None, instance=propietario_editar)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('listar_propietarios')
    return render(request, 'properties/editarOwner.html', {'formulario': formulario})

def borrarPropietario(request, id):
    propietario_delete = Owner.objects.get(id=id)
    propietario_delete.delete()
    return redirect('listar_propietarios')

#--------------------------------------------------------------
#Gestion de Tipos de propiedad

def crearTipoPropiedad(request):
    formu = PropertyTyperForm(request.POST or None,request.FILES or None)
    if formu.is_valid():
        formu.save()
        return redirect('listar_tipos_propiedades') 
    return render(request, 'properties/crearTypeProperty.html', {'formulario': formu})

def listar_tipos_propiedades(request):
    tipos_propiedades = PropertyType.objects.all()
    return render(request, 'properties/indexTypeProperty.html', {'tipos_propiedades': tipos_propiedades})

def editarTipoPropiedad(request, id):
    tipo_propiedad_editar = PropertyType.objects.get(id=id)
    formulario = PropertyTyperForm(request.POST or None, request.FILES or None, instance=tipo_propiedad_editar)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('listar_tipos_propiedades')
    return render(request, 'properties/editarTypeProperty.html', {'formulario': formulario})

def borrarTipoPropiedad(request, id):
    tipo_propiedad_delete = PropertyType.objects.get(id=id)
    tipo_propiedad_delete.delete()
    return redirect('listar_tipos_propiedades')
#--------------------------------------------------------------
#Gestion de tipo de transacción

def crearTransaccion(request):
    formu = TransactionForm(request.POST or None,request.FILES or None)
    if formu.is_valid():
        formu.save()
        return redirect('listar_transacciones')
    return render(request, 'properties/crearTypeTransaction.html', {'formulario': formu})

def listar_transacciones(request):
    transacciones = TransactionType.objects.all()
    return render(request, 'properties/indexTypeTransaction.html', {'transacciones': transacciones})

def editarTransaccion(request, id):
    transaccion_editar = TransactionType.objects.get(id=id) 
    formulario = TransactionForm(request.POST or None, request.FILES or None, instance=transaccion_editar)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('listar_transacciones')
    return render(request, 'properties/editarTypeTransaction.html', {'formulario': formulario}) 

def borrarTransaccion(request, id):
    transaccion_delete = TransactionType.objects.get(id=id)
    transaccion_delete.delete()
    return redirect('listar_transacciones')

#--------------------------------------------------------------
#Gestion de Inmuebles
 
def crearProperty(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            # Crear el objeto pero no guardarlo aún
            property_instance = form.save(commit=False)
            # Establecer publication_date con la fecha y hora actual
            property_instance.publication_date = timezone.now()  # Usa timezone.now() aquí
            property_instance.save()
            return redirect('listar_inmuebles')
    else:
        form = PropertyForm()
    return render(request, 'properties/crearProperty.html', {'formulario': form})

def listarProperty(request):
    inmuebles = Property.objects.all()
    paginator = Paginator(inmuebles, 10) 
    page_number = request.GET.get('page')
    inmuebles = paginator.get_page(page_number)
    return render(request, 'properties/indexProperty.html', {'inmuebles': inmuebles})

def editarProperty(request, id):    
    inmueble_editar = Property.objects.get(id=id)
    formulario = PropertyForm(request.POST or None, request.FILES or None, instance=inmueble_editar)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('listar_inmuebles')
    return render(request, 'properties/editarProperty.html', {'formulario': formulario})

def borrarProperty(request, id):
    inmueble_delete = Property.objects.get(id=id)   
    inmueble_delete.delete()
    return redirect('listar_inmuebles')
#--------------------------------------------------------------






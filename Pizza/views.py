from django.shortcuts import render , redirect
from .models import Pizza , Pije
from .forms import KontaktForm, PorosiForm




def home(request):
    return render(request, 'home.html')  


def rrethnesh(request):
    return render(request, 'rrethnesh.html')       

def base(request):
    return render(request, 'base.html')

def navbar(request):
    return render(request, 'navbar.html')

def footer(request):
    return render(request, 'footer.html')        

def kontakti(request):
    return render(request, 'kontakti.html')     

def porositeonline(request):
    return render(request, 'porositeonline.html')             


def kontakt_view(request):
    if request.method == 'POST':
        form = KontaktForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kontakt_faleminderit')  
    else:
        form = KontaktForm()
    return render(request, 'kontakt.html', {'form': form})


def kontakt_faleminderit(request):
    return render(request, 'kontakt_faleminderit.html')    

def faleminderit(request):
    return render(request, 'faleminderit.html')
    
def menu(request):
    pizzas = Pizza.objects.all()
    pijet = Pije.objects.all()
    return render(request, 'menu.html', {'pizzas': pizzas, 'pijet': pijet})

def porositonline(request):
    pijet = Pije.objects.all()
    pizzat = Pizza.objects.all()

    if request.method == 'POST':
        form = PorosiForm(request.POST)
        if form.is_valid():
            porosi = form.save(commit=False)
            porosi.save()

            
            pije_ids = request.POST.getlist('pijet')
            pizza_ids = request.POST.getlist('pizzat')

            porosi.pijet.set(Pije.objects.filter(id__in=pije_ids))
            porosi.pizzat.set(Pizza.objects.filter(id__in=pizza_ids))

            return render(request, 'faleminderit.html')
    else:
        form = PorosiForm()

    context = {
        'form': form,
        'pijet': pijet,
        'pizzat': pizzat,
    }
    return render(request, 'porositeonline.html', context)

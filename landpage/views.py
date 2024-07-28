from django.shortcuts import render, redirect

from .form import Formulario

def home(request):
    if request.method == "POST":
        form = Formulario(request.POST)
        if form.is_valid():
            form.save()

            return redirect('landpage:thanks')
        
    else:
        form = Formulario()

    return render(request, 'home/index.html', {'form': form})

def thanks(request):
    return render(request, "thanks/index.html")
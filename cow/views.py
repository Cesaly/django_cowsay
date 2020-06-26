from django.shortcuts import render

from cow.models import CowText
from cow.forms import CowTextForm
import subprocess


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = CowTextForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form = CowTextForm()
            CowText.objects.create(
                text=data['text'],
            )
            cowsay_input = subprocess.run(
                ['cowsay'] + data['text'].split(), capture_output=True
            ).stdout.decode()

        return render(request, 'index.html', {'cowsay_input': cowsay_input,
                      'form': form})

    form = CowTextForm()
    return render(request, 'index.html', {'form': form})


def Last10(request):
    cowsay_history = list(CowText.objects.all())
    last10 = cowsay_history[-10:][::-1]

    return render(request, 'history.html', {'last10': last10})

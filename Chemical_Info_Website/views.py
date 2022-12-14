from django.http import HttpResponse
from django.template import loader
from .models import Chemical
from django.forms import ModelForm

class ChemicalForm(ModelForm):

    class Meta:
        model = Chemical
        fields = ["name", "BP_C", "BP_K", "smiles", "MW"]


def index(request, name):
    chemical_entry = Chemical.objects.get(name=name)
    context = {
        'name': chemical_entry.name,
        'BP_C': chemical_entry.BP_C,
        'BP_K': chemical_entry.BP_K,
        'smiles': chemical_entry.smiles,
        'MW': chemical_entry.MW,
    }
    template = loader.get_template('Chemical_Info_Website/chemweb.html')
    return HttpResponse(template.render(context, request))


def chemical_list(request, smiles):
    print(smiles)
    response =Chemical.objects.get(smiles=smiles)
    print('chemical_list', response.BP_C)
    return HttpResponse(response.BP_C)


def chemical_addition(request):
    form = ChemicalForm(request.POST)
    context = {'form': form}

    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        BP_C = data.get("BP_C")
        BP_K = data.get("BP_K")
        smiles = data.get("smiles")
        MW = data.get("MW")

        entry = Chemical(name='new_entry',
                     BP_C=BP_C,
                     BP_K=BP_K,
                     smiles=smiles,
                     MW=MW)
        print(entry)
        entry.save()
    template = loader.get_template('Chemical_Info_Website/add_chemical.html')

    return HttpResponse(template.render(context, request))

from django import forms
from cadastro_seller.models import Empresa, Oportunidade, Tarefa, Lead



class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'


class OportunidadeForm(forms.ModelForm):
    class Meta:
        model = Oportunidade
        fields = '__all__'


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__'
        widgets = {
            'status': forms.Select(choices=[
                ('em negociacao', 'Em Negociação'),
                ('perdida', 'Perdida'),
                ('concluida', 'Concluída'),
            ])
        }

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'
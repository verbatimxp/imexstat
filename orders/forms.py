from django import forms

from .models import OrderItem
from phonenumber_field.formfields import PhoneNumberField


class IndividualForm(forms.Form):
    lastname = forms.CharField(required=True, max_length=50)
    firstname = forms.CharField(required=True, max_length=50)
    middle_name = forms.CharField(required=True, max_length=50)
    email = forms.EmailField(required=True)
    phone = PhoneNumberField(required=True)


class EntityForm(forms.Form):
    firm_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    phone = PhoneNumberField(required=True)
    INN = forms.IntegerField(required=True)
    KPP = forms.IntegerField(required=True)
    legal_adress = forms.CharField(required=True)
    requisites_file = forms.FileField(required=False)


class CartResearchForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['research'].widget.attrs.update({'style': 'display:none;'})
        self.fields['research'].required = False
        self.fields['update_frequency'].required = False
        self.fields['duration'].required = False

    class Meta(object):
        model = OrderItem
        fields = '__all__'
        exclude = ['price', 'order']
        widgets = {
            'update_frequency': forms.RadioSelect(attrs={'class': 'checkbox__input'}),
            'duration': forms.RadioSelect(attrs={'class': 'Duration_choice'})
        }
        error_messages = {
            'update_frequency': {
                'required': ('Выберите частоту исследования')
            },
            'duration': {
                'required': ('Выберите срок подписки')
            }
        }


Formset = forms.formset_factory(CartResearchForm)

from django import forms
from admin.models import my_menu,my_pages,my_constant

class CreateConstForm(forms.ModelForm):
   header = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'input-small','placeholder':'Header'}))
   footer = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'input-small','placeholder':'Footer'}))
   page_title = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'input-small','placeholder':'Title'}))
   page_note = forms.CharField(required=False,widget=forms.TextInput(attrs={'autocomplete':'off','class':'input-small','placeholder':'Slogan'}))
   base_site = forms.URLField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'input-small','placeholder':'Base site'}))
   class Meta:
      model = my_constant 
      exclude = ['date']

class CreateMenuForm(forms.ModelForm):
   menu = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'input-small','placeholder':'Menu'}))
   menu_link = forms.URLField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'input-small','placeholder':'http://domain/menu_link/'}))
   class Meta:
      model = my_menu
      exclude = ['date']

class CreatemypagesForm(forms.ModelForm):
   Topic_Header = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'input-small','placeholder':'Topic Header'}))
   Topic_Detail = forms.CharField(widget=forms.Textarea(attrs={'autocomplete':'off','class':'input-xsmall','id':'textarea'}))
   Topic_In_Depth = forms.CharField(required=False,widget=forms.Textarea(attrs={'autocomplete':'off','class':'input-xsmall','id':'textarea'}))
   class Meta:
      model = my_pages
      exclude = ['date']

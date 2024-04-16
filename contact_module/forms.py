from  django import forms

from .models import ContactUs


class ContactUsForms(forms.Form):
    full_name = forms.CharField(
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام و نام خانوادگی'
        }),
        max_length=50,
        error_messages= {
            'required': 'لطفا نام و نام خانوادگی را وارد کنید',
            'max_lenght': 'بیشتر از 50 کاراکتر نباشد'},
        label= 'نام و نام خانوادگی')
    email = forms.EmailField(
        widget= forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ایمیل'
        }),
        label='ایمیل')
    title = forms.CharField(        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'موضوع'
        }),
        label='عنوان')
    message = forms.CharField(label='متن پیام', widget= forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'message',
            'placeholder': 'متن'
        }),)

class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name','email','title', 'message']
        #fields ='__all__' hame
        #exclude = ['response'] hame be joz responce
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'message': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'message'
            })
        }
        labels = {
            'full_name': 'نام و نام خانوادگی جدید',
        }
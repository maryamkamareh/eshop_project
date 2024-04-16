from  django import forms
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
    subject = forms.CharField(        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'موضوع'
        }),
        label='عنوان')
    text = forms.CharField(label='متن پیام', widget= forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'message',
            'placeholder': 'متن'
        }),)
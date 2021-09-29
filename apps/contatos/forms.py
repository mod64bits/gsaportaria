from django import forms


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Digite seu nome!',
    }))
    email = forms.EmailField(label='email', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Digite seu melhor e-mail!',
    }))
    telefone = forms.CharField(label='Telefone', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Digite seu telefone se tiver seu  whatsapp!',
    }))
    assunto = forms.CharField(label='Assunto', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Digite o assunto de sua mensagem!',
    }))
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Digite Sua mensagem!',
    }))

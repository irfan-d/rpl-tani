from django.forms import ModelForm
from .models import Tumbuhan


class PostForm(ModelForm):
    class Meta:
        model = Tumbuhan
        fields = ['namaTanam', 'jenisTanam', 'deskripsiTanam']

#!/user/bin/env/python
# -*- coding:utf-8 -*_
# 作者:gongwannan

from django import forms
from tinymce.models import HTMLField
from .models import Luntan, Fenlei


class PinglunForm(forms.Form):
    content = forms.CharField(label='评论', max_length=21845, widget=forms.TextInput)


class TieziForm(forms.Form):
    title = forms.CharField(label='标题', max_length=256, widget=forms.TextInput)
    content = forms.CharField(label='内容', max_length=21845, widget=forms.TextInput)
    luntanfenzhi = forms.ModelChoiceField(label='主题板块', queryset=Fenlei.objects.all())




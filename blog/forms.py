from django import forms

#form은 템플릿에서 보여줄 양식을 설정하는 기능을 담고 있다.

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word') # label은 input앞에 붙여질 제목을 가리킨다.

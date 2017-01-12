from django.views.generic.base import TemplateView

#--- TemplateView
class HomeView(TemplateView):
    template_name = 'home.html' # TemplateView상속받을 경우 template_nmae 을 꼭 지정해줘야함

from django.views.generic import TemplateView


class MainView(TemplateView):
    # TODO: использовать ajax запросы к api и рендерить контент в html
    template_name = 'website/main.html'


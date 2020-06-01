# third party imports
from django.contrib.auth.views import TemplateView

# app imports
from .utils import evaluate_words


class TableView(TemplateView):
    template_name = 'table.html'

    def get_context_data(self, **kwargs):
        context = super(TableView, self).get_context_data(**kwargs)
        context['word_sentence_dict'] = evaluate_words()

        return context



from typing import Any
from django.views.generic.edit import BaseFormView

class NotesContextOrganizer(BaseFormView):
    title = ''

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = self.title
        return ctx

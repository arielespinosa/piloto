from django.http import JsonResponse
from time import sleep


class BSModalAjaxFormMixin(object):

    def get_data_as_json(self, form):
        return form.cleaned_data

 
    def form_invalid(self, form):
        response = super(BSModalAjaxFormMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response
  

    def form_valid(self, form):
        response = super(BSModalAjaxFormMixin, self).form_valid(form)

        if self.request.is_ajax():     
            if form.is_valid():
                datos = {
                    'title': "Notificación",
                    'message': self.success_message,
                    #'data': form.cleaned_data,
                }
          
            return JsonResponse(datos)
        else:
            return response





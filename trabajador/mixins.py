from django.http import JsonResponse
from time import sleep


class BSModalAjaxFormMixin(object):

    def get_data_as_json(self, form):
        return form.cleaned_data

 
    def form_invalid(self, form):
        #response = super(BSModalAjaxFormMixin, self).form_invalid(form)
        if self.request.is_ajax():
            datos = {
                'title': "Notificación",
                'message': self.error_message,
                #'data': form.cleaned_data,
            }           
            return JsonResponse(datos)
        else:             
            #return JsonResponse(form.errors, status=400)
            print("no es Ajax")     
            return response
  

    def form_valid(self, form):
        response = super(BSModalAjaxFormMixin, self).form_valid(form)

        if self.request.is_ajax():     
            if form.is_valid():
                form.save(commit=False)
                form.author1 = self.request.user.appuser 
                 

                datos = {
                    'title': "Notificación",
                    'message': self.success_message,
                    #'data': form.cleaned_data,
                }
          
            return JsonResponse(datos)
        else:
            return response
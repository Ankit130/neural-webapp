from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from image.forms import EmployeeForm
from django.views.generic import DetailView
from image.models import Employee
from style import applystyle


class EmployeeImage(TemplateView):

    form = EmployeeForm
    template_name = 'emp_image.html'

    def post(self, request, *args, **kwargs):

        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            print(obj.emp_image)
            applystyle('/media/upload/'+obj.emp_image,'/medial/style/'+obj.emp_image2)
            return HttpResponseRedirect(reverse_lazy('emp_image_display', kwargs={'pk': obj.id}))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class EmpImageDisplay(DetailView):
    model = Employee
    template_name = 'emp_image_display.html'
    context_object_name = 'emp'
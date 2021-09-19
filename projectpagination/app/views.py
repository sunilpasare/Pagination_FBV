
from .models import Laptop
from .forms import LaptopForm
from django.shortcuts import redirect, render
from django.core.paginator import Paginator

# Create your views here.
def createorderview(request):
    form=LaptopForm()
    if request.method == "POST":
        form=LaptopForm(request.POST,request.FILES)
        if form.is_valid():
          form.save()
          return redirect('pagination')

    template_name='addorder.html'
    context={'form':form}
    return render(request,template_name,context)



def Paginationshowview(request):
    all_laptops=Laptop.objects.all()
    paginator=Paginator(all_laptops,2)
    page_number =request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pagination.html', {'page_obj': page_obj})
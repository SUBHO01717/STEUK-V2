from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from . form import *
from django.http import HttpResponseBadRequest
# Create your views here.

def Home(request):
    categories=Category.objects.all()
    context={
        'categories': categories,
    }
    return render(request, 'index.html', context)

def Shop(request):
    products=Product.objects.filter(show_product='YES')
    context={
        'products': products
    }
    return render(request, 'shop.html', context)


def ProductList(request, category_id=None):
    products = Product.objects.filter(show_product='YES')
    if category_id:
        category = Category.objects.get(pk=category_id)
        products = products.filter(category=category)
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
        'category':category
    }
    return render(request, 'product_list.html', context)

def ProductDetails(request, pk):
    try:
        product = Product.objects.get(id=pk)
        brochure = Brochure.objects.get(product=product)
    except ObjectDoesNotExist:
        product = Product.objects.get(id=pk)
        brochure = None  # Set brochure to None or any default value you prefer

    similar_products = Product.objects.filter(category=product.category).exclude(id=pk)[:3]

    context = {
        'product': product,
        'similar_products': similar_products,
        'brochure': brochure
    }

    return render(request, 'product-details.html', context)

def About(request):
    return render(request, 'about.html')



def AllServices(request):
    servicescategory=ServiceCategory.objects.all()

    context={
        'servicescategory':servicescategory
    }
    return render(request, 'services.html', context)


def SingleServices(request, pk):
    # Retrieve the ServiceCategory object with the given primary key
    category = get_object_or_404(ServiceCategory, pk=pk)
    services = Services.objects.filter(category=category)



    context = {
        'services': services,
        'category': category,
    }
    return render(request, 'single_services.html', context)

def SingleServiceDetails(request,pk):
    
    service=Services.objects.get(pk=pk)

    context = {
        'service': service,
        
        }

    return render(request, 'single_service_details.html', context)


def Package(request):
    return render(request, 'packages.html')

def Design(request):
    return render(request, 'design.html')

def Installation(request):
    return render(request, 'installation.html')

def Maintenance(request):
    return render(request, 'maintenance.html')

def BlogView(request):
    all_blog=Blog.objects.all()
    context={
        'all_blog':all_blog,
    }
    return render(request, 'blog.html', context)

def BlogDetailsView(request,pk):
    blog=Blog.objects.get(id=pk)
    context={
        'blog':blog,
    }
    return render(request, 'blog_details.html', context)


def ContactUs(request):

    if request.POST:
        form = ContactForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect ("/thanks/")
      
    else:
         form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'contact.html', context)

def Thanks(request):

    return render(request, 'thanks.html')


def AdminView(request):

    category=Category.objects.all().count()
    product=Product.objects.all().count()
    allproduct=Product.objects.all()
    allcategory=Category.objects.all()
   

    context={
        'category': category,
        'product': product,
        'allproduct':allproduct,
        'allcategory':allcategory,

    }

    return render(request, 'backend/backend.html',context)



# def formItems(request):

#     q_category=Q_FormType.objects.all()
#     all_blog=Blog.objects.all()

#     context={
#         'q_category':q_category,
#         'all_blog':all_blog,
#     }

#     return render(request, 'questionary.html' , context)


def formItems(request):

    q_category=Q_FormType.objects.all()
    all_blog=Blog.objects.all()

    context={
        'q_category':q_category, 
        'all_blog':all_blog,
    }

    return render(request, 'questionary.html' , context)

def QFormType(request, pk):
    form_type = get_object_or_404(Q_FormType, pk=pk)

    if request.method == "POST":
        if form_type.name == 'Boiler':
            form = BoilerForm(request.POST)
        elif form_type.name == 'Heat Pump':
            form = HeatPumpForm(request.POST)
        elif form_type.name == 'EV Charger':
            form = EVForm(request.POST)
        elif form_type.name == 'Home Security':
            form = HomeSecurityForm(request.POST)

        elif form_type.name == 'Infrared Heating':
            form = InfraredHeatForm(request.POST)

        elif form_type.name == 'Solar System':
            form = SolarForm(request.POST)
        
        elif form_type.name == 'Window':
            form = WindowForm(request.POST)

        else:
            return HttpResponseBadRequest("Invalid form type")

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        initial_values = {}
        if form_type.name == 'Boiler':
            initial_values = {'formType': 'Boiler'}  # Set default values for BoilerForm fields
            form = BoilerForm(initial=initial_values)
        elif form_type.name == 'Heat Pump':
            initial_values = {'formType': 'Heat Pump'}  # Set default values for HeatPumpForm fields
            form = HeatPumpForm(initial=initial_values)
        elif form_type.name == 'EV Charger':
            initial_values = {'formType': 'EV Charger'}  # Set default values for EVForm fields
            form = EVForm(initial=initial_values)
        
        elif form_type.name == 'Home Security':
            initial_values = {'formType': 'Home Security'}  # Set default values for EVForm fields
            form = HomeSecurityForm(initial=initial_values)

        elif form_type.name == 'Infrared Heating':
            initial_values = {'formType': 'Infrared Heating'}  # Set default values for EVForm fields
            form = InfraredHeatForm(initial=initial_values)
        elif form_type.name == 'Solar System':
            initial_values = {'formType': 'Solar System'}  # Set default values for EVForm fields
            form = SolarForm(initial=initial_values)

        elif form_type.name == 'Window':
            initial_values = {'formType': 'Window'}  # Set default values for EVForm fields
            form = WindowForm(initial=initial_values)

        else:
            return HttpResponseBadRequest("Invalid form type")

        return render(request, 'form.html', {'form': form, 'form_type': form_type})

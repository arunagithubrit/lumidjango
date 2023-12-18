from django.shortcuts import render,redirect
from productapp.forms import CategoryCreateForm,ProductCreateForm
from productapp.models import Category,Product
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.db.models import Count

# Create your views here.


class CategoryCreateView(CreateView):
    template_name="category_add.html"
    form_class=CategoryCreateForm
    model=Category
    success_url=reverse_lazy("category-add")


class ProductCreateView(CreateView):
    template_name="product_add.html"
    form_class=ProductCreateForm
    model=Product
    success_url=reverse_lazy("product-add")


# class ProductListView(ListView):
#     template_name="product_list.html"
#     context_object_name="products"
#     model=Product
def product_list(request):
    categories = Category.objects.annotate(num_products=Count('product'))
    products = Product.objects.all()
    # allprods=[]
    # catprods=Product.objects.values('category_name','id')
    # cats={item['category_name'] for item in catprods}
    # for cat in cats:
    #     prod=Product.objects.filter(category_name=cat)
    #     n=len(prod)
    #     nSlides=n//4 + ceil((n/4)-(n//4))
    #     allprods.append([prod,range(1,nSlides),nSlides])

    category_filter = request.GET.get('category_filter')
    if category_filter:
        products = products.filter(category_name__id=category_filter)
    else:
        return render(request, "product_list.html", {'categories': categories, 'products': products, 'selected_category': int(category_filter) if category_filter else None})
        # return render(request,"product_list.html",{"categories":categories})


class ProductDetailView(DetailView):
    template_name="product_detail.html"
    context_object_name="product"
    model=Product


class ProductUpdateView(UpdateView):
    template_name="product_edit.html"
    form_class=ProductCreateForm
    model=Product
    success_url=reverse_lazy("product-list")

def remove_product(request,*args,**kwargs):
    id=kwargs.get("pk")
    Product.objects.filter(id=id).delete()
    return redirect("product-list")  


    


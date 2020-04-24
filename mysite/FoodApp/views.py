from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, PostContactInfo
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('FoodApp/index.html')
    context = {
        'item_list': item_list,
    }

    return render(request, 'FoodApp/index.html', context)
    # return HttpResponse(template.render(context,request))


def thanks_page(request):
    return render(request, 'FoodApp/thankyou.html', None)


class IndexClassView(ListView):
    model = Item;
    template_name = 'FoodApp/index.html'
    context_object_name = 'item_list'
    paginate_by = 4
    queryset = Item.objects.all()


def item(request):
    return HttpResponse('<h1>This is new view for items</h1>')


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'FoodApp/detail.html', context)


class FoodDetail(DetailView):
    model = Item
    template_name = 'FoodApp/detail.html'


def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('FoodApp:index')
    return render(request, 'FoodApp/item-forms.html', {'form': form})


# this is class based view for create_item

class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'FoodApp/item-forms.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


class PostContactInfoView(CreateItem):
    model = PostContactInfo
    fields = ['customer_name', 'email_id', 'mobile_no', 'message']
    template_name = 'FoodApp/contact-us-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


def update_item(request, id):
    item = Item.objects.get(pk=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.instance.user_name = request.user
        form.save()
        return redirect('FoodApp:index')
    return render(request, 'FoodApp/item-forms-update.html', {'form': form, 'item': item})


def delete_item(request, id):
    item = Item.objects.get(pk=id)
    form = ItemForm(request.POST or None, instance=item)

    if request.method == 'POST':
        form.instance.user_name = request.user
        item.delete()
        return redirect('FoodApp:index')

    return render(request, 'FoodApp/item-delete.html', {'item': item})

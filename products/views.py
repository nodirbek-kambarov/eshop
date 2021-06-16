from django.views.generic import ListView, DetailView

from products.models import ProductModel, BrandModel, CategoryModel, ProductTagModel


class ProductsListView(ListView):
    template_name = 'products.html'
    paginate_by = 3

    def get_queryset(self):
        qs = ProductModel.objects.order_by('-pk')
        q = self.request.GET.get('q')
        cat = self.request.GET.get('cat')
        brand = self.request.GET.get('brand')
        tag = self.request.GET.get('tag')
        sort = self.request.GET.get('sort')


        if q:
            qs = qs.filter(title__icontains=q)

        if brand:
            qs = qs.filter(brand__id=brand)

        if tag:
            qs = qs.filter(tags__id=tag)

        if cat:
            qs = qs.filter(category__id=cat)

        if sort:
            if sort == 'price':
                qs = sorted(qs, key=lambda i: i.get_price())
            elif sort == '-price':
                qs = sorted(qs, key=lambda i: i.get_price(), reverse=True)

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = BrandModel.objects.order_by('-pk')
        context['categories'] = CategoryModel.objects.order_by('-pk')
        context['tags'] = ProductTagModel.objects.order_by('-pk')
        return context


class ProductDetailView(DetailView):
    template_name = 'product.html'
    model = ProductModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related'] = self.object.category.products.exclude(pk=self.object.pk)[:4]
        return context

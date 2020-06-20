from django.views import generic
from personal_cabinet.models import Client
from .models import Order
from orders.cart import Cart
from products.models import Research
from multi_form_view import MultiFormView
from .forms import EntityForm, IndividualForm, CartResearchForm
from django.urls import reverse
from django import forms


class CartListView(generic.TemplateView):
    template_name = 'orders/cart_list.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.GET.get('remove_from_cart'):
            self.remove_from_cart(request)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart()
        return context

    def remove_from_cart(self):
        if self.request.user.is_authenticated:
            cart = Cart.objects.get(client_id=self.request.user.id)
            Cart.objects.get(cart=cart).delete()
        else:
            cart = Cart(self.request)
            for item in cart:
                if item.get_product().research:
                    cart.remove(item.product)


class CartPurchaseView(MultiFormView):
    form_classes = {
        'entity_form': EntityForm,
        'individual_form': IndividualForm,
    }
    template_name = 'orders/cart_purchase.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.GET.get('remove_from_cart'):
            self.remove_from_cart(request)
        return super(CartPurchaseView, self).dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        FormSet = forms.formset_factory(CartResearchForm)
        formset = FormSet(request.POST or None)
        get_forms = self.get_forms()
        if formset.is_valid() and self.are_forms_valid(get_forms):
            self.form_valid(formset)
        else:
            return self.form_invalid(formset)

    def forms_valid(self, forms):
        client_form = Client.objects.get(user=self.request.user) if self.request.user.is_authenticated else None
        order_form = Order.objects.latest()
        client_form.save() if self.request.user.is_authenticated else None
        order_form.save()
        return super().forms_valid(forms)

    def remove_from_cart(self):
        if self.request.GET.get('remove_from_order'):
            Research.objects.get(slug=self.request.GET.get('remove_from_order'))
            if self.request.user.is_authenticated:
                Cart.objects.get(client_id=self.request.user.id)
            else:
                None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = kwargs['form']
        return context

    def get_success_url(self):
        return reverse('orders:cart')


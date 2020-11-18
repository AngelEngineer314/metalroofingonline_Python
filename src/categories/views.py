from django.shortcuts import render
from django.core.exceptions import MultipleObjectsReturned
from django.views.generic import ListView

from products.models import Product
from carts.models import Cart
from categories.models import Category

class RoofingIronListView(ListView):
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(RoofingIronListView, self).get_context_data(
            *args, **kwargs)
        self.request.session.save()
        try:
            cart_obj, cart_created = Cart.objects.get_or_create(cart_session_id=self.request.session.session_key)
        except MultipleObjectsReturned:
            cart_obj = Cart.objects.filter(cart_session_id=self.request.session.session_key).first()

        try:
            category = Category.objects.filter(title='Roofing Iron').first()
            context['description'] = category.description
            context['description_bottom'] = category.description_bottom
        except:
            pass
        context['cart'] = cart_obj
        context['title'] = 'Roofing Iron'
        context['meta_title'] = 'COLORBOND Roofing Sheets | Metal Roofing Online'
        context['meta_description'] = 'COLORBOND roofing sheets. Easy online ordering of metal roofing. Lowest prices with fast delivery. Trusted BlueScope Steel.'


        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.filter(categoryoption__option__category='Roofing Iron')


class RainwaterGoodsListView(ListView):
    template_name = "products/list.html"


    def get_context_data(self, *args, **kwargs):
        context = super(RainwaterGoodsListView, self).get_context_data(
            *args, **kwargs)
        self.request.session.save()
        try:
            cart_obj, cart_created = Cart.objects.get_or_create(cart_session_id=self.request.session.session_key)
        except MultipleObjectsReturned:
            cart_obj = Cart.objects.filter(cart_session_id=self.request.session.session_key).first()

        try:
            category = Category.objects.filter(title='Rainwater Goods').first()
            context['description'] = category.description
            context['description_bottom'] = category.description_bottom
        except:
            pass

        context['cart'] = cart_obj
        context['title'] = 'Rainwater Goods'
        context['meta_title'] = 'COLORBOND Gutter & Fascia | Metal Roofing Online'
        context['meta_description'] = 'COLORBOND gutter, fascia & more metal roofing materials. Lowest prices with FAST delivery. Easy online ordering. Trusted Australian BlueScope Steel.'

        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.filter(categoryoption__option__category='Rainwater Goods')


class FlashingsListView(ListView):
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(FlashingsListView, self).get_context_data(
            *args, **kwargs)
        self.request.session.save()
        try:
            cart_obj, cart_created = Cart.objects.get_or_create(cart_session_id=self.request.session.session_key)
        except MultipleObjectsReturned:
            cart_obj = Cart.objects.filter(cart_session_id=self.request.session.session_key).first()

        try:
            category = Category.objects.filter(title='Flashings').first()
            context['description'] = category.description
            context['description_bottom'] = category.description_bottom
        except:
            pass

        context['cart'] = cart_obj
        context['title'] = 'Flashings'
        context['meta_title'] = 'COLORBOND, ZINCALUME flashings | Metal Roofing Online'
        context['meta_description'] = 'COLORBOND or ZINCALUME flashings. Order online. Lowest prices. Fast delivery. Easy, secure online ordering. Trusted Australian BlueScope steel.'

        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.filter(categoryoption__option__category='Flashings')


class PolycarbonateListView(ListView):
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PolycarbonateListView, self).get_context_data(
            *args, **kwargs)
        self.request.session.save()
        try:
            cart_obj, cart_created = Cart.objects.get_or_create(cart_session_id=self.request.session.session_key)
        except MultipleObjectsReturned:
            cart_obj = Cart.objects.filter(cart_session_id=self.request.session.session_key).first()

        try:
            category = Category.objects.filter(title='Polycarbonate').first()
            context['description'] = category.description
            context['description_bottom'] = category.description_bottom
        except:
            pass

        context['cart'] = cart_obj
        context['title'] = 'Polycarbonate'
        context['meta_title'] = 'Polycarbonate Roof Sheets | Metal Roofing Online'
        context['meta_description'] = 'Polycarbonate roof  sheets. Corrugated, Greca & more. Order online. Lowest prices. Fast delivery. Easy ordering. Trusted Australian BlueScope steel.'

        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.filter(categoryoption__option__category='Polycarbonate')


class InsulationListView(ListView):
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(InsulationListView, self).get_context_data(
            *args, **kwargs)
        self.request.session.save()
        try:
            cart_obj, cart_created = Cart.objects.get_or_create(cart_session_id=self.request.session.session_key)
        except MultipleObjectsReturned:
            cart_obj = Cart.objects.filter(cart_session_id=self.request.session.session_key).first()

        try:
            category = Category.objects.filter(title='Insulation').first()
            context['description'] = category.description
            context['description_bottom'] = category.description_bottom
        except:
            pass

        context['cart'] = cart_obj
        context['title'] = 'Insulation'
        context['meta_title'] = 'Insulation | Metal Roofing Online'
        context['meta_description'] = 'Roofing Insulation. Roof foil, blanket & more. Order online. Lowest prices. Fast delivery. Easy ordering. Trusted Australian BlueScope steel.'

        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.filter(categoryoption__option__category='Insulation')


class AccessoriesListView(ListView):
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(AccessoriesListView, self).get_context_data(
            *args, **kwargs)
        self.request.session.save()
        try:
            cart_obj, cart_created = Cart.objects.get_or_create(cart_session_id=self.request.session.session_key)
        except MultipleObjectsReturned:
            cart_obj = Cart.objects.filter(cart_session_id=self.request.session.session_key).first()

        try:
            category = Category.objects.filter(title='Accessories').first()
            context['description'] = category.description
            context['description_bottom'] = category.description_bottom
        except:
            pass

        context['cart'] = cart_obj
        context['title'] = 'Accessories'
        context['meta_title'] = 'Roofing Accessories | Metal Roofing Online'
        context['meta_description'] = 'Metal Roofing Accessories. Fasteners, leaf guard & more. Order online. Lowest prices. Fast delivery. Easy ordering. Trusted Australian BlueScope steel.'

        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.filter(categoryoption__option__category='Accessories')


class GutteringListView(ListView):
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(GutteringListView, self).get_context_data(
            *args, **kwargs)
        self.request.session.save()
        try:
            cart_obj, cart_created = Cart.objects.get_or_create(cart_session_id=self.request.session.session_key)
        except MultipleObjectsReturned:
            cart_obj = Cart.objects.filter(cart_session_id=self.request.session.session_key).first()

        try:
            category = Category.objects.filter(title='Rainwater Goods - Guttering').first()
            context['description'] = category.description
            context['description_bottom'] = category.description_bottom
        except:
            pass

        context['cart'] = cart_obj
        context['title'] = 'Rainwater Goods - Guttering'
        context['meta_title'] = 'COLORBOND, ZINCALUME Gutter | Metal Roofing Online'
        context['meta_description'] = 'COLORBOND or ZINCALUME Gutter at lowest prices. FAST delivery. Easy, secure online ordering. Trusted Australian BlueScope Steel.'

        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.filter(categoryoption__option__category='Guttering')


class FasciaListView(ListView):
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(FasciaListView, self).get_context_data(
            *args, **kwargs)
        self.request.session.save()
        try:
            cart_obj, cart_created = Cart.objects.get_or_create(cart_session_id=self.request.session.session_key)
        except MultipleObjectsReturned:
            cart_obj = Cart.objects.filter(cart_session_id=self.request.session.session_key).first()

        try:
            category = Category.objects.filter(title='Rainwater Goods - Fascia').first()
            context['description'] = category.description
            context['description_bottom'] = category.description_bottom
        except:
            pass

        context['cart'] = cart_obj
        context['title'] = 'Rainwater Goods - Fascia'
        context['meta_title'] = 'COLORBOND, ZINCALUME Fascia | Metal Roofing Online'
        context['meta_description'] = 'COLORBOND or ZINCALUME Fascia. Order online NOW. Lowest prices. FAST delivery. Easy, secure online ordering. Trusted Australian BlueScope Steel.'

        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.filter(categoryoption__option__category='Fascia')


class DownpipesListView(ListView):
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DownpipesListView, self).get_context_data(
            *args, **kwargs)
        self.request.session.save()
        try:
            cart_obj, cart_created = Cart.objects.get_or_create(cart_session_id=self.request.session.session_key)
        except MultipleObjectsReturned:
            cart_obj = Cart.objects.filter(cart_session_id=self.request.session.session_key).first()

        try:
            category = Category.objects.filter(title='Rainwater Goods - Downpipes').first()
            context['description'] = category.description
            context['description_bottom'] = category.description_bottom
        except:
            pass

        context['cart'] = cart_obj
        context['title'] = 'Rainwater Goods - Downpipes'
        context['meta_title'] = 'COLORBOND, ZINCALUME Downpipes | Metal Roofing Online'
        context['meta_description'] = 'COLORBOND or ZINCALUME Downpipes. Order online at lowest prices. FAST delivery. Easy, secure online ordering. Trusted Australian BlueScope Steel.'

        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.filter(categoryoption__option__category='Downpipes')


class RidgesListView(ListView):
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(RidgesListView, self).get_context_data(
            *args, **kwargs)
        self.request.session.save()
        try:
            cart_obj, cart_created = Cart.objects.get_or_create(cart_session_id=self.request.session.session_key)
        except MultipleObjectsReturned:
            cart_obj = Cart.objects.filter(cart_session_id=self.request.session.session_key).first()

        try:
            category = Category.objects.filter(title='Flashings - Ridges').first()
            context['description'] = category.description
            context['description_bottom'] = category.description_bottom
        except:
            pass

        context['cart'] = cart_obj
        context['title'] = 'Flashings - Ridges'
        context['meta_title'] = 'COLORBOND, ZINCALUME Ridge | Metal Roofing Online'
        context['meta_description'] = 'COLORBOND or ZINCALUME ridge flashings. Order online. Lowest prices. Fast delivery. Easy online ordering. Trusted Australian BlueScope steel.'

        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.filter(categoryoption__option__category='Ridges')


class ValleysListView(ListView):
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ValleysListView, self).get_context_data(
            *args, **kwargs)
        self.request.session.save()
        try:
            cart_obj, cart_created = Cart.objects.get_or_create(cart_session_id=self.request.session.session_key)
        except MultipleObjectsReturned:
            cart_obj = Cart.objects.filter(cart_session_id=self.request.session.session_key).first()

        try:
            category = Category.objects.filter(title='Flashings - Valleys').first()
            context['description'] = category.description
            context['description_bottom'] = category.description_bottom
        except:
            pass

        context['cart'] = cart_obj
        context['title'] = 'Flashings - Valleys'
        context['meta_title'] = 'COLORBOND, ZINCALUME Valley | Metal Roofing Online'
        context['meta_description'] = 'COLORBOND or ZINCALUME roof valley flashings. Order online. Lowest prices. Fast delivery. Easy ordering. Trusted Australian BlueScope steel.'

        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.filter(categoryoption__option__category='Valleys')


class BargeCappingsListView(ListView):
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(BargeCappingsListView, self).get_context_data(
            *args, **kwargs)
        self.request.session.save()
        try:
            cart_obj, cart_created = Cart.objects.get_or_create(cart_session_id=self.request.session.session_key)
        except MultipleObjectsReturned:
            cart_obj = Cart.objects.filter(cart_session_id=self.request.session.session_key).first()

        try:
            category = Category.objects.filter(title='Flashings - Barge Cappings').first()
            context['description'] = category.description
            context['description_bottom'] = category.description_bottom
        except:
            pass

        context['cart'] = cart_obj
        context['title'] = 'Flashings - Barge Cappings'
        context['meta_title'] = 'COLORBOND, ZINCALUME Barge Capping | Metal Roofing Online'
        context['meta_description'] = 'COLORBOND or ZINCALUME barge capping flashings. Order online. Lowest prices. Fast delivery. Easy ordering. Trusted Australian BlueScope steel.'


        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.filter(categoryoption__option__category='Barge Capping')


class ApronsListView(ListView):
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ApronsListView, self).get_context_data(
            *args, **kwargs)
        self.request.session.save()
        try:
            cart_obj, cart_created = Cart.objects.get_or_create(cart_session_id=self.request.session.session_key)
        except MultipleObjectsReturned:
            cart_obj = Cart.objects.filter(cart_session_id=self.request.session.session_key).first()

        try:
            category = Category.objects.filter(title='Flashings - Aprons').first()
            context['description'] = category.description
            context['description_bottom'] = category.description_bottom
        except:
            pass

        context['cart'] = cart_obj
        context['title'] = 'Flashings - Aprons'
        context['meta_title'] = 'COLORBOND, ZINCALUME Apron | Metal Roofing Online'
        context['meta_description'] = 'COLORBOND or ZINCALUME roof apron flashings. Order online. Lowest prices. Fast delivery. Easy ordering. Trusted Australian BlueScope steel.'


        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.filter(categoryoption__option__category='Apron Flashing')


class BoxGuttersListView(ListView):
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(BoxGuttersListView, self).get_context_data(
            *args, **kwargs)
        self.request.session.save()
        try:
            cart_obj, cart_created = Cart.objects.get_or_create(cart_session_id=self.request.session.session_key)
        except MultipleObjectsReturned:
            cart_obj = Cart.objects.filter(cart_session_id=self.request.session.session_key).first()

        try:
            category = Category.objects.filter(title='Rainwater Goods - Box Gutters').first()
            context['description'] = category.description
            context['description_bottom'] = category.description_bottom
        except:
            pass

        context['cart'] = cart_obj
        context['title'] = 'Rainwater Goods - Box Gutters'
        context['meta_title'] = 'COLORBOND, ZINCALUME Box Gutter | Metal Roofing Online'
        context['meta_description'] = 'COLORBOND or ZINCALUME roof box gutter flashings. Order online. Lowest prices. Fast delivery. Easy ordering. Trusted Australian BlueScope steel.'

        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.filter(categoryoption__option__category='Box Gutters')


class FlatSheetListView(ListView):
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(FlatSheetListView, self).get_context_data(
            *args, **kwargs)
        self.request.session.save()
        try:
            cart_obj, cart_created = Cart.objects.get_or_create(cart_session_id=self.request.session.session_key)
        except MultipleObjectsReturned:
            cart_obj = Cart.objects.filter(cart_session_id=self.request.session.session_key).first()

        try:
            category = Category.objects.filter(title='Rainwater Goods - Flat Sheet').first()
            context['description'] = category.description
            context['description_bottom'] = category.description_bottom
        except:
            pass

        context['cart'] = cart_obj
        context['title'] = 'Rainwater Goods - Flat Sheet'
        context['meta_title'] = 'COLORBOND, ZINCALUME Flat Sheet | Metal Roofing Online'
        context['meta_description'] = 'COLORBOND or ZINCALUME flat sheet. Order online. Lowest prices. Fast delivery. Easy ordering. Trusted Australian BlueScope steel.'


        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.filter(categoryoption__option__category='Flat Sheet')


class WindowFlashingsListView(ListView):
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(WindowFlashingsListView, self).get_context_data(
            *args, **kwargs)
        self.request.session.save()
        try:
            cart_obj, cart_created = Cart.objects.get_or_create(cart_session_id=self.request.session.session_key)
        except MultipleObjectsReturned:
            cart_obj = Cart.objects.filter(cart_session_id=self.request.session.session_key).first()

        try:
            category = Category.objects.filter(title='Rainwater Goods - Window Flashings').first()
            context['description'] = category.description
            context['description_bottom'] = category.description_bottom
        except:
            pass

        context['cart'] = cart_obj
        context['title'] = 'Rainwater Goods - Window Flashings'
        context['meta_title'] = 'COLORBOND, ZINCALUME Window Flashing | Metal Roofing Online'
        context['meta_description'] = 'COLORBOND or ZINCALUME window flashings. Order online. Lowest prices. Fast delivery. Easy ordering. Trusted Australian BlueScope steel.'

        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.filter(categoryoption__option__category='Window Flashings')


class RoofingFastenersListView(ListView):
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(RoofingFastenersListView, self).get_context_data(
            *args, **kwargs)
        self.request.session.save()
        try:
            cart_obj, cart_created = Cart.objects.get_or_create(cart_session_id=self.request.session.session_key)
        except MultipleObjectsReturned:
            cart_obj = Cart.objects.filter(cart_session_id=self.request.session.session_key).first()

        try:
            category = Category.objects.filter(title='Accessories - Rofing Fasteners').first()
            context['description'] = category.description
            context['description_bottom'] = category.description_bottom
        except:
            pass

        context['cart'] = cart_obj
        context['title'] = 'Accessories - Roofing Fasteners'
        context['meta_title'] = 'Roofing Fasteners | Metal Roofing Online'
        context['meta_description'] = 'Metal Roofing Fasteners. Fasteners, leaf guard & more. Order online. Lowest prices. Fast delivery. Easy ordering. Trusted Australian BlueScope steel.'

        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.filter(categoryoption__option__category='Roofing Fasteners')


class GutterGuardListView(ListView):
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(GutterGuardListView, self).get_context_data(
            *args, **kwargs)
        self.request.session.save()
        try:
            cart_obj, cart_created = Cart.objects.get_or_create(cart_session_id=self.request.session.session_key)
        except MultipleObjectsReturned:
            cart_obj = Cart.objects.filter(cart_session_id=self.request.session.session_key).first()

        try:
            category = Category.objects.filter(title='Accessories - Gutter Guard').first()
            context['description'] = category.description
            context['description_bottom'] = category.description_bottom
        except:
            pass

        context['cart'] = cart_obj
        context['title'] = 'Accessories - Gutter Guard'
        context['meta_title'] = 'Gutter Guard | Metal Roofing Online'
        context['meta_description'] = 'Gutter Guard. Simple & easy installation. Order online. Protect your gutters from getting clogged with leaves & debris.'

        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.filter(categoryoption__option__category='Gutter Guard')


class FoamStripsListView(ListView):
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(FoamStripsListView, self).get_context_data(
            *args, **kwargs)
        self.request.session.save()
        try:
            cart_obj, cart_created = Cart.objects.get_or_create(cart_session_id=self.request.session.session_key)
        except MultipleObjectsReturned:
            cart_obj = Cart.objects.filter(cart_session_id=self.request.session.session_key).first()

        try:
            category = Category.objects.filter(title='Accessories - Foam Strips').first()
            context['description'] = category.description
            context['description_bottom'] = category.description_bottom
        except:
            pass

        context['cart'] = cart_obj
        context['title'] = 'Accessories - Foam Strips'
        context['meta_title'] = 'Foam End Closure Strips | Metal Roofing Online'
        context['meta_description'] = 'Foam End Closure Strips. Corrugated, greca, trimdek & more. Order online. Fast delivery & low prices. Easy ordering roofing materials.'


        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.filter(categoryoption__option__category='Foam Strips')


class RoofingToolsListView(ListView):
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(RoofingToolsListView, self).get_context_data(
            *args, **kwargs)
        self.request.session.save()
        try:
            cart_obj, cart_created = Cart.objects.get_or_create(cart_session_id=self.request.session.session_key)
        except MultipleObjectsReturned:
            cart_obj = Cart.objects.filter(cart_session_id=self.request.session.session_key).first()

        try:
            category = Category.objects.filter(title='Accessories - Roofing Tools').first()
            context['description'] = category.description
            context['description_bottom'] = category.description_bottom
        except:
            pass

        context['cart'] = cart_obj
        context['title'] = 'Accessories - Roofing Tools'
        context['meta_title'] = 'Roofing Tools | Metal Roofing Online'
        context['meta_description'] = 'Metal Roofing Tools. Turn Up tools, tin snips, rivet gun & more. Order online. Lowest prices. Fast delivery. Easy ordering'


        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.filter(categoryoption__option__category='Roofing Tools')


class DownpipeAccessoriesListView(ListView):
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DownpipeAccessoriesListView, self).get_context_data(
            *args, **kwargs)
        self.request.session.save()
        try:
            cart_obj, cart_created = Cart.objects.get_or_create(cart_session_id=self.request.session.session_key)
        except MultipleObjectsReturned:
            cart_obj = Cart.objects.filter(cart_session_id=self.request.session.session_key).first()

        try:
            category = Category.objects.filter(title='Accessories - Downpipe Accessories').first()
            context['description'] = category.description
            context['description_bottom'] = category.description_bottom
        except:
            pass

        context['cart'] = cart_obj
        context['title'] = 'Accessories - Downpipe Accessories'
        context['meta_title'] = 'Downpipe Accessories | Metal Roofing Online'
        context['meta_description'] = 'Downpipe Accessories. Colorbond Downpipe clips, nozzles & more. Order online. Lowest prices. Fast delivery of metal roofing materials.'

        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.filter(categoryoption__option__category='Downpipe Accessories')


class FacsiaAccessoriesListView(ListView):
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(FacsiaAccessoriesListView, self).get_context_data(
            *args, **kwargs)
        self.request.session.save()
        try:
            cart_obj, cart_created = Cart.objects.get_or_create(cart_session_id=self.request.session.session_key)
        except MultipleObjectsReturned:
            cart_obj = Cart.objects.filter(cart_session_id=self.request.session.session_key).first()

        try:
            category = Category.objects.filter(title='Accessories - Fascia Accessories').first()
            context['description'] = category.description
            context['description_bottom'] = category.description_bottom
        except:
            pass

        context['cart'] = cart_obj
        context['title'] = 'Accessories - Fascia Accessories'
        context['meta_title'] = 'Fascia Accessories | Metal Roofing Online'
        context['meta_description'] = 'Fascia Accessories. Colorbond & Zincalume fascia spring clips & more. Order online. Lowest prices. Fast delivery of metal roofing materials.'


        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.filter(categoryoption__option__category='Fascia Accessories')


class AdhesiveProductsListView(ListView):
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(AdhesiveProductsListView, self).get_context_data(
            *args, **kwargs)
        self.request.session.save()
        try:
            cart_obj, cart_created = Cart.objects.get_or_create(cart_session_id=self.request.session.session_key)
        except MultipleObjectsReturned:
            cart_obj = Cart.objects.filter(cart_session_id=self.request.session.session_key).first()

        try:
            category = Category.objects.filter(title='Accessories - Adhesive Products').first()
            context['description'] = category.description
            context['description_bottom'] = category.description_bottom
        except:
            pass

        context['cart'] = cart_obj
        context['title'] = 'Accessories - Adhesive Products'
        context['meta_title'] = 'Adhesive Products | Metal Roofing Online'
        context['meta_description'] = 'Adhesive Products for all your metal roofing needs. Anti noise tape, silicone & more. Order online. Lowest prices. Fast delivery of metal roofing materials.'

        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.filter(categoryoption__option__category='Adhesive Products')
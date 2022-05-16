from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_bag(request):
    ''' A view to render the shopping bag page '''

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    ''' Add the quantity of the selected product to the shopping bag '''

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    color = None
    if 'product_color' in request.POST:
        color = request.POST['product_color']
    bag = request.session.get('bag', {})

    if color:
        if item_id in list(bag.keys()):
            if color in bag[item_id]['items_by_color'].keys():
                bag[item_id]['items_by_color'][color] += quantity
                messages.success(request, f'Updated color {color.upper()} \
                    {product.name} quantity to \
                        {bag[item_id]["items_by_color"][color]}')
            else:
                bag[item_id]['items_by_color'][color] = quantity
                messages.success(request, f'Added color {color.upper()} \
                    {product.name} to your bag')
        else:
            bag[item_id] = {'items_by_color': {color: quantity}}
            messages.success(request, f'Added color {color.upper()} \
                {product.name} to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    ''' Update the selected product in the shopping bag '''

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    color = None
    if 'product_color' in request.POST:
        color = request.POST['product_color']
    bag = request.session.get('bag', {})

    if color:
        if quantity > 0:
            bag[item_id]['items_by_color'][color] = quantity
            messages.success(request, f'Updated color {color.upper()} \
                {product.name} quantity to \
                    {bag[item_id]["items_by_color"][color]}')
        else:
            del bag[item_id]['items_by_color'][color]
            if not bag[item_id]['items_by_color']:
                bag.pop(item_id)
            messages.success(request, f'Removed color {color.upper()} \
                {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} \
                quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        color = None
        if 'product_color' in request.POST:
            color = request.POST['product_color']
        bag = request.session.get('bag', {})

        if color:
            del bag[item_id]['items_by_color'][color]
            if not bag[item_id]['items_by_color']:
                bag.pop(item_id)
            messages.success(request, f'Removed color {color.upper()} \
                {product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

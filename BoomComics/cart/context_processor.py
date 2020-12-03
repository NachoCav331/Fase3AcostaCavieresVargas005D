def cart_total(request):
    total= 0
    for key, value in request.session['cart'].items():
        total = total + (int(value['precio']) * value['cantidad'])
    return {'cart_total': total}    

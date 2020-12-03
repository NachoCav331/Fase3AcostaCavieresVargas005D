class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

    def add(self, comic):
        if str(comic.id) not in self.cart.keys():
            self.cart [ str(comic.id)] = {
                "comic_id": str(comic.id),
                "titulo": comic.titulo,
                "cantidad": 1,
                "precio": str(comic.precio),
                "imagen": comic.imagen.url
            }
        else:
            for key, value in self.cart.items():
                if key == str(comic.id):
                    value["cantidad"] = value["cantidad"] + 1
                    break
        self.save()

    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def remove(self, comic):
        comic_id = str(comic.id)
        if comic_id in self.cart:
            del self.cart[comic_id]
            self.save()

    def decrement(self, comic):
        for key, value in self.cart.items():
            if key == str(comic.id):
                value["cantidad"] = value["cantidad"] - 1
                if value["cantidad"] < 1:
                    self.remove(comic)
                else:
                    self.save()
                break
            else:
                print("El producto no existe en el carrito")

    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True

        
                 
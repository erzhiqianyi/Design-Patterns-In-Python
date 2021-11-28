from estate_app.apartment import Apartment
from estate_app.purchase import Purchase


class ApartmentPurchase(Purchase, Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)

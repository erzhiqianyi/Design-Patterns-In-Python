from estate_app.apartment import Apartment
from estate_app.rental import Rental


class ApartmentRental(Rental, Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)

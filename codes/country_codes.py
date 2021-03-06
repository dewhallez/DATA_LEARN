from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return the pygal 2-digit country code for the given country."""

    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None


print(get_country_code('Nigeria'))
print(get_country_code('United Arab Emirates'))
print(get_country_code('Gambia'))


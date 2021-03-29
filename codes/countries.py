from pygal.maps.world import COUNTRIES
# from pygal.maps.world import i18n

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])


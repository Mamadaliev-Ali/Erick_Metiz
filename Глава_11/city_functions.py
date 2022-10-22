def get_country_city(country, city, population=''):
    if population:
        world = f"{country} {city} {population}"
    else:
        world = f"{country} {city}"
    return world.title()

def city_country(city, country, population=None, language=None):
    """Return a string formatted as 'City, Country'."""
    if population is not None:
        if language is not None:
            return f"{city.title()}, {country.title()} - Population: {population}, {language}"
        return f"{city.title()}, {country.title()} - Population: {population}"
    if language is not None:
        return f"{city.title()}, {country.title()}, {language}"
    return f"{city.title()}, {country.title()}"

print(city_country("new York", "united States"))
print(city_country("paris", "france", 2000000))
print(city_country("tokyo", "japan", 13000000, "Japanese"))
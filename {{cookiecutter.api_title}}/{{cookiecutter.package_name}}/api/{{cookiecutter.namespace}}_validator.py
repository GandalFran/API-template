#!/usr/bin/python3

# Copyright {% now 'local', '%Y' %} {{cookiecutter.organization}}
# See LICENSE for details.
# Author: {{cookiecutter.author}} @{{cookiecutter.author_github}} on GitHub

def validator(json_data_to_validate):

    violated_rules = []
    # to check
    if not( json_data_to_validate["temperature"] >= 0):
        violated_rules.append("Temperature out of bounds. Must be a value greater than 0.")
    if not( 0 <= json_data_to_validate["soil_humidity"] and json_data_to_validate["soil_humidity"] <= 100):
        violated_rules.append("Soil humidity out of bounds. Must be a value contained in [0,100].")
    if not( 0 <= json_data_to_validate["ambient_humidity"] and json_data_to_validate["ambient_humidity"] <= 100):
        violated_rules.append("Ambient humidity out of bounds. Must be a value contained in [0,100].")
    if not( json_data_to_validate["precipitation"] >= 0):
        violated_rules.append("Precipitation out of bounds. Must be a value greater than 0.")
    if not( json_data_to_validate["soil_type"] in list(range(4))):
        violated_rules.append("Soil type out of bounds. Must be one of the values [0,1,2,3], where {0: arcilloso, 1: franco_arenoso, 2: franco_arcilloso, 3: arenoso}.")
    if not( json_data_to_validate["plant_variety"] in list(range(4))):
        violated_rules.append("Plant variety out of bounds. Must be one of the values [0,1,2,3], where {0: tempranillo_clon_muy_vigoroso, 1: tempranillo_clon_vigor_medio, 2: cabernet, 3: merlot}.")
    if not( 0 <= json_data_to_validate["NDVI"] and json_data_to_validate["NDVI"] <= 1):
        violated_rules.append("NDVI out of bounds. Must be a value contained in [0,1].")
    if not( json_data_to_validate["temperature_forecast"] >= 0):
        violated_rules.append("Temperature forecast out of bounds. Must be a value greater than 0.")
    if not( json_data_to_validate["precipitation_forecast"] >= 0):
        violated_rules.append("Precipitation forecast out of bounds. Must be a value greater than 0.")
    if not( json_data_to_validate["season"] in list(range(4))):
        violated_rules.append("Season out of bounds. Must be one of the values [0,1,2,3], where {0: primavera, 1: verano, 2: otoño, 3: invierno}.")

    if violated_rules:
        # compound messages if available
        errors = ". ".join(violated_rules)
        return None, errors
    else:
        return json_data_to_validate, None
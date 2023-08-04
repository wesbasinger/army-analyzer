import xml.etree.ElementTree as ET

from army import Army
from unit import Unit
from model import Model
from weapon import Weapon

document = ET.parse("sample.xml")

parsed_army = document.getroot()

army = Army(parsed_army.attrib['name'], int(parsed_army.attrib['points']))

parsed_units = parsed_army.findall('unit')

for parsed_unit in parsed_units:
    
    unit = Unit(parsed_unit.attrib['name'])
    
    parsed_models = parsed_unit.findall('model')

    for parsed_model in parsed_models:

        model = Model(
                    parsed_model.attrib['name'],
                    int(parsed_model.find('movement').text),
                    int(parsed_model.find('toughness').text),
                    int(parsed_model.find('save').text),
                    int(parsed_model.find('wounds').text),
                    int(parsed_model.find('leadership').text),
                    int(parsed_model.find('objective-control').text))
        
        parsed_weapons = parsed_model.find('weapons')

        for parsed_weapon in parsed_weapons:

            try:

                skill = int(parsed_weapon.find('bs').text)

            except AttributeError:

                skill = int(parsed_weapon.find('ws').text)

            weapon = Weapon(
                parsed_weapon.attrib['name'],
                parsed_weapon.attrib['type'],
                parsed_weapon.find('attacks').text,
                skill,
                int(parsed_weapon.find('strength').text),
                int(parsed_weapon.find('ap').text),
                parsed_weapon.find('damage').text)

            model.add_weapon(weapon)
        
        for i in range(int(parsed_model.attrib['count'])):

            unit.add_model(model)

    for i in range(int(parsed_unit.attrib['count'])):

        army.add_unit(unit)

print("total model count: ", army.get_total_model_count())
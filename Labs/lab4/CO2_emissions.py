import csv
import sys
from pygal.style import Style
from pygal.maps.world import World
from pygal.maps.world import COUNTRIES



def country_code(country):
    for code, country_name in COUNTRIES.items():
        if country_name == country:
            return code
    return None

country_mapping = {'Bolivia': 'Bolivia, Plurinational State of',
                   'Cabo Verde': 'Cape Verde',
                   'Congo, Rep.': 'Congo',
                   'Dominica': 'Dominican Republic',
                   'Egypt, Arab Rep.': 'Egypt',
                   'Gambia, The': 'Gambia',
                   'Hong Kong SAR, China': 'Hong Kong',
                   'Iran, Islamic Rep.': 'Iran, Islamic Republic of',
                   'Kyrgyz Republic': 'Kyrgyzstan',
                   'Korea, Rep.': 'Korea, Republic of',
                   'Lao PDR': "Lao People's Democratic Republic",
                   'Libya': 'Libyan Arab Jamahiriya',
                   'Macao SAR, China': 'Macao',
                   'Moldova': 'Moldova, Republic of',
                   'Macedonia, FYR': 'Macedonia, the former Yugoslav Republic of',
                   'Korea, Dem. People’s Rep.': "Korea, Democratic People's Republic of",
                   'Slovak Republic': 'Slovakia',
                   'Tanzania': 'Tanzania, United Republic of',
                   'Venezuela, RB': 'Venezuela, Bolivarian Republic of',
                   'Vietnam': 'Viet Nam',
                   'Yemen, Rep.': 'Yemen',
                   'Congo, Dem. Rep.': 'Congo, the Democratic Republic of the'}

datafile = 'API_EN/API_EN.ATM.CO2E.KT_DS2_en_csv_v2.csv'

emissions = {}
no_data = {}

try:
    with open(datafile) as csvfile:
        file = csv.reader(csvfile)
        for _ in range(5):
            next(file)
        for line in file:
            country = line[0]
            if country in country_mapping:
                country = country_mapping[country]
            code = country_code(country)
            if code:
                emission = line[-6]
                if emission:
                    emissions[code] = float(emission)
                else:
                    no_data[code] = '?'                   
            else:
                print('Leaving out {}'.format(country))
except FileNotFoundError:
    print('Could not open {}, giving up.'.format(datafile))
    sys.exit()

emissions_map = World(style = Style(colors = ('#B22222', '#A9A9A9'), tooltip_font_size = 8,
                      legend_font_size = 10))
emissions_map.title = 'CO2 emissions in 2011'
emissions_map.add('Known data', emissions)
emissions_map.add('No data', no_data)
emissions_map.render_to_file('CO2_emissions.svg')



import json
import os
from pandas import DataFrame
from natsort import natsorted
directory = "json/"

nft = []
topSpeed = []
acceleration = []
braking = []
responsiveness = []
batteryEfficiency = []
energyRegeneration = []

files = natsorted(os.listdir(directory))

for filename in files:
    file = open(directory + filename)
    data = json.load(file)
    row = []
    for index in range(8, 13):
        row.append(data['attributes'][index]['value'])
    
    nft.append(str(data['name'])[20:])
    topSpeed.append(data['attributes'][8]['value'])
    acceleration.append(data['attributes'][9]['value'])
    braking.append(data['attributes'][10]['value'])
    responsiveness.append(data['attributes'][11]['value'])
    batteryEfficiency.append(data['attributes'][12]['value'])
    energyRegeneration.append(data['attributes'][13]['value'])

    df = DataFrame({'NFT': nft,
                    'Top Speed': topSpeed, 
                    'Acceleration': acceleration, 
                    'Braking': braking, 
                    'Responsiveness': responsiveness, 
                    'Battery Efficiency': batteryEfficiency, 
                    'Energy Regeneration': energyRegeneration})

    df.to_excel('out.xlsx', sheet_name='nft', index=False)

print(df)
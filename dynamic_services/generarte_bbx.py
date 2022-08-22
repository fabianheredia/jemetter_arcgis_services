import ssl
from webbrowser import get
import requests as req
import urllib.request
import random
import json
import pandas as pd

info_service = {}
levels = [50, 100, 200, 1000]


def get_service_info(url: str, own_exted=False):
    values = {"f": "json"}
    with req.get(url, params=values, verify=False) as response:
        if response.status_code == 200:
            result = json.loads(response.content)
            info_service = {'url': url,
                            'num_layers': len(result['layers']),
                            'is_Dinamic': result['supportsDynamicLayers'],
                            'spatial_reference': result['spatialReference']['wkid'],
                            }
        else:
            return None

        if own_exted == False:
            info_service['fullExtent'] = {"xmin": -78,
                                          "ymin": -2,
                                          "xmax": -68,
                                          "ymax": 9}
    return info_service


def get_bbx(level, num_vals, bbx):
    bbx_parcial = []
    len_x = bbx['xmax']-bbx['xmin']
    len_y = bbx['ymax']-bbx['ymin']
    part_x = len_x/level
    part_y = len_y/level
    num_vals = round(num_vals)
    for i in range(0, num_vals):
        x_ale = random.uniform(bbx['xmax'], bbx['xmin'])
        y_ale = random.uniform(bbx['ymax'], bbx['ymin'])
        bbx_parcial.append({'xmin': x_ale, 'ymin': y_ale,
                           'xmax': x_ale+part_x, 'ymax': y_ale+part_y})
    return bbx_parcial


def calculate_bbx(num_test, info, path):
    bbx_test = []
    num_test_level = int(num_test)/len(levels)
    for level in levels:
        bbx_test += get_bbx(level, num_test_level, info['fullExtent'])
    df = pd.DataFrame(bbx_test)
    df.to_csv(path)


def to_csv(data):
    print('generando...')

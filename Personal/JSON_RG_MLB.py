import requests
import pandas as pd
from pandas.io.json import json_normalize
from pandas import DataFrame
import numpy as np
import itertools
import requests
import json
import pandas
import csv


# # Quarterbacks
# qb = requests.get('https://d1qacz8ndd7avl.cloudfront.net/lineuphq/v1.00/2019-03-28/2/base/mlb-hitter.json')
#
# QB = qb.json()['data']['results']
#
# qb_proj = pd.DataFrame.from_dict(QB)
#
# for i in qb_proj:
#     print(qb_proj[i]['player']['first_name'], qb_proj[i]['player']['last_name'],",",qb_proj[i]['fpts']['2'],qb_proj[i]['batting_order']['order'],qb_proj[i]['batting_order']['confirmed'])
#
#
#
# # Quarterbacks
# qb = requests.get('https://d1qacz8ndd7avl.cloudfront.net/lineuphq/v1.00/2019-03-28/2/base/mlb-pitcher.json')
#
# QB = qb.json()['data']['results']
#
# qb_proj = pd.DataFrame.from_dict(QB)
#
# for i in qb_proj:
#     print(qb_proj[i]['player']['first_name'], qb_proj[i]['player']['last_name'],",",qb_proj[i]['fpts']['2'])
#

#
# batter = requests.get('https://d1qacz8ndd7avl.cloudfront.net/lineuphq/v1.00/2019-03-28/2/base/mlb-hitter.json')
#
# json_file='/Users/adamsardinha/Desktop/SS.json'
# with open(json_file, 'r') as json_data:
#     x = json.load(json_data)
#
# f = csv.writer(open("/Users/adamsardinha/Desktop/DFS Files/Projections/SaberSim_Projections/NHL/CSV/Nov4-4game.csv", "w"))
#
# f.writerow(["name", "fd_points", "position", "line_pos"])
# for player in x['players']:
#     f.writerow([
#                 player["name"],
#                 player["fd_points"],
#                 player["position"],
#                 player["line_pos"],])


url = 'https://d1qacz8ndd7avl.cloudfront.net/lineuphq/v1.00/2019-04-01/2/base/mlb-hitter.json'
page = requests.get(url)
page_json = json.loads(page.text)['data']['results']

# pOWN = page_json.get("ownership")
# pOWN_value = pOWN.setdefault("ownership")

batter = csv.writer(open("/Users/adamsardinha/Desktop/DFS Files/Projections/Rotogrinders/MLB/April1.csv",'w'))
batter.writerow(["Name", "FD Points", "pOWN","Batting Order"])
for x in page_json:
    batter.writerow([page_json[x]['player']["first_name"] + " " + page_json[x]['player']["last_name"],
                page_json[x]["fpts"]["2"],
                page_json[x]["ownership"]['2'],
                # page_json[x]['batting_order']["order"],
                # pOWN,
    ])

#
url = 'https://d1qacz8ndd7avl.cloudfront.net/lineuphq/v1.00/2019-04-01/2/base/mlb-pitcher.json'
page = requests.get(url)
page_json = json.loads(page.text)['data']['results']
pitcher = csv.writer(open("/Users/adamsardinha/Desktop/DFS Files/Projections/Rotogrinders/MLB/April1_Pitchers.csv",'w'))
pitcher.writerow(["Name", "FD Points","pOWN","Batting Order"])
for x in page_json:
    pitcher.writerow([page_json[x]['player']["first_name"] + " " + page_json[x]['player']["last_name"],
                page_json[x]["fpts"]["2"],
                page_json[x]['ownership']["2"],
    ])


with open('/Users/adamsardinha/Desktop/DFS Files/Projections/Rotogrinders/MLB/April1_Pitchers.csv', 'r') as f1:
    original = f1.read()

with open('/Users/adamsardinha/Desktop/DFS Files/Projections/Rotogrinders/MLB/April1.csv', 'a') as f2:
    f2.write('\n')
    f2.write(original)
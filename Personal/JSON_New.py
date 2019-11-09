import requests
import pandas as pd
from pandas import DataFrame
import numpy as np
import itertools

# Quarterbacks
qb = requests.get('https://d1qacz8ndd7avl.cloudfront.net/lineuphq/v1.00/2019-11-03/1/base/nfl-qb.json')

QB = qb.json()['data']['results']

qb_proj = pd.DataFrame.from_dict(QB)

for i in qb_proj:
    print(qb_proj[i]['player']['first_name'], qb_proj[i]['player']['last_name'],",", qb_proj[i]['fpts']['2'])

# Wide Receivers
wr = requests.get('https://d1qacz8ndd7avl.cloudfront.net/lineuphq/v1.00/2019-11-03/1/base/nfl-wr.json')

WR = wr.json()['data']['results']

wr_proj = pd.DataFrame.from_dict(WR)

for i in wr_proj:
    print(wr_proj[i]['player']['first_name'], wr_proj[i]['player']['last_name'],",", wr_proj[i]['fpts']['2'])

# Tight Ends
te = requests.get('https://d1qacz8ndd7avl.cloudfront.net/lineuphq/v1.00/2019-11-03/1/base/nfl-te.json')

TE = te.json()['data']['results']

te_proj = pd.DataFrame.from_dict(TE)

for i in te_proj:
    print(te_proj[i]['player']['first_name'], te_proj[i]['player']['last_name'],",", te_proj[i]['fpts']['2'])

# Running Back
rb = requests.get('https://d1qacz8ndd7avl.cloudfront.net/lineuphq/v1.00/2019-11-03/1/base/nfl-rb.json')

RB = rb.json()['data']['results']

rb_proj = pd.DataFrame.from_dict(RB)

for i in rb_proj:
    print(rb_proj[i]['player']['first_name'], rb_proj[i]['player']['last_name'],",", rb_proj[i]['fpts']['2'])

# Defense
defense = requests.get('https://d1qacz8ndd7avl.cloudfront.net/lineuphq/v1.00/2019-11-03/1/base/nfl-defense.json')

DEF = defense.json()['data']['results']

def_proj = pd.DataFrame.from_dict(DEF)

for i in def_proj:
    print(def_proj[i]['player']['first_name'], def_proj[i]['player']['last_name'],",", def_proj[i]['fpts']['2'])


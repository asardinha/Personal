import requests
import pandas as pd
from pandas.io.json import json_normalize
from pandas import DataFrame
import numpy as np
import itertools
import requests
import json
import pandas


# Quarterbacks
qb = requests.get('https://d1qacz8ndd7avl.cloudfront.net/lineuphq/v1.00/2019-11-01/3/base/nba-player.json')

QB = qb.json()['data']['results']

qb_proj = pd.DataFrame.from_dict(QB)

for i in qb_proj:
    print(qb_proj[i]['player']['first_name'], qb_proj[i]['player']['last_name'],",",qb_proj[i]['fpts']['2'],",",qb_proj[i]['minutes'],",",qb_proj[i]['ownership']['2'])
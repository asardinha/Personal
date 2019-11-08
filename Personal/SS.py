
import json
import csv


# with open('/Users/adamsardinha/Desktop/SS.json') as f:
#   data = json.load(f)
#
#
#
# for player in data['players']:
#   print(player['name'], ",", player['fd_points'], ",", player['position'],",", player['line_pos'])

# for player in data['players']:
#   print(player['name'], ",", player['fd_points'], ",", player['position'],",", player['line_pos'],",", player['actual'])
#
# for player in data['players']:
#   print(player['name'], ",", player['fd_points'], ",", player['minutes'],",", player['proj_own'],",", player['value'])

# NHL Pull

json_file='/Users/adsardin/Desktop/SS.json'
with open(json_file, 'r') as json_data:
    x = json.load(json_data)

f = csv.writer(open("/Users/adsardin/Desktop/Personal/Nov7-4game.csv", "w"))

f.writerow(["name", "fd_points", "position", "line_pos","actual score"])
for player in x['players']:
    f.writerow([
                player["name"],
                player["fd_points"],
                player["position"],
                player["line_pos"],
                player["actual"],
]
    )

# NBA Pull
# json_file = '/Users/adamsardinha/Desktop/SS.json'
# with open(json_file, 'r') as json_data:
#   x = json.load(json_data)
#
# f = csv.writer(
#   open("/Users/adamsardinha/Desktop/DFS Files/Projections/SaberSim_Projections/NBA/Oct31-3game.csv", "w"))
#
# f.writerow(["name", "fd_points", "position", "value"])
# for player in x['players']:
#   f.writerow([
#     player["name"],
#     player["fd_points"],
#     player["position"],
#     player["value"],
#
#   ])

# MLB Pull

# json_file = '/Users/adamsardinha/Desktop/SS.json'
# with open(json_file, 'r') as json_data:
#   x = json.load(json_data)
#
# f = csv.writer(
#   open("/Users/adamsardinha/Desktop/DFS Files/Projections/SaberSim_Projections/MLB/July13-11game.csv", "w"))
#
# f.writerow(["name", "fd_points", "position","actual","batting order"])
# for player in x['players']:
#   f.writerow([
#     player["name"],
#     player["fd_points"],
#     player["position"],
#     player["actual"],
#   ])


import json
from pathlib import Path
home = str(Path.home())


formatted_results = []
iconURL='{"type": "fileicon","path": "/Applications/Google Chrome.app"}'

file = open(home + "/Library/Application Support/Google/Chrome/Local State", "r")
example = file.read()
file.close()

parsedJSON = json.loads(example)
profile = parsedJSON['profile']
profil = profile['info_cache']

for item in profil:
    result = {
            "title": str(profil[str(item)]['name']),
            "arg": str(item),
            "icon": 'pic'
        }
    formatted_results.append(result)


values = ','.join(str(v) for v in formatted_results)
output = '{"items": ['+ values + ']}'
output = output.replace('pic',iconURL)
output = output.replace("'",'"')
output = output.replace('"{"type"','{"type"')
output = output.replace('}"}','}}')




print(output)

#!/usr/bin/python3
# iselect.py
# Aug-2021 Ton Smeele - Utrecht University
# All rights reserved
# 

from pathlib import Path
import json
import subprocess

# input file IRODSZONESFILE
# format must be: 
#   { "zone1": { "description" : "This is zone 1",
#                "config" : { ... }
#              },
#     "zone2": { ... }
#   }
# where the "config" json object will be the content for the outputfile
IRODSZONESFILE = './irods_zones.json'
#
# output file IRODSENVFILE:
IRODSENVFILE = './irods_environment.json'

def readFile(textfile):
    with textfile.open(mode = 'rt') as f:
        data = f.read()
    f.close()
    return data 

def writeFile(textfile, data):
    parentDir = textfile.parent
    if not textfile.parent.is_dir():
        # create dir(s) if nonexistent
        textfile.parent.mkdir(parents = True)
    with textfile.open(mode = 'wt+') as f:
        f.write(data)
    f.close()

def selector(zones):
    zoneChosen = ''
    while zoneChosen not in zones:
        print('Name: - Description:')
        for name, props in zones.items():
            print(name + "\t : " + props['description'])
        if not zoneChosen == '':
            print('\nSorry, your input was not recognized as a name in the list')
        zoneChosen = input('\nPlease select a name from the list above: ').lower()
    return zoneChosen


def main():
    inPath = Path(IRODSZONESFILE).expanduser()
    outPath = Path(IRODSENVFILE).expanduser()
    if not inPath.is_file():
        print('Required inputfile ' + str(inPath) + ' not found.')
        exit(1)
    data = readFile(inPath)
    zones = json.loads(data)
    zoneChosen = selector(zones)
    data = json.dumps(zones[zoneChosen]['config'])
    writeFile(outPath, data)
    print('Config written to ' + str(outPath))
    subprocess.run(['iinit'])

# main program
if __name__ == "__main__":
    main()

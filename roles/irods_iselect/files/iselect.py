#!/usr/bin/python3
# iselect.py
# Aug-2021 Ton Smeele - Utrecht University
# All rights reserved
# 

VERSION =  'iselect release 1.0'
IRODSZONESFILE = '/etc/irods_zones.json'
IRODSENVFILE = '~/.irods/irods_environment.json'
from pathlib import Path
import json
import sys
import subprocess
import getopt

# input file IRODSZONESFILE
# format must be: 
#   { "zone1": { "description" : "This is zone 1",
#                "config" : { ... }
#              },
#     "zone2": { ... }
#   }
# where the "config" json object will be used as outputfile content
#

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


def selector(zones, nameFilter):
    zoneChosen = nameFilter
    while zoneChosen not in zones:
        # see if user entered a partial name that uniquely matches
        hits = [i for i in zones if zoneChosen in i]
        if len(hits) == 1:
            zoneChosen = hits[0]
            print('Found "' + zoneChosen + '"')
            break
        if nameFilter == '':
            print('Name and Description:')
        else:
            print('Name and Description (filtered by "' + nameFilter + '"):')
        for name, props in sorted(zones.items()):
            if nameFilter in name:
                print(name + "\t : " + props['description'])
        if not zoneChosen == nameFilter:
            print('\nSorry, your input was not recognized as a name in the list')
        zoneChosen = input('\nPlease select a name from the list above: ').lower()
    return zoneChosen


def main(choice):
    inPath = Path(IRODSZONESFILE).expanduser()
    outPath = Path(IRODSENVFILE).expanduser()
    if not inPath.is_file():
        print('Required inputfile ' + str(inPath) + ' not found.')
        exit(1)
    data = readFile(inPath)
    zones = json.loads(data)
    zoneChosen = selector(zones, choice)
    data = json.dumps(zones[zoneChosen]['config'])
    writeFile(outPath, data)
    print('Config written to file ' + str(outPath))
    try:
        subprocess.run(['iinit'])
    except:
        print('Please run command "iinit" to complete configuration')

def help():
    text = 'Usage: iselect <name>\n' + \
    '<name> is used to filter the list\n' + \
    'When the filtered list is down to item, then this name is selected'
    print(text)


# main program
if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hv')
    except:
        help()
        exit(0)
    for opt, arg in opts:
        if opt.lower() == '-v':
            print(VERSION)
        if opt.lower() == '-h':
            help()
    if len(opts) > 0:
        exit(0)
    choice = ''
    if len(args) > 0:
        choice = args[0].lower()
    main(choice)

#!/usr/bin/python3
# iselect.py
# Aug-2021 Ton Smeele - Utrecht University
# All rights reserved
# 

VERSION =  'iselect release 1.1a'
IRODSZONESFILE = '/etc/irods_zones.json'

IRODSENVFILE = '~/.irods/irods_environment.json'
from pathlib import Path
import urllib.request
import json
import sys
import subprocess
import getopt
import re

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

def is_uri(text):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, text) is not None

def readLocation(url):
    with urllib.request.urlopen(url) as f:
        data = f.read().decode('utf-8')
    return data

def getZonesConfig(zonesfile):
    if is_uri(zonesfile):
        try:
           return readLocation(zonesfile)
        except:
           print('Unable to obtain zones configuration from url: ' + zonesfile)
           exit(1)
    inPath = Path(zonesfile).expanduser()
    if not inPath.is_file():
        print('Required inputfile ' + str(inPath) + ' not found.')
        exit(1)
    try:
        return readFile(inPath)
    except:
        print('Unable to read zones configuration file: ' + zonesfile)
        exit(2)

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
        try:
            zoneChosen = input('\nPlease select a name from the list above: ').lower()
        except:
            print('\nInput aborted by user')
            exit(1)
    return zoneChosen


def main(choice, zonesfile):
    outPath = Path(IRODSENVFILE).expanduser()
    data = getZonesConfig(zonesfile)
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
    text = '''
    Usage: iselect [-hva] [-f <location>]  [<name>]

    iselect allows the user to select an iRODS zone from a list of known zones
    and populates the user's irods_environment.json file with a configuration
    suitable for the selected zone.

    <name> is an optional argument used to filter the zones list to only show
    zones that have a name which contains the text <name>. 
    If only one zone meets the filter, then this zone is selected.

    Unless specified, the known zones list is loaded from a default location.

    Options:
     -h   help (this text)
     -v   iselect version
     -a   load alternative list of zones (shows non-production zones)
     -f <location>  load list of zones from the specified file or uri
    '''
    print(text)


# main program
if __name__ == "__main__":
    zonesfile = IRODSZONESFILE
    args_start = 0
    quit = False
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'ahvf')
    except:
        help()
        exit(0)
    for opt, arg in opts:
        if opt.lower() == '-v':
            print(VERSION)
            quit = True
        if opt.lower() == '-h':
            help()
            quit = True
        if opt.lower() == '-a':
            zonesfile = IRODSZONESFILE + '.acc'
        if (opt.lower() == '-f') and len(args) > 0:
            zonesfile = args[args_start]
            args_start = args_start + 1
    if quit:
        exit(0)
    choice = ''
    if len(args) > args_start:
        choice = args[args_start].lower()
    main(choice, zonesfile)

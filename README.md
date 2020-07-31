# sgtools

CLI tool to get fishing data, like tide info, fishery notice, shellfish closures etc. 

## Installation or re-installation

extract zip file to a dir, and cd into that dir you will see a setup.py inside the directory. Run
$ pip3 install .
If necessary, run to confirm both python3.7 and pip are installed properly. 
$ pip3 --version 
$ python3 --version

## Romoval
$ pip3 uninstall gofishing

## Usage

1. tide
    parse the list of stations out of https://tides.gc.ca/eng/station/list, and save to /tmp/stations.csv
    given station location and date, print tide predictions 
2. area
    parse the list of stations out of https://www.pac.dfo-mpo.gc.ca/fm-gp/maps-cartes/areas-secteurs/index-eng.html, and save to /tmp/areas.csv
    given a combo of 'name, category', print the following: 
        * area maps link: https://www.pac.dfo-mpo.gc.ca/fm-gp/rec/tidal-maree/a-s<area_id>-eng.html (special example, area 21/22 is using id 21 for map)
        * get protected areas, and put it into a csv file for all areas. (subarea_id, type, closure_name, closure_map)
        * contamination info: subarea_id, sanitory closure name, closure type, closure map link
        * species regulation: species 
        * latest fishery notice for any restriction of this species in this area. 
   

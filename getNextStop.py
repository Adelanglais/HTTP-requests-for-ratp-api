#/usr/bin/python3

import requests
from lxml import html, etree
import xml.etree as ElementTree

headers = {'keyapp':'FvChCBnSetVgTKk324rO', 'cmd':'getNextStopsRealtime','stopArea':'7'}
response = requests.get('http://apixha.ixxi.net/APIX', params = headers)

#print(response.content)

tree = etree.fromstring(response.content) #contient le fichier html
#r = tree.xpath("//directionId/destinationId/nextStopTime/text()")
retour = tree.xpath("//nextStopTime")
for r in retour:
    print(r.text)

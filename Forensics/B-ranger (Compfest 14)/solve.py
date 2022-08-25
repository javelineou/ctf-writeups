from pyshark import *
import binascii

import cv2
import numpy as np

packets = FileCapture('log.pcap', use_json=True, include_raw=True, override_prefs={'ssl.keylog_file': 'ssl.log'})

part1 = []
part2 = []

for packet in packets:  
    if hasattr(packet, 'http'):
        keys = packet.http._all_fields
        values = packet.http._all_fields.values()
        
        for key in keys:
            if 'HTTP/1.1 206 Partial Content' in key:
                img = {}
                for key, value in zip(keys, values):
                    if key == 'http.response_for.uri':
                        img['uri'] = value

                    if key == 'http.response.line':
                        img['pos'] = value[7].split(' ')[2].split('/')[0].split('-')

                    if key == 'http.file_data_raw':
                        img['data'] = binascii.unhexlify(value[0])

                if 'part_1' in img['uri']:
                    part1.append(img)
                else:
                    part2.append(img)
                
                break

        
part1.sort(key=lambda x: int(x['pos'][0]))
part2.sort(key=lambda x: int(x['pos'][0]))

out = open("part1.png", "wb")
for img in part1:
    out.write(img['data'])
out.close()

out = open("part2.png", "wb")
for img in part2:
    out.write(img['data'])
out.close()

img1 = cv2.imread('part1.png')
img2 = cv2.imread('part2.png')
img = np.concatenate((img1, img2), axis=1)
cv2.imshow('image', img)
cv2.waitKey(0)
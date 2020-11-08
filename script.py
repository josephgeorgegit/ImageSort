import json
import sys

def make():
    input = input('Enter Text file name>')
    links = []
    with open(input, "r") as in_file, open("output.json", 'w') as out_file:
        lines = in_file.read()
        split = lines.split()
        links = []

        for i, s in enumerate(split, 1):
            item = {"id": i, "url": s}
            links.append(item)

        json.dump(links, out_file, indent=4) 
      
make()      

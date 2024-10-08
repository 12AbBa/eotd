'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
This Python script helps to mass-produce the EoTD files.
Written by Royce Yao (mainly) and Zongshu Wu

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import os

# File names
from pathlib import Path

path = Path(__file__).parent

names = 'names.txt'
dates = 'dates.txt'
equations = 'equations.txt'

class Files:
    def __init__(self, names, dates, equations):
        self.names=[x.strip() for x in names]
        self.dates=[x.strip() for x in dates]
        self.equations=[x.strip() for x in equations]
        assert (len(names) == len(dates)) and (len(dates) == len(equations))
        
    def get_name(self, i):
        return self.names[i]

    def get_date(self, i):
        return self.dates[i]

    def get_equation(self, i):
        return self.equations[i]
        
    def __len__(self):
        return len(self.names)

# Read the files
with (path / names).open('r') as f1, (path / dates).open('r') as f2, (path / equations).open('r') as f3:
    names_lines = f1.readlines()
    dates_lines = f2.readlines()
    equations_lines = f3.readlines()

fi = Files(names_lines, dates_lines, equations_lines)

template = """# Equation of The Day

# Day {N}: {Na}

$${E}$$

<picture><img alt="Day {N}" src="{pN}.png"></picture>

<center>{quickref}</center>

[Back to Sector 2](../64-127.md)

<script data-goatcounter="https://zswu.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
<script src="https://utteranc.es/client.js" repo="12AbBa/eotd" issue-term="pathname" theme="github-light" crossorigin="anonymous" async> </script>"""


for i in range(64,len(fi)):
    quickref = ""

    # quickref text + links
    if i > 0:
        quickref += "<a href=\"" + str(i).zfill(4) + ".html\">#" + str(i) + "</a> $\\qquad\\leftarrow\\qquad$ "

    quickref += "#" + str(i+1) + " (" + fi.get_date(i) + ")"

    if i < len(fi) - 1:
        quickref += " $\\qquad\\rightarrow\\qquad$ <a href=\"" + str(i+2).zfill(4) + ".html\">#" + str(i+2) + "</a>"

    with (path / (f"output/{str(i+1).zfill(4)}.md")).open('w+') as wr:
        wr.write(template.format(
            N=str(i+1),
            pN=str(i+1).zfill(4),
            Na=fi.get_name(i),
            D=fi.get_date(i),
            E=fi.get_equation(i),
            quickref=quickref
        ))
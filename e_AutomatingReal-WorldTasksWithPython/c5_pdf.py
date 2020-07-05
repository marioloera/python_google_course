#!/usr/bin/env python3
import os
from reportlab.platypus import SimpleDocTemplate

# Each of these items (Paragraph, Spacer, Table, and Image) 
# are classes that build individual elements in the final document.
from reportlab.platypus import Paragraph, Spacer, Table, Image

# reportlab needs style for each part of the document , 
# so let's import some more things from the module to describe style.
from reportlab.lib.styles import getSampleStyleSheet

# The report object generate a PDF using the filename
filename = os.path.join('output', '000report.pdf')
report = SimpleDocTemplate(filename)

"""
You can make a style all of your own, 
but we’ll use the default provided by the module for these examples. 

The styles object now contains a default "sample" style. 
It’s like a dictionary of different style settings. 
If you've ever written HTML, the style settings will look familiar. 

For example h1 represents the style for the first level of headers. 
Alright, we're finally ready to give this report a title!
"""
styles = getSampleStyleSheet()
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])
# report.build([report_title]) # 001report.pdf

# To make a Table object, we need our data to be in a list-of-lists, 
# sometimes called a two-dimensional array. 
# We have our inventory of fruit in a dictionary.

fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

table_data = []
for k, v in fruit.items():
    table_data.append([k, v])

print('\ntable_data\n', table_data)

report_table = Table(data=table_data)
# report.build([report_title, report_table]) # 002report.pdf


# maybe we should add some style to report_table.
#  For our example, we'll add a border around all of the cells in our table, 
# and move the table over to the left. 
# TableStyle definitions can get pretty complicated, 
# so feel free to take a look at the documentation 
# for a more complete idea of what’s possible.

from reportlab.lib import colors
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
report.build([report_title, report_table]) # 003report.pdf

# Up to now, we've generated a report with a title and a table of data. 
# Next let's add something a little more graphical. 
# What could be better than a fruit pie (graph)?! 
# We’re going to need to use the Drawing Flowable class to create a Pie chart.

from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
inch = 2.54
report_pie = Pie(width=3*inch, height=3*inch)

# To add data to our Pie chart, we need two separate lists: 
# One for data, and one for labels. 
# Once more, we’re going to have to transform our fruit dictionary 
# into a different shape. 
# For an added twist, let's sort the fruit in alphabetical order:
report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)

print('\nreport_pie.data\n', report_pie.data)
print('\nreport_pie.labels\n', report_pie.labels)

# the Pie object isn’t Flowable, 
# but it can be placed inside of a Flowable Drawing.
report_chart = Drawing()
report_chart.add(report_pie)
report.build([report_title, report_table, report_chart])  # 004report.pdf
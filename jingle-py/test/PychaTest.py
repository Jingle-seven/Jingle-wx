# coding=utf8

import sys
import cairo
import pycha.line
from lines import lines


def lineChart(output):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 800, 400)
    dataSet = (
        ('lines', [(i, l[1]) for i, l in enumerate(lines)]),
    )
    options = {
        'axis': {
            'x': {
                'ticks': [dict(v=i, label=l[0]) for i, l in enumerate(lines)],
            },
            'y': {
                'tickCount': 4,
            }
        },
        'background': {
            'color': '#eeeeff',
            'lineColor': '#444444'
        },
        'colorScheme': {
            'name': 'gradient',
            'args': {
                'initialColor': 'blue',
            },
        },
        'legend': {
            'hide': True,
        },
    }
    chart = pycha.line.LineChart(surface, options)
    chart.addDataset(dataSet)
    chart.render()
    surface.write_to_png(output)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        output = sys.argv[1]
    else:
        output = 'linechart.png'
    lineChart(output)

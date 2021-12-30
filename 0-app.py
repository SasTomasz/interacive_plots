import justpy as jp
import pandas as pd
from datetime import datetime as dt

chart = '''
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Month Average Rating'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Rating'
        },
        labels: {
            format: '{value}'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
'''
def create_data():
    data = pd.read_csv('reviews.csv', parse_dates=['Timestamp'])
    data['Month'] = data['Timestamp'].dt.strftime("%Y-%m")
    month_average = data.groupby(['Month']).mean()
    return month_average


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Python course rating", classes="text-h3 text-center q-pa-md")
    hc = jp.HighCharts(a=wp, options=chart)
    data = create_data()
    hc.options.xAxis.categories = list(data.index)
    hc.options.series[0].data = list(data['Rating'])
    return wp

jp.justpy(app)
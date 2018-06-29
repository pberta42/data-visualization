import pandas
from bokeh.plotting import figure, output_file, show

# read dataset
df = pandas.read_csv('../Data/temperature.csv',
                     names=['record_id', 'month', 'day', 'year',
                            'AverageTemperatureFahr',
                            'AverageTemperatureUncertaintyFahr', 'City',
                            'country_id', 'Country', 'Latitude', 'Longitude'],
                     header=0)

# filter important columns
df2 = df.filter(items=['month', 'day', 'year',
                       'AverageTemperatureFahr', 'City'])

# fill missing data
df3 = df2.fillna(method='bfill', limit=50).fillna(method='ffill', limit=50)

# check for data completeness
if df3[pandas.isnull(df3).AverageTemperatureFahr].empty:
    print("Data is clean.")

# create DateTime column
df3 = df3.assign(Date=pandas.Series(
    pandas.to_datetime({'year': df3.year,
                        'month': df3.month,
                        'day': df3.day})).values)

df4 = df3.filter(items=['Date', 'AverageTemperatureFahr', 'City'])


#
# split by cities
#
# print(df3.City.unique())
# print(df3['City'].value_counts())
#
#dfOdesa = df3[df3.City=='Odesa']
#print(dfOdesa)
# dfParis = df3[df3.City=='Paris']
# dfStockholm = df3[df3.City=='Stockholm']
# dfUppsala = df3[df3.City=='Uppsala']


def small():
    start_date = pandas.to_datetime('2009-01-01')
    end_date = pandas.to_datetime('2011-01-01')

    plot = figure(plot_width=500, plot_height=400,
                  x_axis_type="datetime",
                  title='Temperature (F)')

    plot.line(df4[(df4.City == 'Paris') &
                  (df4.Date >= start_date) &
                  (df4.Date < end_date)].Date,
              df4[(df4.City == 'Paris') &
                  (df4.Date >= start_date) &
                  (df4.Date < end_date)].AverageTemperatureFahr,
              legend='Paris',
              line_color='#ef8dc8',
              line_width=2,
              line_cap='round')

    plot.legend.location = "bottom_left"
    plot.border_fill_color = "whitesmoke"
    output_file('small.html')

    show(plot)


def medium():
    start_date = pandas.to_datetime('2000-01-01')
    end_date = pandas.to_datetime('2010-01-01')

    plot = figure(plot_width=500, plot_height=400,
                  x_axis_type="datetime",
                  title='Temperature (F)')

    plot.line(df4[(df4.City == 'Odesa') &
                  (df4.Date >= start_date) &
                  (df4.Date < end_date)].Date,
              df4[(df4.City == 'Odesa') &
                  (df4.Date >= start_date) &
                  (df4.Date < end_date)].AverageTemperatureFahr,
              legend='Odesa',
              line_color='#5bb2ff',
              line_width=2,
              line_cap='round')

    plot.line(df4[(df4.City == 'Paris') &
                  (df4.Date >= start_date) &
                  (df4.Date < end_date)].Date,
              df4[(df4.City == 'Paris') &
                  (df4.Date >= start_date) &
                  (df4.Date < end_date)].AverageTemperatureFahr,
              legend='Paris',
              line_color='#ef8dc8',
              line_width=2,
              line_cap='round')

    plot.legend.location = "bottom_left"
    plot.border_fill_color = "whitesmoke"
    output_file('medium.html')

    show(plot)


def large():

    plot = figure(plot_width=500, plot_height=400,
                  x_axis_type="datetime",
                  title='Temperature (F)')

    plot.line(df4[df4.City == 'Odesa'].Date,
              df4[df4.City == 'Odesa'].AverageTemperatureFahr,
              legend='Odesa',
              line_color='#5bb2ff',
              line_width=2,
              line_cap='round')

    plot.line(df4[df4.City == 'Paris'].Date,
              df4[df4.City == 'Paris'].AverageTemperatureFahr,
              legend='Paris',
              line_color='#ef8dc8',
              line_width=2,
              line_cap='round')

    plot.line(df4[df4.City == 'Stockholm'].Date,
              df4[df4.City == 'Stockholm'].AverageTemperatureFahr,
              legend='Stockholm',
              line_color='#893aa5',
              line_width=2,
              line_cap='round')

    plot.line(df4[df4.City == 'Uppsala'].Date,
              df4[df4.City == 'Uppsala'].AverageTemperatureFahr,
              legend='Uppsala',
              line_color='#e8dd45',
              line_width=2,
              line_cap='round')

    plot.legend.location = "bottom_left"
    plot.border_fill_color = "whitesmoke"
    output_file('large.html')

    show(plot)

#small()
#medium()
large()


from django.shortcuts import render
from django.http import HttpResponse
from home.models import temp
from bokeh.embed import components
import  datetime
from bokeh.models import DatetimeTickFormatter
from bokeh.plotting import figure, output_file, show
from .models import *
from datetime import datetime as dt
import datetime
from math import pi

def default(request):
    #day = datetime.datetime.now()
    day="2020/01/24 00:45"
    x,y,mt,Mt,mtt,Mtt= neo4j("temperature", day)
    plot1 = figure(title="TEMPERATURE",x_axis_type='datetime',x_axis_label='Time', y_axis_label="Temperature", plot_width=680,
                  plot_height=400)
    plot1.line(x,y, line_width=2)
    plot1.xaxis.formatter = DatetimeTickFormatter(

        hours=["%b(%d)-%H:%M"],
        days=["%b(%d%)-%H:%M"],
        months=["%b(%d)-%H:%M"],
        years=["%b(%d%)-H:%M"],
    )
    plot1.xaxis.major_label_orientation = pi / 4
    tempes, tempe = components(plot1)

    mx,my,mm,Mm,mmt,Mmt= neo4j("moisture",day)
    plot2 = figure(title="SOIL MOISTURE",x_axis_type='datetime', x_axis_label='Time', y_axis_label="Soil Moisture", plot_width=680,
                  plot_height=400)
    plot2.line(mx, my, line_width=2)
    plot2.xaxis.formatter = DatetimeTickFormatter \
            (
            hours=["%b(%d)- %H :%M"],
            days=["%b(%d%)-%H:%M"],
            months=["%b(%d)- %H:%M"],
            years=["%b(%d%)-H:%M"],
        )
    plot2.xaxis.major_label_orientation = pi / 4
    moistures, moisture = components(plot2)

    hx,hy,mh,Mh,mht,Mht= neo4j("humidity",day)
    plot3 = figure(title="HUMIDITY",x_axis_type='datetime',x_axis_label='Time', y_axis_label="Humidity", plot_width=680,
                  plot_height=400)
    plot3.line(hx, hy, line_width=2)
    plot3.xaxis.formatter = DatetimeTickFormatter \
            (
            hours=["%b(%d)- %H :%M"],
            days=["%b(%d%)-%H:%M"],
            months=["%b(%d)- %H:%M"],
            years=["%b(%d%)-H:%M"],
        )
    plot3.xaxis.major_label_orientation = pi/4
    humiditys, humidity= components(plot3)

    lx,ly,ml,Ml,mlt,Mlt=neo4j("lightintensity",day)
    plot3 = figure(title="LIGHT INTENSITY", x_axis_label='Time',x_axis_type='datetime', y_axis_label="Light intensity", plot_width=680,
                   plot_height=400)
    plot3.line(lx, ly, line_width=2)
    plot3.xaxis.formatter = DatetimeTickFormatter \
            (
            hours=["%b(%d)- %H :%M"],
            days=["%b(%d%)-%H:%M"],
            months=["%b(%d)- %H:%M"],
            years=["%b(%d%)-H:%M"],
        )
    plot3.xaxis.major_label_orientation = pi / 4
    lights,light = components(plot3)

    cx,cy,cm,cM,mct,Mct =neo4j("co2", day)
    plot3 = figure(title="CO2 CONCENTRATION", x_axis_label='Time', y_axis_label="C02 concentration",x_axis_type='datetime', plot_width=680,
                   plot_height=400)
    plot3.line(cx, cy, line_width=2)
    plot3.xaxis.formatter = DatetimeTickFormatter \
            (
            hours=["%b(%d)- %H :%M"],
            days=["%b(%d%)-%H:%M"],
            months=["%b(%d)- %H:%M"],
            years=["%b(%d%)-H:%M"],
        )
    plot3.xaxis.major_label_orientation = pi / 4
    cos, co = components(plot3)
    return render(request, 'index.html',
                  {'co2': co,'mct':mct,'Mct':Mct,'cm': cm, 'cM': cM, 'co2s': cos, 'light': light,'mlt':mlt,'Mlt':Mlt, 'ml': ml, 'Ml': Ml, 'lights': lights,
                   'tempes': tempes,'mtt':mtt,'Mtt':Mtt, 'mt': mt, 'Mt': Mt, 'day': day, 'tempe': tempe, 'moistures': moistures,'mmt':mmt,'Mmt':Mmt, 'mm': mm,
                   'Mm': Mm, 'humiditys': humiditys, 'humidity': humidity,'mht':mht,'Mht':Mht, 'mh': mh, 'Mh': Mh, 'moisture': moisture})


def custom(request,day):
    date1=request.GET.get('dat')
    #day1= dt.strptime(date1,"%Y/%m/%d %H:%M")
    try:
        day = date1+" 00:00"
        x, y, mt, Mt, mtt, Mtt = neo4j("temperature", day)
        plot1 = figure(title="TEMPERATURE", x_axis_type='datetime', x_axis_label='Time', y_axis_label="Temperature",
                       plot_width=680,
                       plot_height=400)
        plot1.line(x, y, line_width=2)
        plot1.xaxis.formatter = DatetimeTickFormatter(

            hours=["%b(%d)-%H:%M"],
            days=["%b(%d%)-%H:%M"],
            months=["%b(%d)-%H:%M"],
            years=["%b(%d%)-H:%M"],
        )
        plot1.xaxis.major_label_orientation = pi / 4
        tempes, tempe = components(plot1)

        mx, my, mm, Mm, mmt, Mmt = neo4j("moisture", day)
        plot2 = figure(title="SOIL MOISTURE", x_axis_type='datetime', x_axis_label='Time', y_axis_label="Soil Moisture",
                       plot_width=680,
                       plot_height=400)
        plot2.line(mx, my, line_width=2)
        plot2.xaxis.formatter = DatetimeTickFormatter \
                (
                hours=["%b(%d)- %H :%M"],
                days=["%b(%d%)-%H:%M"],
                months=["%b(%d)- %H:%M"],
                years=["%b(%d%)-H:%M"],
            )
        plot2.xaxis.major_label_orientation = pi / 4
        moistures, moisture = components(plot2)

        hx, hy, mh, Mh, mht, Mht = neo4j("humidity", day)
        plot3 = figure(title="HUMIDITY", x_axis_type='datetime', x_axis_label='Time', y_axis_label="Humidity",
                       plot_width=680,
                       plot_height=400)
        plot3.line(hx, hy, line_width=2)
        plot3.xaxis.formatter = DatetimeTickFormatter \
                (
                hours=["%b(%d)- %H :%M"],
                days=["%b(%d%)-%H:%M"],
                months=["%b(%d)- %H:%M"],
                years=["%b(%d%)-H:%M"],
            )
        plot3.xaxis.major_label_orientation = pi / 4
        humiditys, humidity = components(plot3)

        lx, ly, ml, Ml, mlt, Mlt = neo4j("lightintensity", day)
        plot3 = figure(title="LIGHT INTENSITY", x_axis_label='Time', x_axis_type='datetime',
                       y_axis_label="Light intensity", plot_width=680,
                       plot_height=400)
        plot3.line(lx, ly, line_width=2)
        plot3.xaxis.formatter = DatetimeTickFormatter \
                (
                hours=["%b(%d)- %H :%M"],
                days=["%b(%d%)-%H:%M"],
                months=["%b(%d)- %H:%M"],
                years=["%b(%d%)-H:%M"],
            )
        plot3.xaxis.major_label_orientation = pi / 4
        lights, light = components(plot3)

        cx, cy, cm, cM, mct, Mct = neo4j("co2", day)
        plot3 = figure(title="CO2 CONCENTRATION", x_axis_label='Time', y_axis_label="C02 concentration",
                       x_axis_type='datetime', plot_width=680,
                       plot_height=400)
        plot3.line(cx, cy, line_width=2)
        plot3.xaxis.formatter = DatetimeTickFormatter \
                (
                hours=["%b(%d)- %H :%M"],
                days=["%b(%d%)-%H:%M"],
                months=["%b(%d)- %H:%M"],
                years=["%b(%d%)-H:%M"],
            )
        plot3.xaxis.major_label_orientation = pi / 4
        cos, co = components(plot3)
    except:
        tempe=humidity=moisture=light=co="INVALID DATE FORMAT("+ date1+")!!!                                " \
                                         " please insert date like ' 2002/01/01'"
        cm=cM=cos=ml=Ml=lights=tempes=mt=Mt=moistures=mm=Mm=humiditys=mh=Mh=''
        day="Wrong Imput("+date1+")"
        mct=mmt=mm=mtt=mlt=mht=Mht=Mmt=Mtt=Mlt=Mct=''
    return render(request, 'index.html',
                  {'co2': co, 'mct': mct, 'Mct': Mct, 'cm': cm, 'cM': cM, 'co2s': cos, 'light': light, 'mlt': mlt,
                   'Mlt': Mlt, 'ml': ml, 'Ml': Ml, 'lights': lights,
                   'tempes': tempes, 'mtt': mtt, 'Mtt': Mtt, 'mt': mt, 'Mt': Mt, 'day': day, 'tempe': tempe,
                   'moistures': moistures, 'mmt': mmt, 'Mmt': Mmt, 'mm': mm,
                   'Mm': Mm, 'humiditys': humiditys, 'humidity': humidity, 'mht': mht, 'Mht': Mht, 'mh': mh, 'Mh': Mh,
                   'moisture': moisture})


def neo4j(nodename, date1):
    node = temperature.nodes.all()
    start= dt.strptime(date1, "%Y/%m/%d %H:%M")
    if (nodename == 'temperature'):
        node = temperature.nodes.get(name='TEMPRATURE')
        title="Temperature"
    if (nodename == 'moisture'):
        node = moisture.nodes.get(name='MOISTURE')
        title='Moisture'
    if (nodename == 'humidity'):
        node = humidity.nodes.get(name='HUMIDITY')
        title='Humidity'
    if (nodename == 'lightintensity'):
        node = lightintensity.nodes.get(name='LIGHT')
        title='Light Intensity'
    if (nodename == 'co2'):
        node = co2.nodes.get(name='CO2')
        title='CO2 Concentration'
    times = time.nodes.get(name="TIME")
    datav = times.value
    days=[]
    values=[]
    for a in range(-1, (len(datav)-1)):
        a = a + 1
        if (start.day == datav[a].day ):

           if(start.month==datav[a].month):
              days.append(datav[a])
              values.append(node.value[a])
    max=values[0]
    min=values[0]
    for b in range(-1,(len(values)-1)):
        b=b+1
        if (values[b] >= max):
            max = values[b]
            u=days[b]
            maxt=u.strftime("%H:%M %p")
        if (values[b] <= min):
            min = values[b]
            mint=days[b].strftime("%H:%M %p")

    return days,values,min,max,mint,maxt


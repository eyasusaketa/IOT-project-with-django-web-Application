from datetime import datetime
from django.db import models
import  json
from neomodel import (config, StructuredNode,StringProperty, IntegerProperty,
    UniqueIdProperty, RelationshipTo ,ArrayProperty,DateTimeFormatProperty)

class greenhouse(StructuredNode):
    name=StringProperty()

class temp(StructuredNode):
    name=StringProperty()
    x=ArrayProperty(IntegerProperty())
    y = ArrayProperty(IntegerProperty())

class time(StructuredNode):
  name=StringProperty(requirrd=True)
  value=ArrayProperty(DateTimeFormatProperty(format="%Y/%m/%d %H:%M" ))

class moisture(StructuredNode):
    name=StringProperty()
    value=ArrayProperty(IntegerProperty())
    R=RelationshipTo(time,'RECORDED_AT')
class humidity(StructuredNode):
    name=StringProperty()
    value=ArrayProperty(IntegerProperty())
    R = RelationshipTo(time, 'RECORDED_AT')
class temperature(StructuredNode):
    name=StringProperty()
    value=ArrayProperty(IntegerProperty())
    R = RelationshipTo(time, 'RECORDED_AT')
class co2(StructuredNode):
    name=StringProperty()
    value=ArrayProperty(IntegerProperty())
    R = RelationshipTo(time, 'RECORDED_AT')
class lightintensity(StructuredNode):
    name=StringProperty()
    value=ArrayProperty(IntegerProperty())
    R = RelationshipTo(time, 'RECORDED_AT')
class starttime(StructuredNode):
    name=StringProperty()
    value=ArrayProperty(IntegerProperty())
class stoptime(StructuredNode):
    value=ArrayProperty(IntegerProperty())
    name=StringProperty()
class flowmeter(StructuredNode):
    name=StringProperty()
    value=ArrayProperty(IntegerProperty())
    total=IntegerProperty()
    stime=RelationshipTo(starttime,'START_AT')
    sttime=RelationshipTo(stoptime,'STOPPED_AT')
class valve(StructuredNode):
    name=StringProperty()
    ida=IntegerProperty()
    opened=RelationshipTo(starttime,'OPENED')
    closed=RelationshipTo(stoptime,'CLOSED')
class ventilator(StructuredNode):
    name=StringProperty()
    ida=IntegerProperty()
    closed = RelationshipTo(starttime, 'START_AT')
    opened = RelationshipTo(stoptime, 'STOPPED_AT')

class arduino(StructuredNode):
    name=StringProperty(requirrd=True)
    ida=IntegerProperty()
    moisture= RelationshipTo(moisture,'READS')
    humidity= RelationshipTo(humidity,'READS')
    co2= RelationshipTo(co2,'READS')
    temperature= RelationshipTo(temperature,'READS')
    lightintensity= RelationshipTo(lightintensity,'READS')
    flowmeter= RelationshipTo(flowmeter,'READS')
    valve= RelationshipTo(valve,'CONTROLS')
    ventilator= RelationshipTo(ventilator,'CONTROLS')
    greenhouse= RelationshipTo(greenhouse,'PLACED_IN')


from django import template

register = template.Library()

@register.filter
def positionStyle(position):
	return str(position).replace(', ', '/')

@register.filter
def getVoicePart(dictionary):
	for item in dictionary:
		return item; 

@register.filter
def capitalize(string):
	return str(string).upper()
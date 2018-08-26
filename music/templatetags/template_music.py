from django import template

register = template.Library()

@register.filter
def listItems(items):
	list_individual = ""
	for i in range(len(items)):
		if(i < len(items) - 1):
			list_individual += str(items[i]) + ", "
	if len(items) != 0:
		list_individual += str(items[len(items)-1])
	return list_individual
products=[
    {"item_name":"boost","mrp":290,"stock":50},
    {"item_name":"complan","mrp":280,"stock":0},
    {"item_name":"horlicks","mrp":270,"stock":40},
    {"item_name":"nutrella","mrp":260,"stock":30},
    {"item_name":"chocos","mrp":250,"stock":80}

]
#list all product name

name=[]
for product in products:
    name.append(product["item_name"])
print(name)


# name=list(map(lambda product:product["item_name"],products))
# print(name)
#


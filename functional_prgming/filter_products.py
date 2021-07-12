#print out of stock products


products=[
    {"item_name":"boost","mrp":290,"stock":50},
    {"item_name":"complan","mrp":280,"stock":0},
    {"item_name":"horlicks","mrp":270,"stock":40},
    {"item_name":"nutrella","mrp":260,"stock":30},
    {"item_name":"chocos","mrp":250,"stock":80}

]


for product in products:
    if product["stock"]==0:
        print(product)
#
# outofstock=list(filter(lambda product:product["stock"]==0,products))
# print(outofstock)
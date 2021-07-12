#print all product details available below 250


products=[
    {"item_name":"boost","mrp":290,"stock":50},
    {"item_name":"complan","mrp":280,"stock":0},
    {"item_name":"horlicks","mrp":240,"stock":40},
    {"item_name":"nutrella","mrp":230,"stock":30},
    {"item_name":"chocos","mrp":250,"stock":80}

]


# for product in products:
#     if product["mrp"]<250:
#         print(product)
#
lessthan=list(filter(lambda product:product["mrp"]<250,products))
print(lessthan)
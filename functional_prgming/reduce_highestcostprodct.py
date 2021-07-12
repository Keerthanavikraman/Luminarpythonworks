products=[
    {"item_name":"boost","mrp":290,"stock":50},
    {"item_name":"complan","mrp":280,"stock":0},
    {"item_name":"horlicks","mrp":270,"stock":40},
    {"item_name":"nutrella","mrp":260,"stock":30},
    {"item_name":"chocos","mrp":250,"stock":80}

]

from functools import reduce
prices=list(map(lambda product:product["mrp"],products))
high_cost=reduce(lambda price1,price2:price1 if price1>price2 else price2,prices)
print(high_cost)



# prices=max(list(map(lambda product:product["mrp"],products)))
# print(prices)

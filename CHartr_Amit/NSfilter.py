from os import name
import pandas as pd 
import numpy as np 



def routes_txt(route,ns_route):
    if route in routes_df.values:
        print("this NS route has alternative route in GTFS",route)
        # routeid=routes_df[(routes_df['route_long_name'] == route) & (routes_df['agency_id']=='DTC')]['route_id'].item()
        # print('route id is ==',routeid)
    else :
        if '(NS)' in ns_route:
            print('NS route is ',ns_route)
            NS_refined.append(ns_route)
            # write_in_file(ns_route)
        else:
            print('->',route)
            NS_refined.append(route)
            # write_in_file(route)


def write_in_file(route):
    with open('refined.txt','w') as refined:
        for route in NS_refined:
            refined.write(route)
            refined.write("\n")


def ns_filter():
    with open('flag.txt') as f:
        for routes in f:
            ns_route=''
            if '(NS)'in routes:
                ns_route=routes
                # print('this is ns file name ',ns_route,end='')
                routes.strip('(NS)')    
            routes=routes.strip('\n')
            ns_route=ns_route.strip('\n')
            routes_txt(routes,ns_route)



global routes_df
routes_df = pd.read_csv('routes.txt',delimiter=",",dtype={'route_short_name':'float64','route_long_name':'object','route':'int','agency_id':'object'})
global NS_refined
NS_refined=[]

ns_filter()
# print(NS_refined) to print 
write_in_file(NS_refined)
import pandas as pd
import numpy as np

#variable to get total stops count for old DTC data
total_oldstops = 0

#traversing routes.txt file to get route_id corresponding to the route name
def routes_txt(route_lname):
    global total_oldstops
    df1 = pd.read_csv('routes.txt',delimiter = ",",dtype={'route_short_name':'float64','route_long_name':'object','route_type':'int','route_id':'int','agency_id':'object'})
    if route_lname in df1.values:
        routeid = df1[(df1['route_long_name'] == route_lname) & (df1['agency_id']=='DTC')]['route_id'].item()
        trip_txt(routeid)
        return total_oldstops
    else:
        return 0

#traversing trip.txt file to find trip id corresponding to the route_id
def trip_txt(routeid):
    df2 = pd.read_csv('trips.txt', delimiter = ",",dtype = {'route_id': 'int64', 'service_id': 'int64', 'trip_id': 'O', 'shape_id': 'float64'})
    tripid = df2.loc[(df2['route_id']==routeid),'trip_id'].unique()[0]
    print(tripid)
    stop_times_txt(tripid)

#traversing stop_times.txt file to find count all stop counts correspoding to the trip_id
def stop_times_txt(tripid):
    global total_oldstops
    store_stop_name = set()
    df3 = pd.read_csv('stop_times.txt',delimiter = ",",dtype = {'trip_id': 'O', 'arrival_time': 'O', 'departure_time': 'O', 'stop_id': 'O', 'stop_sequence': 'int'})
    stopid = df3.loc[df3['trip_id']==tripid,'stop_id'].unique()
    total_oldstops = 0
    print(stopid)
    for x in stopid:
        stop_txt(stopid)
        total_oldstops +=1     
    print(total_oldstops)      
  
def stop_txt(stopid):
    df4 = pd.read_csv('stops.txt', delimiter=",")
    count =0
    for i in stopid:
        if count<1:
            stopname = df4.loc[df4['stop_id']== i,'stop_name'].unique()[0]
            count+=1
            print(stopname)

  
route_lname = input('enter route name ')
routes_txt(route_lname)

'''
#functions to find stop count corresponding to all route files (.csv) in new data and compare it to stop count of old DTC data
def GetNewName():
    #creating dataframe to read all new DTC route names stores in a txt file DTC_NewData
    df = pd.read_csv('DTC_NewData.txt', delimiter = ",")
    
    #dataframe to store the routes and counts of new & old data in a new file
    dfdata = pd.DataFrame(columns = ['DTC_routes','old_stops','new_stops','difference'])
    
    #traversing the txt file DTC_NewData and finding their correspoding stop count from new and old data
    #new data traversed by reading .csv file of all routes
    for ind in df.index:
        filenames = df['DTC_routes'][ind]
        fileName , separator , extension = filenames.partition('.')
        routename = fileName + "_DTC"
        
        #routes_txt function returns count of all stops corresponding to the given route for old DTC data
        total_stops = routes_txt(routename)
        
        #printing on console route name,old stops count,new stops count
        print(f"Old DTC Data -> Total stops : {total_stops} for {fileName}")
        df1 = pd.read_csv(f'/home/anjali/Desktop/NewDTCdata/{filenames}',delimiter = ",")
        
        #finding count of all stops for new DTC data by reading .csv file
        print(f'New DTC Data -> Total stops corresponding to {fileName} is : {len(df1.index)}')
        
        newstops = len(df1.index)
        
        #appending data for all routes in dataframe 
        data = [{'DTC_routes' : fileName , 'old_stops' : total_stops , 'new_stops' : newstops, 'difference': (int)(total_stops - newstops)}]
        dfdata = dfdata.append(data,ignore_index=True,sort=False)
        
        #storing the data of routes,count of old and new and their difference in a new txt file DTC_DataDiff.txt
        dfdata.to_csv('/home/anjali/Desktop/DTC_CHANGES/DTC_DataDiff.txt',index=False)       
    
'''
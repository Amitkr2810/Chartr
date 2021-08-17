import pandas as pd 
from csv import reader
def routes_txt(route_short_name):
    with open('routes.txt', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        for row in csv_reader:
            if header != None:
                if len(row)==1:
                    break
                if route_short_name == row[1] :
                    trip_txt(row[3])

def trip_txt(route_id):
    with open('trips.txt', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        count  = 0
        for row in csv_reader:
            if count<1:
                if header != None:
                    if len(row)==1:
                        break
                    if route_id == row[0]:
                        count +=1

                        stop_times(row[2])
    
def stop_times(trip_id):
    total_stops = 0
    with open('stop_times.txt', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        for row in csv_reader:
            if header != None:
                if len(row)==1:
                    break
                if trip_id == row[0]:
                    total_stops += 1
        print("\n\nTOTAL_STOPS : ",total_stops)
                    
def stop_txt(stop_id):
    with open('stops.txt', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        for row in csv_reader:
            if header != None:
                if len(row)==1:
                    break
                if stop_id == row[0]:
                    break
                    
                    
    
        
        
    
        
    
                
#route_short_name = input("Enter route short name\n")
with open('DTC_NewData.txt', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        while header :
            routes_txt(header[0])
            header = next(csv_reader)
#             print(header[0])
                         
#stop_txt(row[3])
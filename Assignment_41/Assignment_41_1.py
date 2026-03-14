

import math


def EuclideanDistance(Point1,Point2):
    distance = math.sqrt(((Point1['X']-Point2['X']) ** 2 ) + ((Point1['Y']-Point2['Y']) ** 2))
    return distance

def main():
    data = [{'Point' : 'a', 'X' : 1,'Y':2,'Label':'Red'},
            {'Point' : 'b', 'X' : 2,'Y':3,'Label':'Red'},
            {'Point' : 'c', 'X' : 3,'Y':1,'Label':'Blue'},
            {'Point' : 'd', 'X' : 4,'Y':6,'Label':'Blue'}
            ]
    
    print('Enter X coordinate of new point')
    X = float(input())


    print('Enter Y coordinate of new point')
    Y = float(input())
    

    new_Point = {'X' : X,'Y' : Y}

    for d in data:
        d['distance'] = EuclideanDistance(new_Point,d)

    sorted_data = sorted(data,key=lambda item : item['distance'])

    k = 3

    dict = {}

    nearest = sorted_data[:k]

    for d in nearest:
        if dict.get(d['Label']) is not None:        
            dict[d['Label']] = dict[d['Label']] + 1            
        else:
            dict[d['Label']] = 1

    print(dict)

    maxdata = max(dict,key=dict.get)

    print(maxdata)

if __name__ == "__main__":
    main()
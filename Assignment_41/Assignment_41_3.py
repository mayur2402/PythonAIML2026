

import math


def EuclideanDistance(Point1,Point2):
    distance = math.sqrt(((Point1['X']-Point2['X']) ** 2 ) + ((Point1['Y']-Point2['Y']) ** 2))
    return distance

def main():
    data = [{'X' : 2,'Y':60,'Label':'Fail'},
            {'X' : 5,'Y':80,'Label':'Passed'},
            {'X' : 6,'Y':85,'Label':'Passed'},
            {'X' : 1,'Y':50,'Label':'Fail'}
            ]
    
    print('Enter study hours')
    X = float(input())


    print('Enter attendance percentage')
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

    maxdata = max(dict,key=dict.get)

    print(maxdata)

    print(nearest)


if __name__ == "__main__":
    main()
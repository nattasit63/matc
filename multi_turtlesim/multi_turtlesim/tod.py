# path = [[[59.0, 210.0], [79.0, 190.0], [99.0, 170.0], [119.0, 150.0], [139.0, 130.0], [159.0, 110.0], [179.0, 90.0], [199.0, 90.0], [219.0, 90.0], [239.0, 90.0], [259.0, 90.0]], [[439.0, 710.0], [439.0, 690.0], [439.0, 670.0], [439.0, 650.0], [439.0, 630.0], [439.0, 610.0], [439.0, 590.0], [439.0, 590.0], [439.0, 590.0], [439.0, 590.0], [439.0, 590.0]]]

# aa = [[10.00,20.00],[30.00,40.00],[50.00,60.00]]
# print(aa)
# def to_int(x):
#     ans = []
#     for i in x:
#         ans.append([int(i[0]),int(i[1])])
#     return ans

# print(to_int(aa))
# import numpy as np
# def traffic_to_sim(q):
#     a =[]
#     for i in range(len(q)):
#         a.append([])
#     for i in range(len(q)):
#         for j in q[i]:
#             a[i].append([j[0]*16.00/800.00,abs(16.00-(j[1]*16.00/800.00))])
#     # print(len(a))
#     return a
# print(traffic_to_sim(path))


# # new = [[2.6979854106903076, 11.797858238220215], [8.740004539489746, 3.299777030944824]]
# new = [[1.18, 11.8], [1.58, 12.2]]

# def invert_to_map(data):
#     result=[]
#     for i in range(len(data)):
#         result.append([]) 
#     for i in range(len(data)):
#         result[i]= [data[i][0]*800.00/16.00,800.00-(data[i][1]*800.00/16.00)]
#     return result

# print(invert_to_map(new))


# result = ['1','x1','y1','2','x2','y2','3','x3','y3','id']

import time
def get_pos_result(num_agent,result):
    list_pos = []
    res = result
    for i in range(num_agent):
        list_pos.append([])

    for i in range(len(list_pos)):
        list_pos[i]=[res[i*num_agent+1],res[i*num_agent+2]]
    return list_pos

# print(get_pos_result(3,result))

#!/usr/bin/python3

from multiprocessing import Process, Manager
import multiprocessing as mp
def insert_list(shared,original):
    for i in range(len(original)):
        shared[i] = original[i]

    # print(shared)
    # return shared


cur_pos = [[1,1],[2,2],[3,3]]
size = 3
manager = Manager()
shared_list = manager.list([[]]*size)

print(shared_list)
x = mp.Process(target=insert_list,args=(shared_list,cur_pos,))
x.start()
# x.join()
time.sleep(1)
print(shared_list)
# while(1):
#     print(",")
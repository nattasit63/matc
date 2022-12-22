'''
This is just an example code for guide to use matc_plan()
'''

from traffic import Traffic_Management
import traffic

'''

User config

'''
traffic.GRID_SIZE = 10
traffic.ROBOT_RADIUS = 15
map_loc = '/home/user/ws/src/map/image.png'
fleet_result = [

                    [[131, 193], [164, 94], [324, 84]],
                    [[715, 275], [709, 228], [535, 278], [534, 405]],
                    [[452, 697], [446, 585], [586, 577], [534, 405], [594, 406]]
        
               ]
agent_id = [0,1,2]

'''

Process

'''

tf = Traffic_Management()
obstacle_pixel = tf.get_obstacle_ind(map_loc) #optional
def go_to_point(path):
     return None
def get_current_poition():
     return None
def is_delivered():
     return None
tf.initial(fleet=fleet_result,obstacle=obstacle_pixel)
none,first_path = tf.matc_plan()

path = first_path
go_to_point(path)
while 1:
     if is_delivered():   
          available_agent,path = tf.matc_plan(Trigger= True,
                                             arrive_id= 1 ,  
                                             current_all_pos=get_current_poition())      # This will plan from current position of each agent to recent goal of them
          if path == True :
               print('Complete')
          else:
               go_to_point(path)









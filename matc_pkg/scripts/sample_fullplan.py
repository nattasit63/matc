'''
This is just an example code for guide to use full_plan()
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

'''

Process

'''
tf = Traffic_Management()
obstacle_pixel = tf.get_obstacle_ind(map_loc) #optional


plan_path = tf.full_plan(obstacle=obstacle_pixel,fleet=fleet_result)  #Result



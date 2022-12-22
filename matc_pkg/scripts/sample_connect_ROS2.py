'''
This is just an example code for guide to connect with  ROS2
'''

from traffic import Traffic_Management,Traffic_Service_Server
import traffic
import rclpy
'''

User config

'''
traffic.GRID_SIZE = 10
traffic.ROBOT_RADIUS = 15

      

'''

Process

'''

def main(args=None):
    rclpy.init(args=args)
    traffic = Traffic_Management()
    obstacle = traffic.get_obstacle_ind(map_loc)
    traffic.initial(fleet=fleet_result,obstacle=obstacle)
    traffic.matc_plan()
    
    '''
    calling service will trigger and return the next station of arrive id: 
        ros2 service call /matc_trigger_service turtlee_interfaces/srv/Matcs '{trigger: True,id: 0}'
    '''

    traffic_srv = Traffic_Service_Server(traffic)
    rclpy.spin(traffic_srv)
    traffic_srv.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    map_loc = '/home/user/ws/src/map/image.png'
    fleet_result = [

                    [[131, 193], [164, 94], [324, 84]],
                    [[715, 275], [709, 228], [535, 278], [534, 405]],
                    [[452, 697], [446, 585], [586, 577], [534, 405], [594, 406]]

                    ]
        

    main()






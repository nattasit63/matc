API Reference
========

This API reference for traffic of this project. traffic provides classes definition called "Traffic_Management" and "Traffic_Service_Server"
 
Get static obstacles of image
************
In case you want to simply get the static obstacles from your image in format of List[ tuple (int,int) ] , Note that default value of binary theshold is 127.
    .. code-block:: none
     traffic.Traffic_management().get_obstacle_ind(name = ' ')  

    .. code-block:: python3
     import traffic
     from traffic import Traffic_Management
    
     tf = Traffic_management()
     traffic.THRESHOLD = 20   # In case you need to custom value of binary theshold
    
     example_map_path = '/home/user/ws/src/map/image.png'
     static_obstacle  = tf.get_obstacle_ind(example_map_path)

 
Initializing Parameters
************
To use traffic planning in the library which are  full_plan( ) and  matc_plan( ) , Both of them require 'obstacle' in format of List[ tuple (int,int) ]  and  'fleet' (list of vehicle route) in format of List[ List [int,int] ] . And to do traffic planning , User should customize GRID_SIZE and ROBOT_RADIUS (in format of int) up to user's environment . Note that default value of GRID_SIZE and ROBOT_RADIUS are 12 and 8 respectively.
 
  
    .. code-block:: python3
        import traffic
        from traffic import Traffic_Management
        
        # In case you need to custom value of GRID_SIZE and ROBOT_RADIUS 
        traffic.GRID_SIZE     = 20
        traffic.ROBOT_RADIUS  = 25   

        tf = Traffic_management()
        example_map_path = '/home/user/ws/src/map/image.png'
        static_obstacle  = tf.get_obstacle_ind(example_map_path) 

        list_of_vehicle_route =  [

                                [[131, 193], [164, 94], [324, 84]],                             # List of route of vehicle0
                                [[715, 275], [709, 228], [535, 278], [534, 405]],               # List of route of vehicle1
                                [[452, 697], [446, 585], [586, 577], [534, 405], [594, 406]]    # List of route of vehicle2

                                ] 
   
   
Full planning
************
Full planning function or full_plan() is a callable method from traffic.Traffic_Management() .This function will plan all traffic path at once .
To call full_plan() :

    .. code-block:: none
        traffic.Traffic_Management().full_plan(obstacle: List[tuple[int,int]],fleet:List[List[int,int]])
 
 
Here is example to use full_plan()
 
    .. code-block:: python3
        tf = Traffic_management()
        full_plan_path = tf.full_plan(obstacle = static_obstacle  ,
                                    fleet    = list_of_vehicle_route)
        
                               

MATC planning
************
MATC planning function or matc_plan() is a callable method from  traffic.Traffic_Management() . This function will plan traffic from 'Trigger signal' at current all  agent position to their current goal. So user have to write program to call function when a agent arrived their current goal . But to use matc_plan() have to initialize first at initial function
To call initial() :

    .. code-block:: none
        traffic.Traffic_Management().initail(obstacle: List[tuple[int,int]], fleet: List[List[int,int]])
 
To call matc_plan() :

    .. code-block:: none
        traffic.Traffic_Management().matc_plan(Trigger: Boolean ,arrive_id: Int ,current_all_pos: List[List[int,int]] )
    
Here is example to use full_plan()       
      
    .. code-block:: python3
        agent_id = [0,1,2]
        tf = Traffic_management()

        def go_to_point(path):
            return None
        def get_current_poition():
            return None
        def is_delivered():
            return None
            
        tf.initial(fleet    =  list_of_vehicle_route,
                    obstacle =  static_obstacle)
        None,first_path = tf.matc_plan()

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



Connect ROS2 to Traffic management library
************
This libray can also adapt to connect with ROS2 by create class that inherits the functionality from traffic.Traffic_management(), send the parent class as a parameter when creating the child class . 
In this example , Define that child class is Traffic_Service_Server which will spin 'traffic_service_server' node to be a server of ROS2 service . And ROS2 service in this case is a customer service which will recieve 'trigger' and 'id' from user , This custom service will call traffic.Traffic_management().matc_plan() 
 
To call Traffic_Service_Server class :

    .. code-block:: none
        traffic.Traffic_Service_Server(Traffic:Traffic_Management)

 
Here is example of code to create child class and connect with ROS2

    .. code-block:: python3
        import rclpy
        from rclpy.node import Node
        from turtlee_interfaces.srv import Matcs
        from std_srvs.srv import Empty
        from traffic import Traffic_Management
        
        class Traffic_Service_Server(Node):
            def __init__(self,Traffic):
                super().__init__('traffic_service_server')
                self.traffic = Traffic
                self.position_trigger = self.create_service(Matcs,'/matc_trigger_service',self.set_trigger_callback) 
            def set_trigger_callback(self,request,response):
                self.traffic.get_server_service( request.trigger,request.id)
                return response
                
            def main(args=None):
                rclpy.init(args=args)
                traffic = Traffic_Management()
                traffic.initial(fleet    = list_of_vehicle_route,
                                obstacle = static_obstacle)


                traffic_srv = Traffic_Service_Server(traffic)
                rclpy.spin(traffic_srv)
                traffic_srv.destroy_node()
                rclpy.shutdown()

            if __name__=='__main__':
                main()    
    
  
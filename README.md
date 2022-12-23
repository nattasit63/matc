# *Interface for Fleet and Traffic management for multiple-depot*


* This project is to connect between User, Fleet and Traffic Management of Autonomous Mobile Robot. 
* In part of Fleet management, This project have adapted it from Kimbim's MDVRP (source : https://github.com/kimbim/MDVRP)
* In part of Visualization, This project use [Multi-Turtlesim](https://github.com/tchoopojcharoen/multi_turtlesim)
* Interface for Fleet and Traffic management for multiple-depot will be fully usable on ROS2 (If not used on ROS2, it cannot work in the section of visualization with Traffic Service Server Node)

------
**USER GUIDE** :
========
  - [Installation](#installation--)
  - [How to Use](#how-to-use)
  - [Guiding to Traffic Management Library](#guiding-to-traffic-management-library)
  - [Limitation of System](#limitation-of-system)
----
**Installation  :**
========
* **Download**
  - Simply download this [respository](https://github.com/nattasit63/Interface-for-Fleet-and-Traffic-management-for-multiple-depot) to your workspace.
 
* **Requirements**
  The requirements for running this project are:
  - [networkX](https://networkx.github.io/documentation/stable/)
  - [numpy](https://pypi.org/project/numpy/)
  - [pygame](https://pypi.org/project/pygame/)
  - [cbs-mapf](https://pypi.org/project/cbs-mapf/)
  - tkinter
  
------

**How to Use**
========

  1.  Jump to where your file located :
   ```sh
    cd  your_workspace/Interface-for-Fleet-and-Traffic-management-for-multiple-depot/main
   ```
   
  2.  Run main.py
   ```sh
   python3 main.py
   ```
   
  3.  If correct it should be displayed like the image below (This is called 'main window'). Then press the 'Create File' button to go to the next step. 

   <p align="center"><img src="matc_pkg/tutorial_pic/home.jpg?raw=true" alt="drawing" height=350 width="500"/></p>
   
   
  4.  **Step1** is step that's user must import image of map file such as png, jpg, bmp, etc. by click on 'Import map' button (The image will be converted from its          original size to 800x800 pixels)
      <p align="center"><img src="matc_pkg/tutorial_pic/step1.jpg?raw=true" alt="drawing" height=350 width="500"/></p>
          When the button is pressed, it displays the following window. Users can select file from where it located then click 'Open' or double click on file.
          
      <p align="center"><img src="matc_pkg/tutorial_pic/step1-select-map.jpg?raw=true" alt="drawing" height=180 width="380"/></p>
      Here is a selected sample map image that will be displayed in a new window with size 800x800 pixel.
      <p align="center"><img src="matc_pkg/tutorial_pic/pop plain map.jpg?raw=true" alt="drawing" height=400 width="400"/></p>
  
  
   5. **Step2** is step that's user must draw nodes on an imported map. There are 3 types of node :
        - Depot point :  The location of the starting point or charging station for the robot.    (Red color)  
        - Customer point  :   The location of the picked up or delivered point which have demand.   (Green Color) 
        - Connetor point  :  It is used as an access point to evade obstacles and determine various positions.  (Turquoise color)
        
      To place the nodes can be done after selecting the type of node and left-click on the window of the imported image (This is called 'drawing window'),this can be un-pasted last time by right-click. User can also determine the radial size of the nodes. (This depends on the user's needs and it has no effect on the calculations)
      
      <p align="center"><img src="matc_pkg/tutorial_pic/step2-select node type.jpg?raw=true" alt="drawing" height=350 width="500"/></p>
      
      The requirements for placing nodes are as follows :
        - All Depot nodes must be placed before other types of nodes.
        - The placed nodes must not overlap the obstacles on map.
      
      Here is an example of placing nodes on drawing window.
      
         <p align="center"><img src="matc_pkg/tutorial_pic/step2-draw depot first.jpg?raw=true" alt="drawing" height=400 width="400"/>(Place all Depot nodes first)</p>
       
         <p align="center"><img src="matc_pkg/tutorial_pic/draw all node.jpg?raw=true" alt="drawing" height=400 width="400"/>(Place other nodes       )</p>
      
      
   6. After the nodes are placed on the map, User must press the Enter key to proceed to the next section of this part is "Edge Connection" (the connection path        between the nodes). Edge connections can be made by left-click on nodes between two nodes to create paths between them and can be undo by right-click on drawing window.
   
       The requirements for connection edges are as follows :
        - Each Depot node can have only one edge.
        - The edges connected between nodes must not overlap or pass through obstructions.
          
      Here is an example of Edge Connection on drawing window. (The red frame is shown that each Depot node can have only one edge)
      
        <p align="center"><img src="matc_pkg/tutorial_pic/show one line.jpg?raw=true" alt="drawing" height=400 width="400"/></p>
    
      After all the edges are created, User must click on 'OK' button in the main window to proceed to next step.
      
      
  7. **Step3** , In the main window will show data that created from **Step2** which are amount of total depot and total customer. In this step, user have to input the data about the user's desired environment by click on 'Input Data' button to open input-window. There are 4 part of input data :
      - Maximum vehicle for each depot (Amount of maximum vehicle for each depot are equaled)
      - Maximum load of vehicle (All vehicle load are equaled)
      - Route duration (Default is 0)
      - Demand (Demand for each customer point)
      
      When all filling box are filled, user must click on 'Confirm' button in an input-window to show result from fleet calculation and proceed to next step.
      <p align="center"><img src="matc_pkg/tutorial_pic/step3 window.jpg?raw=true" alt="drawing" height=350 width="500"/></p>
      
      The requirements for input data of environment are as follows :
       - Data in filling box must be integer
       - Maximum vehicle for each depot must be only 1 (Because of depot is station charge then it can has one vehicle for one station charge)
       - All filling box must be filled before click on 'Confirm' button in an input-window
      
       Here is an example of input-window and result from fleet calculation.
      <p align="center"><img src="matc_pkg/tutorial_pic/config data input.jpg?raw=true" alt="drawing" height=500 width="350"/></p>
  
       <p align="center"><img src="matc_pkg/tutorial_pic/visualize fleet result.jpg?raw=true" alt="drawing" height=400 width="400"/></p>
  
  8. **Step4**  is a final step. There are 3 buttons in this step :
      - Re-Calculate : Do fleet calculation again
      - Save result  : Save result from fleet calculation in term of List of via points (scale : 800x800) to text file 
      - Visualize    : visualize on [Multi-turtlesim with Traffic control](https://github.com/nattasit63/Interface-for-Fleet-and-Traffic-management-for-multiple-depot/blob/main/main/multi_turtlesim_visualize.py)(This just an example of using traffic management maybe it's not work perfectly in some cases) . Suppose that turtle is vehicle and red point is position of depot and customer point.
     
      <p align="center"><img src=matc_pkg/tutorial_pic/step4 window.jpg?raw=true" alt="drawing" height=350 width="500"/></p>   
      
      Here is an example of Save result
       
       <p align="center"><img src="matc_pkg/tutorial_pic/example save fleet result.jpg?raw=true" alt="drawing" height=180 width="380"/></p>
      
      Here is an example of Visualize
     
       <p align="center"><img src="matc_pkg/tutorial_pic/multi-turtlesim window.jpg?raw=true" alt="drawing" height=400 width="400"/></p>
------

**Guiding to Traffic Management Library**
========
                        
   Traffic Management library has been applied and developed from [cbs-mapf](https://pypi.org/project/cbs-mapf/) to be used for result of fleet management which is List of list of ways point for each vehicle. In other words, It is [ [route vehicle 1],[route vehicle 2], . . . , [route vehicle n] ] (Define its name as list of vehicle route). There are 2 major funtions that have developed
   1. Full planning function  is a function that use for plan all at once
      | Input variable | format |
      |:----------:|:----------:|
      |obstacle| List[tuple[int,int]] |
      |fleet| List[List[int,int]] |
      
      
      |Return| A numpy.ndaarray with shape (N, L, 2) with N being the number of agents and L being the length of the path|
      |:----------:|:----------|
      
       [Here](https://github.com/nattasit63/Interface-for-Fleet-and-Traffic-management-for-multiple-depot/blob/main/main/sample_fullplan.py) is an example to use full_plan() 
   2.  Multi-Agent Traffic Control (matc) is a function replanning traffic when one of agents have picked up or delivered and then replanning from its current position.(User have to write a program to use with this function) To use , User have to initial data first by call sub-function initial() 
   
        | Input variable in initial()| format |
        |:----------:|:----------:|
        |obstacle| List[tuple[int,int]] |
        |fleet| List[List[int,int]] |
       
        If initial() is called , User have to call matc_plan() with no agrument to get fisrt planning path .After this, the user have to write program to keep checking that's which agent has arrived its goal. When every agents have already picked up or delivered at all targets this function will return True,True
        
        | Input variable in  matc_plan()| format | description |
        |:----------|:----------|:----------|
        |Trigger| Boolean | True,False|
        |arrive_id| Integer | Id of agent which has picked up or delivered (must related to index from fleet's input in initial())
        |current_all_pos| List[List[int,int]] | Current position of every agent in a time that matc_plan() has been called (lenght and index must related to fleet's input in initial() )
        
        Here is a table of output from matc_plan() with its condition (define that 'PATH' is a numpy.ndaarray with shape (N, L, 2) with N being the number of agents and L being the length of the path)
        
        | condition | return | example of call matc_plan() |
        |:----------|:----------|:----------|
        | To get first planning path| [ ],PATH | first_path = matc_plan() |
        | Common planning| available_agent = List[agent_id] , PATH | agent,path = matc_plan(True,1,[ [150.35],[225,140],[389,128] ])
        | Complete for all target | True,True | None|
        
         [Here](https://github.com/nattasit63/Interface-for-Fleet-and-Traffic-management-for-multiple-depot/blob/main/main/sample_matc.py) is an example to use matc_plan()
         
         
         This function can also connect to ROS2 . [Here](https://github.com/nattasit63/Interface-for-Fleet-and-Traffic-management-for-multiple-depot/blob/main/main/sample_connect_ROS2.py) is an example code to connect Traffic Management library with ROS2 by spin ROS2 node . In an example , class of Traffic Service Server is an inherit of Traffic management and Traffic Service Server will spin 'traffic_service_server' node and create ROS2 custom service which connected to matc_plan() in Traffic Management

   
   
------

**Limitation of System**
========
   - In step2 about placing nodes and edge connection
      -  all depot must placed first
      -  each Depot node can have only one edge
      -  placed nodes must not overlap the obstacles on map
      -  The edges connected between nodes must not overlap or pass through obstructions
   - In step3 about input data of enviroment
      -  data in the box must be integer
      -  maximum vehicle for each depot can be only 1
   - In step4 about saving result and visualization
      - saving result is text of result from fleet management which is list of list of postion for each vehicle and its scale is 0 to 800 both x and y axis (user have to convert back to user's map scale)
      - visualization is just an example of code to interface with traffic management. In some cases, it's not work perfectly cause of [visualize code](https://github.com/nattasit63/Interface-for-Fleet-and-Traffic-management-for-multiple-depot/blob/main/main/multi_turtlesim_visualize.py) is not able to do some cases.
   -  [Traffic management](https://github.com/nattasit63/Interface-for-Fleet-and-Traffic-management-for-multiple-depot/blob/main/main/traffic.py) has been developed as a library. Therefore, user can apply from the results of fleet management to do traffic control

 
    
------
 
 **API Reference**
 ========
 This API reference for traffic of this project. traffic provides classes definition called "Traffic_Management" and "Traffic_Service_Server"
 
 Get static obstacles of image
--------
In case you want to simply get the static obstacles from your image in format of List[ tuple (int,int) ] , traffic.Traffic_management().get_obstacle_ind(name = ' ') is able to use. Note that default value of binary theshold is 127.

   ```python3
    import traffic
    from traffic import Traffic_Management
    
    tf = Traffic_management()
    traffic.THRESHOLD = 20   # In case you need to custom value of binary theshold
    
    example_map_path = '/home/user/ws/src/map/image.png'
    static_obstacle  = tf.get_obstacle_ind(example_map_path) 
   ```

 
 Initializing Parameters
 --------
 To use traffic planning in the library which are  full_plan( ) and  matc_plan( ) , Both of them require 'obstacle' in format of List[ tuple (int,int) ]  and  'fleet' (list of vehicle route) in format of List[ List [int,int] ] . And to do traffic planning , User should customize GRID_SIZE and ROBOT_RADIUS (in format of int) up to user's environment . Note that default value of GRID_SIZE and ROBOT_RADIUS are 12 and 8 respectively.
 
  
  ```python3
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
   ```
   
 Full planning
 --------
 Full planning function or full_plan() is a callable method from traffic.Traffic_Management() .This function will plan all traffic path at once .
 To call full_plan() :
 ```
 traffic.Traffic_Management().full_plan(obstacle: List[tuple[int,int]],fleet:List[List[int,int]])
 ``` 
 
 Here is example to use full_plan()
 
  ```python3
    tf = Traffic_management()
    full_plan_path = tf.full_plan(obstacle = static_obstacle  ,
                                  fleet    = list_of_vehicle_route)
    
   ```                              

 MATC planning
 --------
 MATC planning function or matc_plan() is a callable method from  traffic.Traffic_Management() . This function will plan traffic from 'Trigger signal' at current all  agent position to their current goal. So user have to write program to call function when a agent arrived their current goal . But to use matc_plan() have to initialize first at initial function
 To call initial() :
 ```
 traffic.Traffic_Management().initail(obstacle: List[tuple[int,int]], fleet: List[List[int,int]])
 ```  
 To call matc_plan() :
 ```
 traffic.Traffic_Management().matc_plan(Trigger: Boolean ,arrive_id: Int ,current_all_pos: List[List[int,int]] )
 ```       
 Here is example to use full_plan()       
      
  ```python3
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

 ```  

 Connect ROS2 to Traffic management library
 --------
 
 This libray can also adapt to connect with ROS2 by create class that inherits the functionality from traffic.Traffic_management(), send the parent class as a parameter when creating the child class . 
 In this example , Define that child class is Traffic_Service_Server which will spin 'traffic_service_server' node to be a server of ROS2 service . And ROS2 service in this case is a customer service which will recieve 'trigger' and 'id' from user , This custom service will call traffic.Traffic_management().matc_plan() 
 
 To call Traffic_Service_Server class :
 ```
 traffic.Traffic_Service_Server(Traffic:Traffic_Management)
 ```   
 
 Here is example of code to create child class and connect with ROS2
   ```python3
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
    
    
   ```   
 
    
   

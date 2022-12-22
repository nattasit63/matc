Guiding to Traffic Management Library
========
                        
Traffic Management library has been applied and developed from cbs-mapf_ to be used for result of fleet management which is List of list of ways point for each vehicle. 
In other words, It is [ [route vehicle 1],[route vehicle 2], . . . , [route vehicle n] ] (Define its name as list of vehicle route).

There are 2 major funtions that have developed : 


1.Full planning function  is a function that use for plan all at once

   
.. list-table:: full_plan()
   :widths: 25 50
   :header-rows: 1

   * - Input variable
     - Format
   * - obstacle
     - fleet
   * - List[tuple[int,int]]
     - List[List[int,int]]




sample_fullplan_ is an example to use full_plan()

      
   
2.Multi-Agent Traffic Control (matc) is a function replanning traffic when one of agents have picked up or delivered and then replanning from its current position.(User have to write a program to use with this function) To use , User have to initial data first by call sub-function initial() 

.. list-table:: initial()
   :widths: 25 50
   :header-rows: 1

   * - Input variable
     - Format
   * - obstacle
     - fleet
   * - List[tuple[int,int]]
     - List[List[int,int]]
      
If initial() is called , User have to call matc_plan() with no agrument to get fisrt planning path .After this, the user have to write program to keep checking that's which agent has arrived its goal. When every agents have already picked up or delivered at all targets this function will return True,True
      
      | Input variable in  matc_plan()| format | description |
      |:----------|:----------|:----------|
      |Trigger| Boolean | True,False|
      |arrive_id| Integer | Id of agent which has picked up or delivered (must related to index from fleet's input in initial())
      |current_all_pos| List[List[int,int]] | Current position of every agent in a time that matc_plan() has been called (lenght and index must related to fleet's input in initial() )
.. list-table:: matc_plan()
   :widths: 25 25 50
   :header-rows: 1

   * - Input variable
     - Format
     - Description
   * - Trigger
     - Boolean
     - True,False
   * - arrive_id
     - Integer
     - Id of agent which has picked up or delivered (must related to index from fleet's input in initial())
   * - current_all_pos
     - List[List[int,int]]
     - Current position of every agent in a time that matc_plan() has been called (lenght and index must related to fleet's input in initial())
      
Here is a table of output from matc_plan() with its condition (define that 'PATH' is a numpy.ndaarray with shape (N, L, 2) with N being the number of agents and L being the length of the path)

| condition | return | example of call matc_plan() |
|:----------|:----------|:----------|
| To get first planning path| [ ],PATH | first_path = matc_plan() |
| Common planning| available_agent = List[agent_id] , PATH | agent,path = matc_plan(True,1,[ [150.35],[225,140],[389,128] ])
| Complete for all target | True,True | None|


   sample_matc_ is an example to use matc_plan()


   This function can also connect to ROS2 . This_ is an example code to connect Traffic Management library with ROS2 by spin ROS2 node . In an example , class of Traffic Service Server is an inherit of Traffic management and Traffic Service Server will spin 'traffic_service_server' node and create ROS2 custom service which connected to matc_plan() in Traffic Management

      


.. _cbs-mapf:https://pypi.org/project/cbs-mapf/
.. _This:https://github.com/nattasit63/matc/blob/main/matc_pkg/scripts/sample_connect_ROS2.py
.. _sample_matc:https://github.com/nattasit63/matc/blob/main/matc_pkg/scripts/sample_matc.py
.. _sample_fullplan:https://github.com/nattasit63/matc/blob/main/matc_pkg/scripts/sample_fullplan.py
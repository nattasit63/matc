Limitation of System
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
    - visualization is just an example of code to interface with traffic management. In some cases, it's not work perfectly cause of visualize_code_ is not able to do some cases.
-  Traffic-Management_ has been developed as a library. Therefore, user can apply from the results of fleet management to do traffic control

 
.. _visualize_code: https://github.com/nattasit63/matc/blob/main/matc_pkg/scripts/multi_turtlesim_visualize.py

.. _Traffic-Management:https://github.com/nattasit63/matc/blob/main/matc_pkg/matc_pkg/traffic.py
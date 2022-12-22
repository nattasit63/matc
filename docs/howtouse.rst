
How to Use
========

  1.  Jump to where your file located :

   .. code-block:: sh

      cd  your_ws/src/matc/matc_pkg/scripts
   
  2.  Run main.py
   .. code-block:: sh

      python3 main.py
   
   
  3.  If correct it should be displayed like the image below (This is called 'main window'). Then press the 'Create File' button to go to the next step. 


    .. image:: tutorial_pic/home.jpg
      :width: 500
      :height: 350
      :alt: Alternative text
   
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

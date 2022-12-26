*Interface for Fleet and Traffic management for multiple-depot*
========
Due to the flexibility of movement, ability to modify target position and consistency in work. Fleet of autonomous mobile robots has been applied and replaced by traditional conveying systems such as conveyor systems or manual maneuvers. 
Software that can make such a fleet of robots work together and meet the user's needs includes the environment setting, displaying, and planning the movement. 
Traffic management and communication with each robot Integrating these elements is a combination of logistics and robotics. but at present Such software has not been launched in the industry among robot developers.
In addition, such software does not have a clear standard of use. Therefore, this research focuses on the development of interconnection systems between robots, users and automated fleet management of robots that are consistent with the actual use in factory conditions. 
The software supports the modification of robot paths and key locations in the factory. and must be able to plan the goals of each robot The robot's target is then used to plan the route. And the internal traffic management system will issue commands to the robot to avoid deadlock in the traffic. 





Credit
************
* This project is to connect between User, Fleet and Traffic Management of Autonomous Mobile Robot. 
* In part of Fleet management, This project have adapted from Kimbim's MDVRP (source : https://github.com/kimbim/MDVRP)
* In part of Visualization, This project use Multi-Turtlesim_


.. toctree::
   :maxdepth: 1
   :caption: USER GUIDE


   Installation.rst
   howtouse.rst
   guild_traffic_lib.rst
   api-ref.rst
   limitations-of-system.rst
   


.. _Multi-Turtlesim: https://github.com/tchoopojcharoen/multi_turtlesim
# LARM course M1 IMT
These two challenges (code challenge 1 and 2) are aimed at:  
- controlling a robot to go localize itself and go to a pose destination by itself or be moved by an operator,  
- controlling a robot in an unknown area and make it look for Coke Cans while marking down their locations.
  
### Rendu:
Pour le challenge 1:
- lancer la simulation avec roslaunch larm challenge-1.launch 
- lancer dans un second terminal le navigation.launch
- lancer dans un dernier terminal rosrun rviz rviz, nous avons sauvegarder notre configuration, elle est composée de :
        - fixed frame : map
        - 3 map/costmap différentes qui souscrivent aux topics : /map, /move_base/local_costmap/costmap et /move_base/global_costmap/costmap
        - laser : /scan
        - et path planning : /move_base
Pour commencer il faut que le robot se localise lui même, on effectue un 2D pose goal en fonction de sa position dans la simulation, puis on lance un teleop dans un nouveau terminal (en avançant et en tournant le robot va diminuer la densité de son nuage de points et ainsi mieux se localiser). Ensuite on peut bouger via 2D nav goal, se rapprocher des obstacles tout en les évitant.

Pour le challenge 2 :
- lancer la simulation avec roslaunch larm challenge-2.launch
- lancer sur un autre terminal mapping.launch (lance aussi teleop)
- lancer rviz comme précédement avec la configuration suivante : 
        - fixed frame : odom
        - map : /map
        - laser : /scan
        - pose : /bottle
Pour vérifier le bon fonctionnement on peut ouvrir la simulation et rviz sur la meme fenetre que le webshell, on déplace le robot pour qu'il détecte une canette, ainsi on verra la position de celle ci sur l'écran de rviz et la map se créée au fur et à mesure.



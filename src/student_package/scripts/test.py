import rospy
from geometry_msgs.msgs import PoseWithCovarianceStamped
          

bouteille = PoseWithCovarianceStamped() #syntaxe ???

#Defining a call back function for the Subcriber.
def callback():
    bouteille = subRobot
    pub.publish(bouteille)


rospy.init_node('position_subscriber')

#Souscrit au topic amcl_pose pour avoir la position du robot quand on a une bouteille
subRobot = rospy.Subscriber('amcl_pose', PoseWithCovarianceStamped,callback)

#Doit ajouter à ça la distance du robot avec la canette, voir si doit mettre dans la class de l'image
#subCamera = rospy.Subscriber("/camera/depth/image_raw",Image,self.camera_callback2)

#Publie dans bottle la position du robot
pub = rospy.Publisher('bottle', PoseWithCovarianceStamped, queue_size=10)
rate = rospy.Rate(10) # 10hz

rospy.spin()



import rospy
from geometry_msgs.msgs import PoseWithCovarianceStamps
          

bouteille = new PoseWithCovarianceStamps() #syntaxe ???

#Defining a call back function for the Subcriber.
def callback():
    bouteille = sub.pose.pose.position 
    pub.publish(bouteille)

rospy.init_node('position_subscriber')

#Souscrit au topic amcl_pose pour avoir la position du robot quand on a une bouteille
sub = rospy.Subscriber('amcl_pose',PoseWithCovarianceStamps,callback)

#Publie dans bottle la position du robot
pub = rospy.Publisher('bottle', PoseWithCovarianceStamps, queue_size=10)
rate = rospy.Rate(10) # 10hz

rospy.spin()



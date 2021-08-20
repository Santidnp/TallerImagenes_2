import  cv2
import numpy as np

class thetaFilter:
    
    def __init__(self,path):
        
        self.image = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2GRAY)

    def set_theta(self,theta,diftheta):
        pass

    def filtering(self):
        pass




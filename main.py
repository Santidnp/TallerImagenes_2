from thetaFilter import *
import sys


if __name__ == '__main__':

    path = sys.argv[1]
    t =  sys.argv[2]
    dt =  sys.argv[3]
    imagen = thetaFilter(path)
    imagen.set_theta(t,dt)
    u = imagen.filtering()


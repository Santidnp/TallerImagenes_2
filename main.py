from thetaFilter import *
import sys

"""
python path_imagen 135 30
"""

if __name__ == '__main__':

    path = sys.argv[1]
    t =  sys.argv[2]
    dt =  sys.argv[3]
    imagen = thetaFilter(path)
    imagen.set_theta(t,dt)
    u = imagen.filtering()
    grados = ['0', '45', '90', '135']
    
    imagen_promedio = np.empty([u.shape[0],u.shape[1]])

    for i in grados:
        img = imagen = thetaFilter(path)
        img.set_theta(i,dt)
        V = img.filtering()
        imagen_promedio += V

    imagen_promedio = imagen_promedio/4
    imagen_promedio = imagen_promedio -imagen_promedio.min()
    imagen_promedio = imagen_promedio/imagen_promedio.max()
    cv2.imshow("Imagen Promedio",imagen_promedio)
    cv2.waitKey(0)



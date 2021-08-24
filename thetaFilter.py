import cv2
import numpy as np



class thetaFilter:
    
    def __init__(self,path):

        self.path = path
        self.image_gray = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2GRAY)

    def set_theta(self,theta,diftheta):
        self.theta = theta
        self.diftheta = diftheta


    def filtering(self):
        band_pass_mask1 = np.zeros_like(self.image_gray)
        image_gray_fft = np.fft.fft2(self.image_gray)
        image_gray_fft_shift = np.fft.fftshift(image_gray_fft)
        num_rows, num_cols = (self.image_gray.shape[0], self.image_gray.shape[1])
        enum_rows = np.linspace(0, num_rows - 1, num_rows)
        enum_cols = np.linspace(0, num_cols - 1, num_cols)
        col_iter, row_iter = np.meshgrid(enum_cols, enum_rows)
        half_size = num_rows / 2 - 1
        idx_low = 180 * (np.arctan2(col_iter - half_size, row_iter - half_size)) / np.pi > (int(self.theta) - int(self.diftheta))
        idx_high = 180 * (np.arctan2(col_iter - half_size, row_iter - half_size)) / np.pi < (int(self.theta) + int(self.diftheta))
        idx_bp = np.bitwise_and(idx_low, idx_high)
        band_pass_mask1[idx_bp] = 1
        mask = band_pass_mask1  # can also use high or band pass mask
        fft_filtered = image_gray_fft_shift * mask
        image_filtered1 = np.fft.ifft2(np.fft.fftshift(fft_filtered))
        image_filtered1 = np.absolute(image_filtered1)
        image_filtered1 /= np.max(image_filtered1)
        cv2.imshow("Filtered image ", image_filtered1)
        cv2.waitKey(0)


    #if __name__ == '__main__':
   # pass
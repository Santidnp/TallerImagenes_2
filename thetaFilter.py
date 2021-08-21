import  cv2
import numpy as np
import sys

class thetaFilter:
    
    def __init__(self,path):
        
        self.image_gray = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2GRAY)

    def set_theta(self,theta,diftheta):
        self.theta = theta
        self.diftheta = diftheta


    def filtering(self):
        # create a low pass filter mask
        num_rows, num_cols = (image_gray.shape[0], image_gray.shape[1])
        enum_rows = np.linspace(0, num_rows - 1, num_rows)
        enum_cols = np.linspace(0, num_cols - 1, num_cols)
        col_iter, row_iter = np.meshgrid(enum_cols, enum_rows)
        low_pass_mask = np.zeros_like(image_gray)
        high_pass = np.zeros_like(image_gray)
        freq_cut_off = self.theta - self.diftheta  #0.25 it should less than 1
        half_size = num_rows / 2 - 1  # here we assume num_rows = num_columns
        radius_cut_off = int(freq_cut_off * half_size)
        idx_lp = np.sqrt((col_iter - half_size) ** 2 + (row_iter - half_size) ** 2) < 0.4 * half_size
        idx_hp = np.sqrt((col_iter - half_size) ** 2 + (row_iter - half_size) ** 2) > 0.2 * half_size
        idx_bp = np.bitwise_and(idx_lp, idx_hp)
        low_pass_mask[idx_bp] = 1

        # filtering via FFT
        fft_filtered = image_gray_fft_shift * low_pass_mask
        image_filtered = np.fft.ifft2(np.fft.fftshift(fft_filtered))
        image_filtered = np.absolute(image_filtered)
        image_filtered /= np.max(image_filtered)

        cv2.imshow("Image", image_filtered)
        cv2.waitKey(0)


if __name__ == '__main__':
    pass
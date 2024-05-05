import numpy as np
[WIDTH, HEIGHT] = [1600, 800]
[win_x, win_y] = [20, 20]

[frame1_w, frame1_h] = [1000, 440]
[frame1_x, frame1_y] = [10, 10]

[frame2_w, frame2_h] = [1000, 330]
[frame2_x, frame2_y] = [10, 460]

[frame3_w, frame3_h] = [570, 385]
[frame3_x, frame3_y] = [1020, 10]

[frame4_w, frame4_h] = [570, 385]
[frame4_x, frame4_y] = [1020, 405]

[frame_details_w, frame_details_h] = [490, 300]
[frame_details_x, frame_details_y] = [500, 20]

[thickness_w, thickness_h] = [350,100]
[thickness_x, thickness_y] = [10,20]

[button_w, button_h] = [450,100]
[button_x, button_y] = [600,20]

[button1_w, button1_h] = [20, 1]
[button2_w, button2_h] = [5, 1]

[generate_w, generate_h] = [30, 1]
[generate_x, generate_y] = [270,40]

[select_w, select_h] = [30,1]
[select_x, select_y] = [350,390] 

[rect_w, rect_h] = [980, 180]
[rect_x, rect_y] = [10, 170]

[orange, green, white, brown, yellow, purple, red] = ["#F07101", "#44C200", "#FFFFFF", "#9F3D0F", "#FFFB00","#9C00C2", "#FF1717"]

pts_freq = 500
freq = np.linspace(0.1e9,6e9,pts_freq)
#Testing functions

#W
w_move_point = [750, 900]

#A
a_move_point = [600, 1050]

#S
s_move_point = [750, 1200]

#D
d_move_point = [900, 1050]

def map(value, fromLow, fromHigh, toLow, toHigh):
        return (toHigh - toLow) * (value - fromLow) / (fromHigh - fromLow) + toLow

w_x = map((w_move_point[0]-750),0,150,0,35)
w_y = map((1050 - w_move_point[1]),0,150,0,35)

a_x = map((a_move_point[0]-750),0,150,0,35)
a_y = map((1050 - a_move_point[1]),0,150,0,35)

s_x = map((s_move_point[0]-750),0,150,0,35)
s_y = map((1050 - s_move_point[1]),0,150,0,35)

d_x = map((d_move_point[0]-750),0,150,0,35)
d_y = map((1050 - d_move_point[1]),0,150,0,35)

print("w_x: " + str(w_x) + ", w_y: " + str(w_y))
print("a_x: " + str(a_x) + ", a_y: " + str(a_y))
print("s_x: " + str(s_x) + ", s_y: " + str(s_y))
print("d_x: " + str(d_x) + ", d_y: " + str(d_y))
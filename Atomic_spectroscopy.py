import math
in_var          = input("Please type the angle that measered for hydrogen，only degree part，separated by spaces，no arcmin: ")
in_var_arc      = input("Please type the angle that measered for hydrogen，only arcmin part，type zero if you do not have it: ")
# 输入测量的角度，input degree that measured
T_0                          = float(in_var_arc)
lenth_test                   = 0
while        T_0             == 0:
	in_var_arc               = list(in_var)
	i                        = 0
	lenth_test               = len(list(in_var))
	while i                  < lenth_test:
		in_var_arc[i]        = 0
		i                    = i + 1
				
in_slope        = float(input("Please type the slope, d, in grating: "))
in_b            = float(input("Please type the intercept, b, of equation: "))
# 输入测得的回归方程，input the regression equation that measured

in_uncer_2d     = float(input("Please type the uncertainty of d, the slope: "))
in_uncer_b      = float(input("Please type you uncertainty of b,the intercept: "))
# 输入测得的回归方程的误差, input the uncertainty of regression equation
# called var
in_var_list                  = list(map(float, in_var.split()))
in_var_arc_list              = list(map(float, in_var_arc.split()))
in_var_cal_list              = list(in_var_list)

i                            = 0
while  i                     < len(in_var_arc_list):
	in_var_cal_list[i]       = float(in_var_list[i])+float(in_var_arc_list[i])/60
	i                        = i+1  # make a loop to calculate degree
"""define var"""
d2                           = 2*in_slope
pi2rad                       = float(2*math.pi/360)
bb                           = float(pi2rad/2)
"""called var"""
out_var_list                 = list(in_var_list)
out_uncer_list               = list(in_var_cal_list)
out_var_with_b_list          = list(in_var_cal_list)
out_uncer_with_b_list        = list(in_var_cal_list)

A1                           = 0
i                            = 0

while i                      < len(in_var_cal_list):
	A1                       = float(in_var_cal_list[i])
	
	out_var_list[i]          = d2*math.sin(A1*bb)  # 1727.21,
	out_uncer_list[i]        = math.fabs(math.sin(A1*bb))*in_uncer_2d
	# 输出波长 output wavelength
	
	out_var_with_b_list[i]   = (math.sin(A1*bb))*d2+in_b   # *1727.21+18.36279
	# out put uncertainty with b
	out_uncer_with_b_list[i] = math.sqrt((float(out_uncer_list[i]))**2+in_uncer_b**2)
	# 输出波长，带b的， output wavelenth with intercept
	print("The wavelenth is {:5g} ".format(out_var_list[i]), "±{:1g}".format(out_uncer_list[i]))
	print("The wavelenth(with intercept) is {:5g}".format(out_var_with_b_list[i]), "±{:1g}".format(out_uncer_with_b_list[i]))
	i = i+1

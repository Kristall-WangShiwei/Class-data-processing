#bug很多有人帮忙看一看吗。。。
import math


##in_var_Ls_turns         = input("Please type the truns that you measured of laser, except 0 make sure that you had inverted it. separated by spaces:")
##in_var_sigma_Ls         = input("Please type the uncertainty of each measurement,except 0, separated by space")

# Na/Laser turns,laser sigma, k=43081 +-........ 
##in_var_na_turns         = input("Please type the truns that you measured of sodium, make sure that you had inverted it, if not please calculated by hand, separated by spaces: ")
##in_var_k                = input("please input the slope from graph")

##in_var_Ls_turns         = #input("Please type the truns that you measured of laser, except 0 make sure that you had inverted it. separated by spaces:")
##in_var_sigma_Ls         = #input("Please type the uncertainty of each measurement,except 0, separated by space")

# Na/Laser turns,laser sigma, k=43081 +-........ 
##in_var_na_turns         = #input("Please type the truns that you measured of sodium, make sure that you had inverted it, if not please calculated by hand, separated by spaces: ")
in_var_k                = 43081 #input("please input the slope from graph")

in_var_na_turns         = '5.5 5.4 5.5 5.4 5.25'
in_var_Ls_turns         = '0.073 0.1385 0.204 0.282 0.3455 0.431 0.492 0.5695 0.6555 0.7435'
in_var_sigma_Ls         = '0.002 0.0115 0.015 0.016 0.0275 0.04  0.04  0.0485 0.0615 0.0715'

in_var_na_turns_list    = list(map(float,in_var_na_turns.split() ))
in_var_sigma_Ls_list    = list(map(float,in_var_sigma_Ls.split() ))
in_var_Ls_turns_list    = list(map(float,in_var_Ls_turns.split() ))

#in_var_na_turns_list    = [5.5, 5.4, 5.5, 5.4, 5.25] # list(map(float,in_var_na_turns.split() ))
#in_var_sigma_Ls_list    = [0.002, 0.0115, 0.015, 0.016, 0.0275, 0.04,  0.04,  0.0485, 0.0615, 0.0715] #list(map(float,in_var_sigma_Ls.split() ))
#in_var_Ls_turns_list    = [0.073, 0.1385, 0.204, 0.282, 0.3455, 0.431, 0.492, 0.5695, 0.6555, 0.7435]#list(map(float,in_var_Ls_turns.split() ))

##in_var_na_turns_list = list(in_var_na_turns_list)
##in_var_sigma_Ls_list = list(in_var_sigma_Ls_list)
##in_var_Ls_turns_list = list(in_var_Ls_turns_list)



turns_na_size           = float( len(in_var_na_turns_list))
std_na_turns            = float(0.102469508)
sigma_na_turns          = std_na_turns/math.sqrt(turns_na_size)
avg_na_turns = float(sum(in_var_na_turns_list)/len(in_var_na_turns_list))

i = 0 
a = 0
b = 0
var_sigma_list = list(in_var_sigma_Ls_list)
i=0
# 取sigma/turns这个常数表
while i < 10 : # float(len(in_var_sigma_Ls_list)):
    a = float( in_var_sigma_Ls_list[i])
    b = float( in_var_Ls_turns_list[i])
    var_sigma_list[i]   = a/b
    i                   = i+1



# 取sigma平均值，c将所有的误差视为常数
c = sum(in_var_sigma_Ls_list)/len(in_var_sigma_Ls_list)

# 去极端值
#a = str(max(var_sigma_list ))
#b = str(min(var_sigma_list ))
#in_var_Ls_turns_list.remove(a)
#in_var_Ls_turns_list.remove(b)
del var_sigma_list[0]
del var_sigma_list[-1]

std_Ls_turns            = float(0.10247) #float(staticstics.stdev(in_var_Ls_turns_list))
sigma_Ls_turns          = float(0.045825757)
## std_Ls_turns / math.sqrt(float( len( in_var_Ls_turns_list )))
constant                = sum(var_sigma_list)/len(var_sigma_list)

i=0
sigma_f = list(in_var_na_turns_list)
while i < turns_na_size :
    sigma_f[i] = in_var_na_turns_list[i]
    i = i+1
i = 0
sigma_fc =0
booli = True

#下面是算波长差
# dL=L^2/d
Delta_wl = 588.995*588.995/(2*avg_na_turns)

i = 0


while i < len(in_var_na_turns_list ):
    sigma_f[i] = math.sqrt(float(float(c)*float(c)*float(in_var_na_turns_list[i])*float(in_var_na_turns_list[i])+float(sigma_na_turns)*float(sigma_na_turns)*float(in_var_k)*float(in_var_k)))
    print (i,"sigma of constant uncertainty is:",float(sigma_f[i]) )
    i= i+1
print("average uncertainty of d is:", sum(sigma_f)/len(sigma_f))
print("Wavelength difference is ",Delta_wl)
print("uncertainty of wavelenth difference is:",sum(sigma_f)/len(sigma_f)*588.995*588.995/2*avg_na_turns )

sigma_fc = math.sqrt(in_var_k *in_var_k + sigma_na_turns*sigma_na_turns * in_var_k*in_var_k)
print("sigma of variable uncertainty is:",sigma_fc)
print("Wavelength difference is ",Delta_wl)
print("uncertainty of wavelenth difference is:",sigma_fc*588.995*588.995/2*avg_na_turns )
######


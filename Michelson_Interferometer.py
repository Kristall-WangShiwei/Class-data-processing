#bug很多有人帮忙看一看吗。。。
import math



in_var_na_turns         = input("Please type the truns that you measured of sodium, make sure that you had inverted it, if not please calculated by hand, separated by spaces: ")
in_var_sigma_Ls         = input("Please type the uncertainty of each measurement,except 0, separated by space")
in_var_Ls_turns         = input("Please type the truns that you measured of laser, except 0 make sure that you had inverted it. separated by spaces:")
# Na/Laser turns,laser sigma, k=43081 +-........ 
in_var_k                = input("please input the slope from graph")

in_var_na_turns_list    = list(map(float,in_var_na_turns.split() ))
in_var_sigma_Ls_list    = list(map(float,in_var_sigma_Ls.split() ))
in_var_Ls_turns_list    = list(map(float,in_var_Ls_turns.split() ))

turns_na_size           = float( len(in_var_turns_na_list))
std_na_turns            = float(pandas.std(in_var_na_turns_list))
sigma_na_turns          = uncer_na_turns/(turns_na_size ** 0.5)
i = 0 
var_sigma_list = in_var_Ls_turns_list

while i < float(len(in_var_sigma_Ls_list)):
    var_sigma_list[i]   = in_var_sigma_Ls_list[i]/in_var_Ls_turns_list[i]
    i                   = i+1

c = sum(var_sigma_list)/len(var_sigma_list)
in_var_Ls_turns_list.remove(max(var_sigma_list ))
in_var_Ls_turns_list.remove(min(var_sigma_list ))

std_Ls_turns            = float(pandas.std(in_var_Ls_turns_list))
sigma_Ls_turns          = std_Ls_turns/(float( len( in_var_Ls_turns_list )) **0.5 )
constant                = sum(var_sigma_list)/len(var_sigma_list)

i=0
while i < turns_na_size ):
    sigma_f[i] = in_var_na_turns_list[i]
    i = i+1
i = 0



deter                = str(input("Is that you uncertainty is a consant or variable? type v for variable, type c for constant."))
if deter == "c":
    while i < len(in_var_Na_turns )
        sigma_f[i] = (c*c*in_var_Na_turns[i]**2 +sigma_Na_turns**2 * in_var_k**2)**0.5
if deter == "v":
    sigma_f = (in_var_k **2 + sigma_na_turns**2 * in_var_k**2)**0.5


      
import matplotlib.pyplot as plt
x_ass_coord=[1,2,3,4,5]#skaits
y_ass_coord=[12,24,36,32,90]#vērtības
y_ass_coord2=[70,55,69,100,50]

#plt.style.use("Solarize_Light2")
plt.plot(x_ass_coord,y_ass_coord,label="Vērtība 1. precei",linewidth=3,linestyle="dashed",color='green')
plt.plot(x_ass_coord,y_ass_coord2,label="Vērtība 2.precei",linewidth=5,linestyle="dashdot",color='yellow')
plt.title("Cenas")
plt.xlabel("Skaits")
plt.ylabel("Vērtība")
plt.legend(loc="lower right")
plt.show()
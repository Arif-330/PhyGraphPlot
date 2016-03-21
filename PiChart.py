import matplotlib.pyplot as plt

labels = 'Python','C++','C#','Java','Ruby'
sizes = [15,13,45,10,9]
colors = ['gold','yellowgreen','lightcoral','lightskyblue']
explode = (0,0,0,0,0)

plt.pie(sizes,explode=explode,labels=labels,colors=colors,
        autopct='%1.1f%%',shadow=False,startangle=180)
#plt.axis('equal')
plt.show()
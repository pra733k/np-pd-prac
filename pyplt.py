#             -------- DATA VISUALISATION MatPlotLib--------

import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9,10]
y = [10,20,30,40,50,60,70,80,90,100]
z = plt.bar(x,y)
print(plt.show())

# Program to plot 2-D Heat map
# using matplotlib.pyplot.imshow() method
import numpy as np
import matplotlib.pyplot as plt
data = np.random.random((10,10))
print(data)
print(type(data))
plt.imshow( data , cmap = 'winter' , interpolation = 'blackman' )
# supported values for interpolation are :->
# 'antialiased', 'none', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36', 'hanning', 'hamming', 
# 'hermite', 'kaiser', 'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos', 'blackman'
plt.title( "2-D Heat Map" )
plt.show()

# Program to plot 2-D Heat map
# using matplotlib.pyplot.pcolormesh() method
import matplotlib.pyplot as plt
import numpy as np
Z = np.random.rand( 15 , 15 )
plt.pcolormesh( Z , cmap = 'summer' )
plt.title( '2-D Heat Map' )
plt.show()

#             -------- MatPlotLib Crash Course freeCodeCamp.org --------
# plot
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([11,22,33,44,55,66,77,88,99,110])
# resize your graph
plt.figure(figsize=(5,3), dpi=300) # 1500x900 resolution

plt.plot(x,y, label="11x", color="y", linewidth="1", linestyle="dashdot", marker="o", markersize="5", markeredgecolor="cyan")
# plt.plot(x,y,'b^--', label="11x") # Short hand notation, ftm = '[color][marker][line]'
plt.title("CHTX graph", fontdict={'fontname':'Comic Sans MS','fontsize':'20','color':"r"})

# line 2
z = np.arange(1,10,0.5)
plt.plot(z[:6],z[:6]**2, 'r', label="0.5x[1]", linewidth="1", linestyle="", marker="^", markersize="3", markeredgecolor="b")
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.plot(z[5:],z[5:]**2, 'k-.^', label="0.5x[2]", linewidth="1", linestyle="dashdot", marker="o", markersize="1", markeredgecolor="cyan")
plt.xticks(np.array(range(1,11,1)))
plt.yticks(np.array(range(11,121,11)))

plt.legend()
# plt.savefig('mygraph.png', dpi = 300)
plt.show()


# sincos 
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 1000)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, "-b", label="sine")
plt.plot(x, y2, "-r", label="cosine")
plt.legend(loc="upper left")
plt.ylim(-1.5, 2.0)
plt.show()



# bar

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
labels = ['A','B','C']
values = [1,2,4]
bars = plt.bar(labels,values) # x,y

# bars[0].set_hatch('/')
# bars[1].set_hatch('o')
# bars[2].set_hatch('*')
patterns = ['/','o','*']
for bar in bars: bar.set_hatch(patterns.pop(0))
plt.show()



import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

x = 'gas_prices.csv'
gas = pd.read_csv(x,error_bad_lines=False)
plt.figure(figsize=(8,5), dpi=300)
# plt.plot(gas.Year, gas.USA, 'b.-' , label='USA')
# plt.plot(gas.Year, gas.Canada,'r.-', label='CAD')
# plt.plot(gas.Year, gas['South Korea'],'g.-', label='KOR')
# plt.plot(gas.Year, gas.Australia,'y.-', label='AUS')
for country in gas:
	if country != 'Year':
		print(country)
		plt.plot(gas.Year, gas[country], marker='.')
plt.title("Gas Prices over time (in $USD)")
plt.xlabel("Year")
plt.ylabel("Price in USD")
plt.xticks(gas.Year[::2].tolist()+[2011])
plt.figlegend()
plt.legend(loc='upper center', fancybox=True, ncol=5)
plt.show()




# Histogram
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

fifa = pd.read_csv('fifa_data.csv')

bins = [40,50,60,70,80,90,100]
plt.hist(fifa.Overall, bins=bins, color='#8904c2')
plt.xticks(bins)
plt.ylabel("Np. of Players")
plt.xlabel("Skill Level")
plt.title('Distribution of Players in FIFA')
plt.show()



# Pie Chart 1
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

fifa = pd.read_csv('fifa_data.csv')
left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]

labels = ['Left','Right']
colors = ['#abcf','#8904c2']
plt.pie([left,right], labels=labels, colors=colors, autopct='%.2f %%')
plt.title("Foot Preference of Players")
plt.show()





# Pie Chart 2
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
fifa = pd.read_csv('fifa_data.csv')
fifa.Weight = [int(x.strip('lbs')) if type(x)==str else x for x in fifa.Weight]
plt.style.use('seaborn-pastel')
light = fifa.loc[fifa.Weight <125].count()[0]
light_medium = fifa.loc[(fifa.Weight <125) & (fifa.Weight<150)].count()[0]
medium = fifa.loc[(fifa.Weight <=150) & (fifa.Weight<175)].count()[0]
medium_heavy = fifa.loc[(fifa.Weight <=175) & (fifa.Weight<200)].count()[0]
heavy = fifa.loc[fifa.Weight >=200].count()[0]
labels = ['Under 125', '125-150','150-175','175-200','Over 200']
weights=[light,light_medium,medium,medium_heavy,heavy]
explode = (.4,.2,0,0,.5)
plt.title('Weight Distribution of FIFA Players(lbs)')
plt.pie(weights,autopct="%.2f %%", labels=labels, pctdistance=1, explode=explode,radius = 1.2, shadow=True, startangle=24)
plt.show()






# Box & Whisker Plot
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
fifa = pd.read_csv("fifa_data.csv")
plt.figure(figsize=(5,8))
barcelona = fifa.loc[fifa.Club =='FC Barcelona']['Overall']
madrid = fifa.loc[fifa.Club =='Real Madrid']['Overall']
revs = fifa.loc[fifa.Club =='New England Revolution']['Overall']
labels = ['FC Barcelona','Real Madrid','NE Revolution']
boxes = plt.boxplot([barcelona,madrid,revs],patch_artist=True,labels=labels)
for box in boxes['boxes']:
	box.set(color='#a055cf', linewidth=3, facecolor="#abcdef")
plt.title('Team Comparison')
plt.ylabel('Overall Rating')
plt.show()






# Heat Maps
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
vegetables = ["cucumber", "tomato", "lettuce", "asparagus",
              "potato", "wheat", "barley"]
farmers = ["Farmer Joe", "Upland Bros.", "Smith Gardening",
           "Agrifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]
harvest = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                    [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
                    [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
                    [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
                    [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])
fig, ax = plt.subplots()
im = ax.imshow(harvest)
ax.set_xticks(np.arange(len(farmers)))
ax.set_yticks(np.arange(len(vegetables)))
ax.set_xticklabels(farmers)
ax.set_yticklabels(vegetables)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",rotation_mode="anchor")
for i in range(len(vegetables)):
    for j in range(len(farmers)):
        text = ax.text(j, i, harvest[i, j],
                       ha="center", va="center", color="w")
ax.set_title("Harvest of local farmers (in tons/year)")
fig.tight_layout()
plt.show()

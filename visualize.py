import matplotlib.pylot as plt

# Setting axes values.
x = [10, 30, 50, 100, 250, 500, 1000, 2000, 5000]
y = [10.279830587380388, 13.707607288527434, 15.246720297071317, 17.03347227003784, 19.07323968615581, 21.005331100841303, 21.927596934984948, 23.889638399197523, 27.59053004717982]
  
# plotting the points 
plt.plot(x, y, color = 'blue', linewidth = 2, marker = 'o', markerfacecolor = 'black', markersize = 6)

# specifying horizontal bounds
plt.axhline(y = 406.720, color = 'green', linestyle = '-')
plt.axhline(y = 997.543, color = 'red', linestyle = '-')

# setting x and y axis range
plt.ylim(1, 1050)
plt.xlim(10, 5000)
  
# naming the x axis
plt.xlabel('No. of images')
# naming the y axis
plt.ylabel('Lipschitz bound')
  
# giving a title to my graph
plt.title('Increase in avg. of empirical lipschitz bound with no. of images')
  
# function to show the plot
plt.show()

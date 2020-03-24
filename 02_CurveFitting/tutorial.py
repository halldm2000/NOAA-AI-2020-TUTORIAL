#_______________________________________________________________________________
def load_co2_data():

    # load CO2 data file using numpy
    import numpy as np
    data  = np.loadtxt("./data/co2_weekly_mlo.txt")

    # drop invalid points
    valid = data[:,4]>0                               # identify which rows are valid
    data  = data[valid,:]                             # remove rows with missing values
    year  = data[:,3] - 1974;                         # column 3 is year in decimal format
    co2   = data[:,4]                                 # column 4 is co2 in parts per million
    print("Number of CO2 obsertvations =",co2.size)

    return year, co2

#_______________________________________________________________________________
def plot_co2_data(x, y, ypred,loss=-1):
  import matplotlib.pyplot as plt

  # plot targets
  fig = plt.figure(figsize=(20,10))
  plt.plot(x,y,'o',alpha=0.7,markersize=1)
  plt.grid(True)
  plt.title('Mauna Lua CO$_2$ weekly data')
  plt.title(f'Mauna Lua CO$_2$ weekly data.  Loss={loss:.3f}',fontsize=16) if loss > 0 else None
  plt.ylabel('CO$_2$ parts per million ')
  plt.xlabel('Years since 1974')

  # plot prediction
  plt.plot(x, ypred,'.', markersize=1)
  fig.show()

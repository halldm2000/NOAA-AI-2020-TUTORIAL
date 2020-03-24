
def load_extent_data():

    import numpy as np
    from datetime import datetime, timedelta
    sec_per_day = 3600*24

    data   = np.loadtxt("./data/N_seaice_extent_daily_v3.0.csv", skiprows=2, delimiter=',', usecols=(0,1,2,3,4))
    extent = data[:,3]
    time   = np.zeros_like(extent)

    nrows = data.shape[0]
    start = datetime(1978,1,1)

    for i in range(nrows):
      yr, day, hr, mn = data[i,0:4].astype(int)
      date = datetime(yr,day,hr,mn)
      time[i] = (date-start).total_seconds()/sec_per_day

    return time, extent

import numpy as np
import pandas as pd

#Load all longliner data into numpy arrays then pandas dataframes
kristina_longliner = np.load('datasets/kristina_originals/kristina_longliner.npz')
kristina_longliner = kristina_longliner['x']
kristina_longliner = pd.DataFrame(kristina_longliner)
kristina_longliner.columns = kristina_longliner.columns.str.replace('is_fishing','classification')
kristina_longliner.dropna()
arr_ip = [tuple(i) for i in kristina_longliner.as_matrix()]
dtyp = np.dtype(list(zip(kristina_longliner.dtypes.index, kristina_longliner.dtypes)))
arr = np.array(arr_ip, dtype=dtyp)
np.savez("datasets/kristina_adjusted/kristina_longliner", x=arr)

#Load all trawler data into numpy arrays then pandas dataframes
kristina_trawl = np.load('datasets/kristina_originals/kristina_trawl.npz')
kristina_trawl = kristina_trawl['x']
kristina_trawl = pd.DataFrame(kristina_trawl)
kristina_trawl.columns = kristina_trawl.columns.str.replace('is_fishing','classification')
kristina_trawl.dropna()
arr_ip = [tuple(i) for i in kristina_trawl.as_matrix()]
dtyp = np.dtype(list(zip(kristina_trawl.dtypes.index, kristina_trawl.dtypes)))
arr = np.array(arr_ip, dtype=dtyp)
np.savez("datasets/kristina_adjusted/kristina_trawl", x=arr)

#Load all purse seine data into numpy arrays then pandas dataframes
kristina_ps = np.load('datasets/kristina_originals/kristina_ps.npz')
kristina_ps = kristina_ps['x']
kristina_ps = pd.DataFrame(kristina_ps)
kristina_ps.columns = kristina_ps.columns.str.replace('is_fishing','classification')
kristina_ps.dropna()
arr_ip = [tuple(i) for i in kristina_ps.as_matrix()]
dtyp = np.dtype(list(zip(kristina_ps.dtypes.index, kristina_ps.dtypes)))
arr = np.array(arr_ip, dtype=dtyp)
np.savez("datasets/kristina_adjusted/kristina_ps", x=arr)

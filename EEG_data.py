#%%
import mne
import numpy as np

import matplotlib.pyplot as plt

#%%
raw =mne.io.read_raw_brainvision(r'eeg.vhdr')
print(raw.ch_names)
events = mne.events_from_annotations(raw)
#%%
data = raw.get_data()
print(data.shape)
print(events[0].shape)
#%%
x = np.arange(data.shape[1])
y = data[3,:]
plt.plot(x,y)
print(events[0])
#%%
all_eeg_data = []
print(events[0].shape)
for i in range(events[0].shape[0]):
  if(events[0][i,2]==1 or events[0][i,2]==2 or events[0][i,2]==3):
    all_eeg_data.append(data[1:30,events[0][i,0]+150:events[0][i,0]+750])
all_eeg_data =np.array(all_eeg_data)[2:]
print(all_eeg_data.shape)

  # %%
def standardlizeSig(data):
    base = np.mean(data)
    std = np.std(data)
    standardlized_data = (data-base)/std
    del base, std
    return standardlized_data

# %%
y_lables = []
for i in range(all_eeg_data.shape[0]):
    y_lables.append(i % 3)
print(y_lables)
#%%
np.savez(r'D:\workspace\x,y.npz', all_eeg_data[:], y_lables[:])


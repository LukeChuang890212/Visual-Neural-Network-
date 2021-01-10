#%%
import numpy as np

#%%
input_to_v1 = np.identity(7)
input_to_v1

#%%
v1_to_spat1 = np.array([[1,0,0,0,0],
                        [1,1,0,0,0],
                        [1,1,1,0,0],
                        [0,1,1,1,0],
                        [0,0,1,1,1],
                        [0,0,0,1,1],
                        [0,0,0,0,1]])
v1_to_spat1

#%%
spat1_to_spat2 = np.array([[1,0,0],
                        [1,1,0,],
                        [1,1,1],
                        [0,1,1],
                        [0,0,1]])
spat1_to_spat2

#%%
v1_to_obj1 = np.array([[1,0,0,0,0],
                        [1,1,0,0,0],
                        [1,1,1,0,0],
                        [0,1,1,1,0],
                        [0,0,1,1,1],
                        [0,0,0,1,1],
                        [0,0,0,0,1]])
v1_to_obj1

#%%
obj1_to_obj2 = np.array([[1,0,0],
                        [1,1,0],
                        [1,1,1],
                        [0,1,1],
                        [0,0,1]])
obj1_to_obj2

#%%
spat1_to_obj1 = np.array([[1,0,0],
                        [1,1,0],
                        [1,1,1],
                        [0,1,1],
                        [0,0,1]])
spat1_to_obj1

#%%
spat1_lateral_inhibit = np.identity(5)*2-np.ones(5)
spat1_lateral_inhibit

#%%
spat2_lateral_inhibit = np.identity(3)*2-np.ones(3)
spat2_lateral_inhibit
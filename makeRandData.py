import pandas as pd
import numpy as np
np.random.seed(1)


for i in range(25):
    data = pd.DataFrame({"A" : np.random.randint(low=1, high=500, size=50),
                        "B"  : np.random.randint(low=1, high=500, size=50),
                        "C" : np.random.randint(low=1, high=100, size=10),
                        "D"  : np.random.randint(low=1, high=500, size=50),
                        "E" : np.random.randint(low=1, high=100, size=10),
                        "F"  : np.random.randint(low=1, high=500, size=50),
                        "G" : np.random.randint(low=1, high=500, size=50),
                        "H"  : np.random.randint(low=1, high=500, size=50),
                        "A" : np.random.randint(low=1, high=500, size=50),
                        "B"  : np.random.randint(low=1, high=500, size=50),
                        "C" : np.random.randint(low=1, high=500, size=50),
                        "D"  : np.random.randint(low=1, high=500, size=50),
                        "E" : np.random.randint(low=1, high=500, size=50),
                        "F"  : np.random.randint(low=1, high=500, size=50),
                        "G" : np.random.randint(low=1, high=500, size=50),
                        "H"  : np.random.randint(low=1, high=500, size=50)
                        })
    name = '/Users/georgienahass/Desktop/fakeData/' + str(i) + '.xlsx'
    print(name)
    data.to_excel(name)  



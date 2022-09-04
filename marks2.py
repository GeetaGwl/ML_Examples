import numpy as np
import pandas as pd 

import sweetviz

data=pd.read_csv("bh.csv")
rep=sweetviz.analyze([data,"data"],target_feat="price")
rep.show_html('rep2.html')
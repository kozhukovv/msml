from pyscopus import Scopus
import pandas as pd

pd.set_option('display.max_columns', None)
pd.options.display.expand_frame_repr = False
pd.options.display.max_colwidth = False

#KEY = '4b6871c642e0c92c6e34132c53aae2a2' твой ключ

scopus = Scopus(KEY)

search_df = scopus.search("KEY(MR)", count=50, view='Standard')
print(search_df)

#author_result_df = scopus.search_author("AUTHLASTNAME(Khovaylo)", view='STANDARD')

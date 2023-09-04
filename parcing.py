from pybliometrics.scopus import ScopusSearch
import pandas as pd
from tqdm import tqdm

def get_papers(keys:list, pubyear:list, doctype:str = 'ar', subjarea:str = 'MATE'):
    """key – ключевое слово, doctype – вид статьи, subjarea – научная область, pubyear – список годов"""
    
    dataframe = pd.DataFrame() # список, в которые будут записываться все результаты запросов в списках
    
    print('Progress scanning keywords:')
    for key in tqdm(keys):
        #print(f'Keyword: {key}')
        
        for year in pubyear:
            #print(f'Year: {year}')
            query = f'TITLE-ABS-KEY({key}) AND DOCTYPE({doctype}) AND SUBJAREA({subjarea}) AND PUBYEAR = {year}'
            
            data = ScopusSearch(query, subscriber=False, verbose=False)
            data_q = pd.DataFrame(pd.DataFrame(data.results))            
            
            data_q[['keyword', 'doctype', 'subjarea', 'year']] = key, doctype, subjarea, year
            
            dataframe = pd.concat([dataframe, data_q])
    return dataframe
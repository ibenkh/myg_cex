#!/usr/bin/env python3
from pandas import read_csv


class IMPORT_PARAM:

    def __init__(self, path):
        self.path = path
        self.df = self.import_els(self.path)
        self.df = self.propre_df(self.df)
        # mettre les methode a lancer

    def import_els(self, path):
        df = read_csv(path)
        return df

    def propre_df(self, df):
        df = df.pivot(index='but_idr_business_unit', columns='oxf_account',
                      values='f_value_account').reset_index(drop=True)
        df.columns = ['700TTC', '990808', '990812', 'BTXTVA', 'S10100',
                      'S29990', 'S39950', 'T6100E', 'T6400E', 'W200', 'WGLE01']
        return df


"""
if __name__ == '__main__':
    a = IMPORT_PARAM('~/Bureau/mg_cex/param_forecast.csv').df
    print(a)
"""

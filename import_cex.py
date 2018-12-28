#!/usr/bin/env python3
from pandas import read_csv


class IMPORT_CEX:

    def __init__(self, path):
        self.path = path
        self.df = self.import_els(self.path)
        self.df = self.propre_df(self.df)
        # mettre les methode a lancer

    def import_els(self, path):
        try:
            df = read_csv(path)
        except TypeError as e:
            print('la direction du fichier n est pas bonne', e)
        return df

    def propre_df(self, df):
        df = df.drop(['rs_technical_date', 'rs_technical_flow'], axis=1).pivot(
            index='dpt_idr_department', columns='oxr_account', values='f_value_account').reset_index().copy().fillna(0)

        df.columns = ['dpt_num', '13500_AL', '700TTC', 'NETMGE', 'NETMGI_AL',
                      'RTCMGI_AL', 'S10190R', 'S13298_AL', 'S24300', 'T6100E', 'T6520E', 'W200']
        return df


"""
if __name__ == '__main__':
    a = IMPORT_CEX('~/Bureau/mg_cex/cex_mg.csv')
    a.df
"""

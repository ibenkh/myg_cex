#!/usr/bin/env python3
from numpy import nansum


class CALCUL_CEX:

    def __init__(self, df):
        self.df = df
        self.total_ca = nansum(df['700TTC'].values)
        self.total_w200 = nansum(df['W200'].values)
        self.df = self.cle_repartition(self.df, self.total_ca)
        self.df = self.recalcul_W200(self.df, self.total_w200)

    def cle_repartition(self, df, total):
        df['cle'] = df['700TTC'].values/total
        return df

    # degres 1 / W200 / T6200E
    def recalcul_W200(self, df, total):
        df['W200'] = df['cle'].values * total
        print('recalcul W200')
        return df

    # degres 2 / NETGME / T6900E
    # degres 3 / OPRTE

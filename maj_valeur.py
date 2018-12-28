#!/usr/bin/env python3


class MAJ_VALEUR:

    def __init__(self, dpt_num, df_cex=None,  valeur_ca=None, df_param=None, valeur_heure=None, valeur_metre=None):
        self.dpt_num = dpt_num
        self.df_cex = df_cex
        self.df_param = df_param
        self.valeur_ca = valeur_ca
        self.valeur_heure = valeur_heure
        self.valeur_metre = valeur_metre
        if valeur_ca is not None:
            self.df_cex = self.maj_valeur_ca(df_cex, dpt_num, valeur_ca)
        if valeur_heure is not None:
            self.df_param = self.maj_valeur_heure(df_param, valeur_heure)
        if valeur_metre is not None:
            self.df_param = self.maj_valeur_metre(df_param, valeur_metre)

    def maj_valeur_ca(self, df, dpt_num, valeur):
        df.loc[df['dpt_num'] == dpt_num, '700TTC'] = valeur
        print('maj_ca')
        return df

    def maj_valeur_heure(self, df, valeur):
        df['S29915'] = valeur
        print('maj_heure')
        return df

    def maj_valeur_metre(self, df, valeur):
        df['S10100'] = valeur
        print('maj_surface')
        return df


"""
if __name__ == '__main__':
    df = pd.read_csv('~/Bureau/mg_cex/cex_mg.csv')
    df = df[['dpt_idr_department', 'but_idr_business_unit',
             'wee_id_week', 'oxr_account', 'f_value_account']].copy()

    a = df.pivot(index='dpt_idr_department', columns='oxr_account',
                 values='f_value_account').reset_index()

    a.columns = ['dpt_num', '13500_AL', '700TTC', 'NETMGE', 'NETMGI_AL',
                 'RTCMGI_AL', 'S10190R', 'S13298_AL', 'S24300', 'T6100E', 'T6520E', 'W200']

    a = a.fillna(0)
    ca = 10
    dpt_num = 0
    print(a.loc[a['dpt_num'] == dpt_num, '700TTC'])
    B = MAJ_VALEUR(dpt_num, a, ca).df_cex
    print(B.head())
"""

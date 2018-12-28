#!/usr/bin/env python3
from import_cex import IMPORT_CEX
from calcul_cex import CALCUL_CEX
from maj_valeur import MAJ_VALEUR
from import_param import IMPORT_PARAM

dpt_num = 0
new_ca = 4000
new_heure = 12
new_metre = 24


def main():

    # Importation dataframe cex
    df_cex = IMPORT_CEX('~/Bureau/mg_cex/cex_mg.csv').df
    df_param = IMPORT_PARAM('~/Bureau/mg_cex/param_forecast.csv').df

    # Mise à jour des valeurs
    df_cex = MAJ_VALEUR(dpt_num, df_cex=df_cex, valeur_ca=new_ca).df_cex

    print(df_cex.loc[df_cex['dpt_num'] == 0, '700TTC'])

    df_param = MAJ_VALEUR(dpt_num, df_param=df_param, valeur_heure=new_heure,
                          valeur_metre=new_metre).df_param

    print(df_param[['S10100', 'S29915']])

    # Recalcul indicateurs
    df_cex = CALCUL_CEX(df_cex).df
    print(df_cex.columns)


if __name__ == '__main__':
    main()

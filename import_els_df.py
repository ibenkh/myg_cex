#!/usr/bin/env python3
from elasticsearch import Elasticsearch
from pandas import concat
from pandas.io.json import json_normalize
from json import loads, dumps


class IMPORT_ELS_DF:

    def __init__(self, es, index, body, flag_cex=True, size_max=1000, filter=None):
        self.es = es
        self.index = index
        self.body = body
        self.flag_cex = flag_cex
        if flag_cex:
            self.df_cex = self.get_df_cex(self.load_els(es, index, body))
        else:
            self.df_param = self.get_df_param(self.load_els(es, index, body))

    def load_els(es, index, size_max, body, filter=None):
        return loads(dumps(es.search(index=index, size=size_max, body=body, filter_path=filter)))

    def get_df_cex(doc):
        df = concat([json_normalize(dic['_source']) for dic in doc['hits']['hits']], axis=0)
        df.columns = [nomcol.replace('accounts.', '') for nomcol in df.columns]
        return df.drop(['but_typ', 'rs_technical_date'], axis=1).reset_index(drop=True)

    def get_df_param(doc):
        df = concat([json_normalize(dic['_source']) for dic in doc['hits']['hits']], axis=0)
        df.columns = [nomcol.replace('oxf_id_time', 'week_id').replace(
            'but_num_business_unit', 'but_num') for nomcol in df.columns]
        return df[['but_num', 'oxf_account', 'f_value_account']].reset_index(drop=True)


if __name__ == '__main__':
    es = Elasticsearch(
        ['internal-internal-ELS-V56-PP-2029477262.eu-west-1.elb.amazonaws.com'], timeout=100)

    cex_index = 'f_myg_cex_real_to_wee_but_dpt_3_0'
    param_index = 'f_oxy_forecast_1_0'

    cex_body = {
        "query": {"bool": {"must": [{"term": {"but_num": "1289"}}, {"term": {"week": "201713"}}]}}}
    param_body = {"query": {"bool": {
        "must": [{"term": {"but_num_business_unit": "1289"}}, {"term": {"oxf_id_time": "W201713"}}]}}}

    a = IMPORT_ELS_DF(es, cex_index, cex_body).df_cex
    b = IMPORT_ELS_DF(es, param_index, param_body, flag_cex=False).df_param
    print(a.head())
    print(b.head())

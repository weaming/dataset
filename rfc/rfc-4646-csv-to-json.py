#!/usr/bin/env python3

import json
import pandas as pd

# from http://www.lingoes.net/en/translator/langcode.htm
df = pd.read_csv('rfc-5646.csv')
# from https://github.com/datasets/language-codes/blob/master/data/ietf-language-tags.csv
# df = pd.read_csv('ietf-language-tags.csv')
# print(df)

code_lang = {}
for x in json.load(open('../iso/iso-639.json')):
    code_lang[x['639-1']] = x
# print(code_lang)


code_country = {}
for x in json.load(open('../iso/iso-3166-1.zh.json')):
    code_country[x['代码']] = x['国家/地区']
# print(code_country)


# from http://www.lingoes.net/en/translator/langcode.htm
default_langs = {
    'kok': '贡根语',
    'ns': '北部梭托语',
    'syr': '古叙利亚语',
}
seen = set()
print('lang,langChinese,country/region')
for _, row in df.iterrows():
    # print(row.to_dict())
    code = row['lang']
    if code in seen:
        continue
    seen.add(code)
    if len(code.split('-')) == 2:
        lang, country = code.split('-')
        if country == '001':
            continue
        if not pd.isna(country):
            cty = code_country.get(country, country)
            print(
                '{},{},{}'.format(
                    code,
                    code_lang.get(lang, {}).get(
                        'Chinese',
                        default_langs.get(lang, 'UNKNOWN'),
                    ),
                    cty,
                )
            )

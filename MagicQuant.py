# -*- coding: utf-8 -*-
import pandas as pd



def magic_by_pd(path_per, path_roa):
    # 파일경로
    file_path_per = path_per

    # 파일읽기
    # per_data = pd.read_excel(file_path, sheet_name='PER', index_col=0)
    per_data = pd.read_csv(file_path_per, sep='\t', index_col=0)

    # 필터링
    filtered_per = per_data[per_data['PER'] > 0]

    # 정렬
    sorted_per = filtered_per.sort_values(by='PER')

    # 랭킹
    sorted_per['PER랭킹'] = sorted_per['PER'].rank()

    # sorted_per
    
    # 파일경로
    file_path_roa = path_roa

    # 파일읽기
    roa_data = pd.read_csv(file_path_roa, sep='\t', index_col=0)

    # 필터링
    filtered_roa = roa_data.dropna()
    filtered_roa.columns = ['ROA']

    # 정렬
    sorted_roa = filtered_roa.sort_values(by='ROA', ascending=False)

    # 랭킹
    sorted_roa['ROA랭킹'] = sorted_roa['ROA'].rank(ascending=False)

    # sorted_roa
    
    # 병합
    total_df = pd.merge(sorted_per, sorted_roa, how='inner', left_index=True, right_index=True)

    total_df['랭킹 합계'] = total_df['PER랭킹'] + total_df['ROA랭킹']

    sorted_df = total_df.sort_values(by='랭킹 합계')

    sorted_df['종합 랭크'] = sorted_df['랭킹 합계'].rank()

    # sorted_df
    
    return sorted_df

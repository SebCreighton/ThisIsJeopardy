import pandas as pd
import re

pd.set_option('display.max_colwidth', None)

df = pd.read_csv('jeopardy.csv')

print(df.head())


def dataset_filter_qs_with_words(word_list, data_set):
    sizeofList = len(word_list)
    i = 0
    new_list = []
    for word in word_list:
        new_list.append(word.lower())
    data_set["Question"] = data_set["Question"].str.lower()
    data_set_modified = data_set[data_set['Question'].str.contains(new_list[i])]

    while i < sizeofList:
        data_set_modified = data_set_modified[data_set_modified['Question'].str.contains(new_list[i])]
        i += 1

    data_set_modified["Question"] = data_set_modified["Question"].str.capitalize()
    return data_set_modified


print(dataset_filter_qs_with_words(["King"], df))


def compute_agg_stats(word_list, data_set):
    data_set['Value'] = data_set['Value'].replace(to_replace='None', value='$0.00', regex=True)
    data_set['Value'] = data_set['Value'].replace('[\$,]', '', regex=True).astype(float)
    new_data_set = dataset_filter_qs_with_words(word_list, data_set)
    return new_data_set["Value"].mean()


print(compute_agg_stats(['King'], df))


def count_unique_answers(word_list, data_set):
    new_data_set = dataset_filter_qs_with_words(word_list, data_set)
    return new_data_set['Answer'].value_counts()


print(count_unique_answers(['king'], df))


def filter_date(word_list, data_set, decade):
    new_data_set = dataset_filter_qs_with_words(word_list, data_set)
    new_data_set_dates = new_data_set[new_data_set['Air Date'].str.startswith(decade)]
    return new_data_set_dates


print(filter_date(['King'], df, "200"))


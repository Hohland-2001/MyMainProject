import pandas as pd


def read_operations_from_csv(path_to_csv: str):
    """Преобразует файл из формата CSV в список словарей"""
    df = pd.read_csv(path_to_csv, delimiter=';')
    max_count_x = df.shape[0]
    operations_list = []
    for count_x in range(0, max_count_x, 1):
        try:
            operations_dict_1 = {}
            operations_dict_2 = {}
            operations_dict_3 = {}
            operations_dict_1['id'] = int(df.iloc[count_x, 0])
            operations_dict_1['state'] = df.iloc[count_x, 1]
            operations_dict_1['date'] = df.iloc[count_x, 2]
            operations_dict_2['amount'] = str(round(float(df.iloc[count_x, 3])))
            operations_dict_3['name'] = df.iloc[count_x, 4]
            operations_dict_3['code'] = df.iloc[count_x, 5]
            operations_dict_1['operationAmount'] = operations_dict_2
            operations_dict_2['currency'] = operations_dict_3
            operations_dict_1['description'] = df.iloc[count_x, 8]
            operations_dict_1['from'] = df.iloc[count_x, 6]
            operations_dict_1['to'] = df.iloc[count_x, 7]
        except Exception:
            continue
        finally:
            operations_list.append(operations_dict_1)
    return operations_list


def read_operations_from_excel(path_to_excel: str):
    """Преобразует файл из формата XLSX в список словарей"""
    df = pd.read_excel(path_to_excel)
    max_count_x = df.shape[0]
    operations_list = []
    for count_x in range(0, max_count_x, 1):
        try:
            operations_dict_1 = {}
            operations_dict_2 = {}
            operations_dict_3 = {}
            operations_dict_1['id'] = int(df.iloc[count_x, 0])
            operations_dict_1['state'] = df.iloc[count_x, 1]
            operations_dict_1['date'] = df.iloc[count_x, 2]
            operations_dict_2['amount'] = str(round(float(df.iloc[count_x, 3])))
            operations_dict_3['name'] = df.iloc[count_x, 4]
            operations_dict_3['code'] = df.iloc[count_x, 5]
            operations_dict_1['operationAmount'] = operations_dict_2
            operations_dict_2['currency'] = operations_dict_3
            operations_dict_1['description'] = df.iloc[count_x, 8]
            operations_dict_1['from'] = df.iloc[count_x, 6]
            operations_dict_1['to'] = df.iloc[count_x, 7]
        except Exception:
            continue
        finally:
            operations_list.append(operations_dict_1)
    return operations_list

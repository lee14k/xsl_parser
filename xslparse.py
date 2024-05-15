import pandas

excel_data_fragment = pandas.read_excel('inventory_list_7.xlsx', sheet_name='Northland Farms')

json_str = excel_data_fragment.to_json()

print('Excel Sheet to JSON:\n', json_str)
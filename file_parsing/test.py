import file_parsing as fp
#html = fp.spreadsheet_to_html('/home/brad/Documents/Code/Libraries/Diablo-Python/tests/test_spreadsheet_to_html/test_merged_columns.xlsx', css_classes='table table-striped')

html = fp.spreadsheet_to_html('/home/brad/Documents/Code/Libraries/Diablo-Python/tests/test_spreadsheet_to_html/test_narrow_merged_column.xlsx', css_classes='table table-striped')


print(html)

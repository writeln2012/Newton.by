import gspread


gc = gspread.service_account(filename='my-test-project-375409-d344fb391379.json')
hit = gc.open_by_url('https://docs.google.com/spreadsheets/d/119zT2AFXdJvJHPrd5PR1sCpnU8NMNk5S/edit#gid=280272758')

wk = hit.sheet1
print(wk)

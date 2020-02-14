from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws1 = wb.create_sheet("Mysheet")
ws.title = "hello"
wb.save("fishc.xlsx")

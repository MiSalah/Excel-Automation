import openpyxl as xl

workbook = xl.load_workbook("transactions.xlsx")
sheet = workbook["Sheet1"]

for row in range(2, sheet.max_row +1):
    cell = sheet.cell(row,3)
    corrected_price = cell.value*0.9

    new_cell = sheet.cell(row, 4)
    new_cell.value = corrected_price

sheet.cell(1,4).value = "New Price (- 10%)"
workbook.save("output_transaction.xlsx")
    

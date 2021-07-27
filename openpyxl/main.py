import openpyxl
from openpyxl import Workbook
from openpyxl.styles import *
from openpyxl.worksheet.table import Table, TableStyleInfo


def show_table(sheet: openpyxl.worksheet.worksheet.Worksheet):
    for i in sheet.values:
        print(i)


def test():
    workbook = openpyxl.load_workbook("./sample.xlsx")
    page1 = workbook['Instructions']
    page2 = workbook['FoodSales']
    page3 = workbook['MyLinks']
    workbook.create_sheet('TestSheet')
    page4 = workbook['TestSheet']
    workbook.remove(page4)
    workbook.create_sheet('TestSheet')
    del workbook['TestSheet']
    workbook.create_sheet('TestSheet')
    print("sheet state:", page1.sheet_state)
    print("max rows on 2nd sheet:", page2.max_row)
    print("max columns on 2nd sheet:", page2.max_column)
    print("sheet view:", page2.sheet_view, "\n")
    print("Let's show contents:")
    show_table(page1)
    show_table(page2)
    show_table(page3)
    print('Value of C3 cell:', page2['C4'].value)
    print('Value of C3 cell:', page2.cell(row=4, column=3).value)
    cell_to_change = page2['C4']
    cell_to_change.value = 'Naberezhnye Chelny'
    workbook.save('./same_CHANGED.xlsx')
    workbook.close()


def test2():
    workbook = openpyxl.load_workbook('./sample.xlsx')
    sheet = workbook['FoodSales']
    cell = sheet['B8']
    font = Font(color=colors.BLUE,
                bold=True,
                italic=True)
    cell.font = font
    fill = PatternFill(fill_type='solid',
                       bgColor='F7FE2E')
    cell.fill = fill
    workbook.save('./sample_COLOURED.xlsx')
    workbook.close()


def get_records():
    text_file = open("./new_table.txt")
    records = []
    text_file.seek(0)
    for record in text_file.readlines():
        records.append(record.rstrip('\n').split(','))
    text_file.close()
    return records


def fill_workbook(records):
    workbook = Workbook()
    fpath = "./new_table.xlsx"
    workbook.save(fpath)
    sheet = workbook['Sheet']
    sheet.title = 'Flights'

    for row in records:
        sheet.append(row)

    table = Table(displayName='Table', ref='A1:H8')
    style = TableStyleInfo(name='TableStyleMedium9', showRowStripes=True, showColumnStripes=True)
    table.tableStyleInfo = style

    sheet.add_table(table)

    font = Font(color=colors.BLUE, bold=True, italic=True)
    for cell_no in range(2, 8):
        if int(sheet['D%s' % cell_no].value) % 10 > 3:
            sheet['D%s' % cell_no].font = font
    workbook.save(fpath)
    workbook.close()


def create_from_txt():
    records = get_records()
    fill_workbook(records)


if __name__ == '__main__':
    create_from_txt()

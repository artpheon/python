import openpyxl
from openpyxl.styles import *


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


if __name__ == '__main__':
    test()
    test2()

import xlrd
wb = xlrd.open_workbook(filename=r"D:\python\python\day09\任务\12月份衣服销售数据.xlsx",encoding_override=True)
sheet = wb.sheet_by_name("12月份各种服饰销售情况")

nrows = sheet.nrows #获取多少行的数据
ncols = sheet.ncols # 获取多少列的数据



for row in range(nrows):
    for col in range(ncols):
        data = sheet.cell_value(row,col)
        print(data,end="")
    print()

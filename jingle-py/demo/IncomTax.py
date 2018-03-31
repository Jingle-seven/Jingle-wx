# 计算个税，单位：元

import xlwt

nums = (0, 1500, 4500, 9000, 35000, 55000, 80000)
rates=(0,0.03,0.1,0.2,0.25,0.3,0.35,0.45)

def getIncomeTax(shouldBeTaxed):
    if shouldBeTaxed <= 0:
        return 0
    if shouldBeTaxed <= nums[1]:
        return shouldBeTaxed * rates[1]
    if shouldBeTaxed <= nums[2]:
        return getIncomeTax(nums[1]) + rates[2] * (shouldBeTaxed - nums[1])
    if shouldBeTaxed <= nums[3]:
        return getIncomeTax(nums[2]) + rates[3] * (shouldBeTaxed - nums[2])
    if shouldBeTaxed <= nums[4]:
        return getIncomeTax(nums[3]) + rates[4] * (shouldBeTaxed - nums[3])
    if shouldBeTaxed <= nums[5]:
        return getIncomeTax(nums[4]) + rates[5] * (shouldBeTaxed - nums[4])
    if shouldBeTaxed <= nums[6]:
        return getIncomeTax(nums[5]) + rates[6] * (shouldBeTaxed - nums[5])
    if shouldBeTaxed > nums[6]:
        return getIncomeTax(nums[6]) + rates[7] * (shouldBeTaxed - nums[6])
# 递龟
def getTax(shouldBeTax, idx=-1):
    if idx==-1:
        idx=getLevel(shouldBeTax)
    if idx==0:
        return 0
    if idx==7:
        return getTax(nums[idx - 1], idx - 1) + rates[7] * (shouldBeTax - nums[6])
    if idx>0:
        # print("income {} rate {}".format(shouldBeTax,rates[idx]))
        return getTax(nums[idx - 1], idx - 1) + rates[idx] * (shouldBeTax - nums[idx - 1])

def getLevel(shouldBeTaxed):
    if shouldBeTaxed <= nums[0]:return 0
    if shouldBeTaxed <= nums[1]:return 1
    if shouldBeTaxed <= nums[2]:return 2
    if shouldBeTaxed <= nums[3]:return 3
    if shouldBeTaxed <= nums[4]:return 4
    if shouldBeTaxed <= nums[5]:return 5
    if shouldBeTaxed <= nums[6]:return 6
    if shouldBeTaxed > nums[6]:return 7

# 准备表格
workBook = xlwt.Workbook()
sheet = workBook.add_sheet("工作表1")
sheet.write(0,0,"收入")
sheet.write(0,1,"税额")
sheet.write(0,2,"占比")

for (i,j) in zip(range(1,31),range(1,100)):
    # print("getIncomeTax\t{}\t\t{}".format(i,getIncomeTax(i-3500)))
    tax = getTax(i*1000-3500)
    print("getTax\t\t\t{}\t\t{}".format(i,tax))
    sheet.write(j,0,"%s k"%i)
    sheet.write(j,1,tax)
    sheet.write(j,2,tax/(i*10))

# print(getIncomeTax(9000))
workBook.save("../resource/income_tax.xls")
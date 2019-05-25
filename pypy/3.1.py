#英制单位英寸和公制单位为厘米转换
value = float(input("请输入数值"))
unit = input("请输入单位")
if unit == "in" or unit == "英寸":
    print("%2.f英寸=%f厘米" % (value,value*2.54))
elif unit == "cm" or unit == "厘米":
 	print("%f厘米=%f英寸" % (value,value/2.54))
else:
 	print("请输入有效的单位")
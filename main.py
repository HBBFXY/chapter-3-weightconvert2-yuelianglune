current_weight = float(input("请输入您当前的体重（kg）"))
year_up = 0.5
print("\n未来10年体重预测情况")
print("=" * 40)
print ("{:^6} {:^12} {:^12}".format("年份","地球体重（kg）","月球体重（kg）"))
print("-" * 40)

for year in range(1,11):
    erath_weight = current_weight + year_up * year
    moon_weight = erath_weight * 0.165
    print("{:^6} {:^12.1f} {:^12.2f}".format(f"第{year}年",erath_weight,moon_weight))
print("=" * 40)# 在这个文件里编写代码

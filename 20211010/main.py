loan_type = int(input("请输入贷款类型，商业0/公积金1："))  # 输入贷款类型
loan_year = int(input("请输入贷款年限："))               # 输入贷款年限
loan_money = int(input("请输入贷款数额（万）："))         # 输入贷款数额
repayment_month = int(input("请输入还款月数："))         # 请输入还款月数
month_rate = 0           # 月利率
# 判断月利率为多少
if loan_type == 0:       # 商业贷款
    if loan_year <= 5:   # 五年以下(含五年)
        month_rate = 0.0475 / 12
    else:                # 五年以上
        month_rate = 0.049 / 12
else:                    # 公积金贷款
    if loan_year <= 5:   # 五年以下(含五年)
        month_rate = 0.0275 / 12
    else:                # 五年以上
        month_rate = 0.0325 / 12
print("--------------------------------")
# 计算每月月供
number = (1 + month_rate) ** repayment_month
month = loan_money * 10000 * (month_rate * number) / (number - 1)
print("每月月供为：%.2f" % month, end='\n')
# 计算还款总额
money = month * loan_year * 12
print("还款总额为：%.2f" % money, end='\n')
# 计算支付利息
interest = money - loan_money * 10000
print("支付利息为：%.2f" % interest, end='\n')









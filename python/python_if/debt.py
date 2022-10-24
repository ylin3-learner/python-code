# coding: utf-8
money = float(input('請輸入還款總金額: '))
time = int(input('請輸入分期數 3, 6, 12: '))
loan_fee_3 = 0.025
total_fee_3 = money* loan_fee_3
loan_fee_6 = 0.045
total_fee_6 = money * loan_fee_6
loan_fee_12 = 0.088
total_fee_12 = money * loan_fee_12

if time == 3:
	print(f'3期总手续费为:{total_fee_3:.2f}元')
	print('每期手续费: %.2f元' % (total_fee_3 / time))
	print('每期应还本金:{:.2f}元'.format(money / time))
	print('每期还款总额{:.2f}元'.format(money / time + total_fee_3 / time))
elif time == 6:
	print(f'6期总手续费为:{total_fee_6:.2f}元')
	print('每期手续费: %.2f元' % (total_fee_6 / time))
	print('每期应还本金:{:.2f}元'.format(money / time))
	print('每期还款总额{:.2f}元'.format(money / time + total_fee_6 / time))
elif time == 12:
	print(f'12期总手续费为:{total_fee_12:.2f}元')
	print('每期手续费: %.2f元' % (total_fee_12 / time))
	print('每期应还本金:{:.2f}元'.format(money / time))
	print('每期还款总额{:.2f}元'.format(money / time + total_fee_12 / time))
else:
	print('輸入錯誤, 請重新輸入\t')
	print('感謝您的配合')

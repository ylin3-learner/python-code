# coding: utf-8

# coding :utf-8



Monday = ('周一', '麻辣小龍蝦', 23, '羅宋湯')
Tue = ('週二', '宮保雞丁', 12, '紫菜蛋花湯')
Wed = ('週三', '水煮肉片', 32, '西湖牛肉麵')
Thur = ('週四', '果兒拌菜', 19, '番茄雞蛋湯')
Fri = ('週五', '小雞燉蘑菇', 33, '米酒小湯圓')

print('%s特價%s%s元, 贈送一份價值9.80000的%s' % (Monday) )
print('%s特價%s%s元, 贈送一份價值9.80000的%s' % (Tue))
print('%s特價%s%s元, 贈送一份價值9.80000的%s' % (Wed))
print('%s特價%s%s元, 贈送一份價值9.80000的%s' % (Thur))
print('%s特價%s%s元, 贈送一份價值9.80000的%s' % (Fri))
'''
line = '*'.zfill(30)
test = line.replace('0','*')
print(test)
print(id(line))
print(id(test))
'''
print('*'*30)

info = ('{}饭店不仅每天有特价,为了回馈新老客户到店就送价值{}的精美礼品,凭结账小票可进行抽奖\n 一等奖:\t价值{}欧洲游 \n 二等奖:\t价值{}的豆浆机 \n 三等奖:\t价值{}的生活大礼包').format('小北', 29.9, '一萬元', 388, '200元')
print(info)


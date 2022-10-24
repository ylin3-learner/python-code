# coding: utf-8

print( '%c' % 123 )
# print('%c' % 'ab')
# print('%c' % 10000000) %c arg not in range(0x110000)
print('%c' % 999999)

print('%u' % 1)
print('%u' % -1)

print('%f' % 3.14)
print('%f' % 1.2)
print('%f' % 12)

print('%d' % 10)
print('%d' % -10)
print('%d' % 1.2)

print('%s' % 123)

# print('%f' % '1.2') TypeError: must be real number, not str

print('{:d}'.format(1))
print('{:f}'.format(1.2))
# print('{:u}'.format(123))

print('{:o}'.format(7))
print('%o' % 8)

print('%x' % 24)
print('{:x}'.format(32))
# print('%x' % '123ab') %x format: an integer is required, not str


number = int('123ab', 16)
print(number)
print('%x' % number)

print('%e' % 1.2)



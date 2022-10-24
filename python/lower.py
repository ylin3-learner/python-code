# coding: utf-8

message_en = 'How do you do? Xiao mu;'
message_ch = '你好呀! Xiao Mu;'
message_mix = '你好呀! Xiao Mu, 今天是星期五!'

message_en_lower = message_en.lower()
message_en_casefold = message_en.casefold()

message_ch_lower = message_ch.lower()
message_ch_casefold = message_ch.casefold()

message_mix_lower = message_mix.lower()
message_mix_casefold = message_mix.casefold()

print(message_en_lower, message_en_casefold, message_en)
print(message_ch_lower, message_ch_casefold, message_ch)
print(message_mix_lower, message_mix_casefold, message_mix)

empty = ''
empty_lower = empty.lower()
empty_casefold = empty.casefold()

print('.' + empty_lower + '.', '.' + empty_casefold + '.')




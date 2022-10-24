# coding: utf-8

info = ('GitLab CI 是 GitLab 的 CI 服務，本文分享 GitLab CI 的用法，以及配置文件 .gitlab-ci.yml 的寫法。'
       'CI 是 continuous integration 的縮寫，'
       '華文叫持續整合或持續集成'
       '通常還會與 continuous delivery、continuous deployment 摻在一起'
       '有人把這些叫成 DevOps，儘管這些工程師黑話各有各的面向'
       '但他們之間涵義上的重疊率真的太高'
       '並且竊以為不斷發明新名詞、新詮釋對理解這些事物沒有幫助'
       '所以我們反璞歸真，就稱之為 CI，因為它的發音比 DevOps 簡單，'
       '也不像那兩位 CD 同學會與生活中的 CD 撞名，所以就叫 CI 吧！')

a = 'GitLab'
b = 'CI'
c = 'CD'
d = 'DevOps'
e = '*'
f = '0'
g = '$'
h = '&'

test = info.replace(a, e).replace(b, f).replace(c, g).replace(d, h)
print(test)


'''print(info)
test = info.replace(c, e)
print(test)
test_1 = info.replace(a, f)
print(test_1)
test_2 = info.replace(b, g)
print(test_2)
test_3 = info.replace(d, h)
print(test_3)
'''



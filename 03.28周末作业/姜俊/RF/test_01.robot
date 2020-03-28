*** Settings ***
Library           RequestsLibrary
Library           SeleniumLibrary
Resource          login_01.txt

*** Test Cases ***
login
    登录接口测试    17765838175    jiangjun123..
    登录接口测试    17765838176    jiangjun123..
    登录接口测试    17765838175    jiangjun123
    登录接口测试    17765838176    jiangjun123

change_page
    导航栏切换接口测试    会员    会员
    导航栏切换接口测试    商品上架    商品上架
    导航栏切换接口测试    商品管理    商品管理
    导航栏切换接口测试    查询销售    查询销售

del_pro
    删除商品    2134105
    删除商品    2134102
    删除商品    2134106
    删除商品    2134107

add_VIP
    添加会员卡    1    10    10    10    1    100000
    ...    金卡    17556
    添加会员卡    3    5    3    4    1    2000000
    ...    至尊会员卡    17556
    添加会员卡    0    80    60    60    1    1000
    ...    普卡    17556

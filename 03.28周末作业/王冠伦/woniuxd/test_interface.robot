*** Settings ***
Library           RequestsLibrary
Library           SeleniumLibrary
Resource          interface_test.txt

*** Test Cases ***
login_test
    进行登录测试    13119150855    w19971130
    进行登录测试    13119150855    w1234567
    进行登录测试    13119150856    w19971130
    进行登录测试    13119150855    !@$@#!@

add_custmoer
    进行添加会员测试    2    15    5    5    1    10000
    ...    金卡    17547
    进行添加会员测试    1    20    5    6    1    1000
    ...    普卡    17547
    进行添加会员测试    3    30    40    20    1    100000000
    ...    至尊会员卡    17547

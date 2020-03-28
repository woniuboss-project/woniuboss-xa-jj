*** Settings ***
Library           Selenium2Library
Resource          web_ui_step.txt

*** Test Cases ***
login
    登录成功    17765838175    jiangjun123..
    登录失败    17765838175    jiangjun123
    登录失败    17765838176    jiangjun123..

add_customer
    新增会员    张三    15891234567    lulula
    新增会员    \    15891234587    lulula
    新增会员    王文英    \    lulula
    新增会员    李四    15891234568    lily

outPut_pro
    商品出库    12
    商品出库    0
    商品出库    9999999

payFor
    修改支出    2    3500    2020-03-17
    修改支出    3    2000    2020:03:17
    修改支出    0    2300    2020-03-17
    修改支出    5    0    2020-03-17

reback_pro
    退货

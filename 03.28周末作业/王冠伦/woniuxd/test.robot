*** Settings ***
Resource          组织.txt
Resource          组织2.txt
Resource          login_page.txt

*** Test Cases ***
login_test
    进行登录测试    https://snailpet.com/    13119150855    w19971130

login_out_test
    进行注销测试    https://snailpet.com/    13119150855    w19971130

shopcard_test
    直接登录
    Click Element    xpath:/html/body/app-root/div/snail-menu-nav/div/a[16]
    Click Element    xpath:/html/body/app-root/div/snail-message-main/div/snail-sale/div[1]/div[2]/div[1]
    Wait Until Element Is Visible    xpath:/html/body/app-root/div/snail-message-main/div/snail-sale/div[2]/div/div/div[1]
    Element Should Contain    xpath:/html/body/app-root/div/snail-message-main/div/snail-sale/div[2]/div/div/div[1]    添加购物卡
    关闭浏览器

prompt_guide_test
    直接登录
    Click Element    xpath:/html/body/app-root/div/snail-menu-nav/div/a[16]
    Click Element    xpath:/html/body/app-root/div/snail-message-main/div/snail-sale/div[1]/div[1]/div/a
    Wait Until Element Is Visible    xpath:/html/body/app-root/div/snail-message-main/div/snail-sale/div[3]/div/div/div[1]
    Element Should Contain    xpath:/html/body/app-root/div/snail-message-main/div/snail-sale/div[3]/div/div/div[1]    提示小指南
    关闭浏览器

lost_card_test
    直接登录
    Click Element    xpath:/html/body/app-root/div/snail-menu-nav/div/a[15]
    Click Element    xpath:/html/body/app-root/div/snail-message-main/div/snail-sale/div[1]/div[1]/div/a
    Wait Until Element Is Visible    xpath:/html/body/app-root/div/snail-message-main/div/snail-sale/div[1]/div[1]/ul/li[2]
    Element Should Contain    /html/body/app-root/div/snail-message-main/div/snail-sale/div[1]/div[1]/ul/li[2]    次卡记录
    关闭浏览器

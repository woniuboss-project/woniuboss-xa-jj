*** Settings ***
Library           Selenium2Library
Library           String

*** Test Cases ***
login
    [Template]    login_template
    13110462112    3jzW.Dfa42cdLU*D@    # 正确的用户名密码
    13110462112    2213    # 错误的密码
    13110462116    3jzW.Dfa42cdLU*D@    # 错误的用户名
    [Teardown]

customer
    [Setup]    login
    [Template]    member_template
    王小明    13112345678    小白
    李小红    13112345679    小红
    李小蓝    13112345677    小红    # 宠物名重复
    李小青    13112345677    小青    # 电话号重复
    王小明    13112345688    小白2    # 姓名重复
    [Teardown]    close_the_browser

expend
    [Setup]    login
    [Template]    expend_template
    12.20    2020-03-02    #输入小数点后2位金额
    12    2020-03-02    #输入小数点后0位金额
    99.9999    2020-03-02    #输入小数点后4位金额
    34    2020-03-36    # 输入错误的时间
    [Teardown]    close_the_browser

membercard
    [Setup]    login
    [Template]    membercard_template
    蜗牛会员卡    100
    蜗牛会员卡2    100.01
    蜗牛会员卡3    eee
    2020    99
    \ \ \    10000
    [Teardown]    close_the_browser

shoppingcard
    [Setup]    login
    [Template]    shoppingcard_template
    蜗牛积分卡1    1
    蜗牛积分卡2    12.78
    蜗牛积分卡3    -1
    蜗牛积分卡4    opq
    蜗牛积分卡5    0
    [Teardown]    close_the_browser

*** Keywords ***
login_template
    [Arguments]    ${phone}    ${password_user}
    Set Selenium Implicit Wait    2
    Open Browser    https://snailpet.com    gc
    Sleep    1
    Run Keyword And Ignore Error    Click Element    css:.red_btn
    Input Text    css:input[name=phone]    ${phone}
    Input Password    css:input[name=password]    ${password_user}
    Click Element    css:.ori-btn
    sleep    0.5
    Run Keyword And Ignore Error    Click Element    css:.red_btn
    Run Keyword And Continue On Failure    Wait Until Element Is Visible    id:user_name    2
    Run Keyword And Continue On Failure    Element Should Contain    id:user_name    店长
    Delete All Cookies
    [Teardown]    close_the_browser

member_template
    [Arguments]    ${customer_name}    ${customer_phone}    ${customer_pet}
    Click Element    css:a[data-id=member]
    sleep    1
    Click Link    partial link:新增会员
    Input Text    css:input[name=name]    ${customer_name}
    Input Text    css:input[name=phone]    ${customer_phone}
    Input Text    css:input[name=petName]    ${customer_pet}
    Click Element    css:.red_btn
    sleep    0.5
    Run Keyword And Continue On Failure    Element Text Should Be    css:.js-check-box>tr>td:nth-child(4)    ${customer_phone}
    Reload Page

login
    Open Browser    https://snailpet.com    gc
    Sleep    1
    Run Keyword And Ignore Error    Click Element    css:.red_btn
    Input Text    css:input[name=phone]    13110462112
    Input Password    css:input[name=password]    3jzW.Dfa42cdLU*D@
    Click Element    css:.ori-btn
    sleep    0.5
    Run Keyword And Ignore Error    Click Element    css:.red_btn
    [Teardown]

expend_template
    [Arguments]    ${price}    ${date}
    Set Selenium Implicit Wait    2
    Click Element    css:a[data-id=expend]
    sleep    2
    ${money_text}    Get Text    css:span.ori-text
    @{money_list}    Split String    ${money_text}    元
    ${money_before}    Evaluate    float(@{money_list}[0])
    ${money_add}    Evaluate    float(${price})
    ${money_blance}    Evaluate    ${money_before}+${money_add}
    Click Link    partial link:记一笔
    ${random}    Evaluate    random.randint(1,18)    random
    Input Text    css:input[name=price]    ${price}
    Input Text    css:input[name=date]    ${date}
    Run Keyword And Ignore Error    Handle Alert    accept    timeout=0
    Click Element    css:li[data-type="${random}"]    # 随机选择类型
    Click Element    css:.red_btn
    sleep    1
    ${money_text}    Get Text    css:span.ori-text
    @{money_list}    Split String    ${money_text}    元
    ${money_after}    Evaluate    float(@{money_list}[0])
    Run Keyword And Continue On Failure    Should Be Equal    ${money_after}    ${money_blance}
    Reload Page
    sleep    1

membercard_template
    [Arguments]    ${cardname_input}    ${low_cardmoney_input}
    Set Selenium Implicit Wait    2
    sleep    0.5
    Click Element    css:a[routerlink="/treasure/member"]
    sleep    1
    Click Button    css:button.last-li
    Input Text    css:input[type=text]    ${cardname_input}    # 输入会员卡名称
    Click Element    css:div.js-card
    ${random}    Evaluate    random.randint(1,6)    random
    Click Element    css:div.js-card li:nth-child(${random})
    Input Text    css:input[type=number]    ${low_cardmoney_input}    # 输入充值金额
    Click Element    css:span.js-cl
    ${random}    Evaluate    random.randint(1,2)    random
    Click Element    css:div.wn-model-form > div:nth-child(4) \ li:nth-child(${random})
    Run Keyword And Continue On Failure    Click Element    css:.red_btn
    sleep    0.5
    ${cardname}    Get Text    css:div.unit>span
    ${low_card_money_text}    Get Text    css:div.unit:nth-child(8)>span
    ${low_money}    Evaluate    float(${low_card_money_text})
    ${low_money_input}    Evaluate    float(${low_cardmoney_input})
    Run Keyword And Continue On Failure    Should Be Equal    ${low_money}    ${low_money_input}
    Run Keyword And Continue On Failure    Should Be Equal    ${cardname}    ${cardname_input}
    sleep    0.5
    [Teardown]    page_reload

page_reload
    Reload Page

shoppingcard_template
    [Arguments]    ${cardname_input}    ${card_radio_input}
    Set Selenium Implicit Wait    2
    sleep    0.5
    Click Element    css:a[routerlink="/shopping"]
    sleep    1
    Click Element    css:div.tl-add-btn
    Input Text    css:input[type=text]    ${cardname_input}    # 输入购物卡名称
    Input Text    css:input[type=number]    ${card_radio_input}    # 输入积分比例
    Click Element    css:label.title
    Click Element    css: div.model-classify-select \ li
    Run Keyword And Continue On Failure    Click Element    css:.red_btn
    sleep    1
    ${cardname}    Get Text    css:div.tl-dev-382>span
    ${card_radio}    Get Text    css:div.right>div:nth-child(3) span
    ${card_radio}    Evaluate    float(${card_radio})
    ${card_radio_input}    Evaluate    float(${card_radio_input})
    Run Keyword And Continue On Failure    Should Be Equal    ${card_radio}    ${card_radio_input}
    Run Keyword And Continue On Failure    Should Be Equal    ${cardname}    ${cardname_input}
    sleep    0.5
    [Teardown]    page_reload

close_the_browser
    Close All Browsers

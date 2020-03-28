*** Settings ***
Library           RequestsLibrary
Library           urllib3

*** Variables ***
&{headers}        Content-Type=application/json    Connection=keep-alive    Signature=4b988eee97fbc211567995083b86b495    Cookie=snailServerTimeC=0    TE=Trailers
&{headers2}       Content-Type=application/x-www-form-urlencoded    charset=UTF-8

*** Test Cases ***
login
    [Template]    login_template
    13110462112     3jzW.Dfa42cdLU*D@
    13110462112    123456
    123456    13110462112

customer
    [Setup]
    [Template]    member_template
    王小明    13112345678    小白
    李小红    13112345679    小红
    李小蓝    13112345677    小红    # 宠物名重复
    李小青    13112345677    小青    # 电话号重复
    王小明    13112345688    小白2    # 姓名重复

expend
    [Template]    expend_template
    123    1584460800
    128.99    1584460800
    0    1584460800
    278.9    aaaaa

membercard
    [Template]    membercard_template
    蜗牛会员卡    100
    蜗牛会员卡2    100.01
    蜗牛会员卡3    eee
    2020    99
    \ \ \    10000

shoppingcard
    [Template]    shoppingcard_template
    蜗牛积分卡1    1
    蜗牛积分卡2    12.78
    蜗牛积分卡3    -1
    蜗牛积分卡4    opq
    蜗牛积分卡5    0

*** Keywords ***
login_template
    [Arguments]    ${phone}    ${password}
    Disable Warnings
    Create Session    session    https://snailpet.com    headers=&{headers}
    Sleep    1
    ${data}    Create Dictionary    phone=${phone}    password=${password}    shop_id=${EMPTY}
    ${resp}    Post Request    session    /v2/Passport/login    \    json=${data}    headers=&{headers}
    ${resp_json}    To Json    ${resp.text}
    Should Be Equal    ${resp_json[0]['datal']['user']['phone']}    13110462112
    Delete All Sessions

login
    Create Session    session    https://snailpet.com    headers=&{headers}
    Sleep    1
    ${data}    Create Dictionary    phone=13110462112    password=3jzW.Dfa42cdLU*D@    shop_id=${EMPTY}
    Post Request    session    /v2/Passport/login    \    json=${data}    headers=&{headers}

member_template
    [Arguments]    ${customer_name}    ${customer_phone}    ${pet_name}
    Disable Warnings
    Create Session    session    https://snailpet.com    headers=&{headers}
    Sleep    1
    ${data}    Create Dictionary    phone=13110462112    password=3jzW.Dfa42cdLU*D@    shop_id=${EMPTY}
    Post Request    session    /v2/Passport/login    \    json=${data}    headers=&{headers}
    &{pet}    Create Dictionary     \ \ birthday=      \ \ \ \ \ mark=      \ \ \ \ \ name= ${pet_name}     \ \ \ \ \ sex=      \ \ \ \ \ color=
    ...     \ \ \ \ \ weight_new= 0     \ \ \ \ \ speciesId=
    &{data}    Create Dictionary    addr=    cardNumber=    cardNumber=    name=${customer_name}    phone=${customer_phone}
    ...    pets=[&{pet}]     \ phone= 15612345678     \ spare_phone=      \ sex= 1     \ is_spending_msg= 1     \ is_open_upgrade= 1
    ...     \ shopId= 17542     \ member_tags=      \ shop_id= 17542
    ${resp}    Post Request    session    /v2/Members/add    \    json=&{data}    headers=&{headers}
    Should Match Regexp    ${resp.text}    \\d+
    Delete All Sessions

expend_template
    [Arguments]    ${price}    ${date}
    Disable Warnings
    Create Session    session    https://snailpet.com    headers=&{headers}
    Sleep    1
    ${data}    Create Dictionary    phone=13110462112    password=3jzW.Dfa42cdLU*D@    shop_id=${EMPTY}
    Post Request    session    /v2/Passport/login    \    json=${data}    headers=&{headers}
    ${data}    Create Dictionary    actionTime=${date}    type=1    mark=    amount=${price}    shopId=17542
    ...    shop_id=17542
    ${resp}    Post Request    session    /v2/Shop/addSpending    ${data}    headers=&{headers2}
    ${resp_json}    To Json    ${resp.text}
    Should Be Equal    ${resp_json[0]['error']}    0
    Delete All Sessions

membercard_template
    [Arguments]    ${cardname_input}    ${low_cardmoney_input}
    Disable Warnings
    Create Session    session    https://snailpet.com    headers=&{headers}
    Sleep    1
    ${data}    Create Dictionary    phone=13110462112    password=3jzW.Dfa42cdLU*D@    shop_id=${EMPTY}
    Post Request    session    /v2/Passport/login    \    json=${data}    headers=&{headers}
    &{data}    Create Dictionary    background=0    discount=10    discount_for_combination=10    discountForService=10    enablePlus=1
    ...    minPrice=${low_cardmoney_input}    name=${cardname_input}    shop_id=17542    shopId=17542
    ${resp}    Post Request    session    /v2/Shop/setMemberLevel    \    json=&{data}    headers=&{headers}
    ${resp_json}    To Json    ${resp.text}
    Should Be Equal    ${resp_json[0]['error']}    0
    Delete All Sessions

shoppingcard_template
    [Arguments]    ${cardname_input}    ${card_radio_input}
    Disable Warnings
    Create Session    session    https://snailpet.com    headers=&{headers}
    Sleep    1
    ${data}    Create Dictionary    phone=13110462112    password=3jzW.Dfa42cdLU*D@    shop_id=${EMPTY}
    Post Request    session    /v2/Passport/login    \    json=${data}    headers=&{headers}
    &{data}    Create Dictionary    exp_time_type=0    integral_percentage=${card_radio_input}    name=${cardname_input}     shop_id=17542    shopId=17542
    ${resp}    Post Request    session    /v2/shopping_card/save    \    json=&{data}    headers=&{headers}
    ${resp_json}    To Json    ${resp.text}
    Should Be Equal    ${resp_json[0]['error']}    0
    Delete All Sessions

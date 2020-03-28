Action()
{	
//	lr_start_transaction("login")
//	定义检查点
	web_reg_find("SaveCount=check_login",
		"Text=user",
		LAST);
	
	
	web_reg_save_param_json(
		"ParamName=check_login",
		"QueryString=$..error",
		SEARCH_FILTERS,
		LAST);
	//执行方法
	web_submit_data("login_shop",
		"Action=https://snailpet.com/v2/Passport/login",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=password", "Value={password}", ENDITEM,
		"Name=phone", "Value={phone}", ENDITEM,
		"Name=shop_id", "Value={shopid}", ENDITEM,
		LAST);

	lr_log_message(lr_eval_string("{check_login}"));
	
	//进行断言
	if(atoi(lr_eval_string("{check_login}")) == 0){
		lr_output_message("test_ok");
	}else{
		lr_output_message("test_fail");
	}
	

	
	
	//添加会员
	web_reg_save_param_json(
		"ParamName=check_add",
		"QueryString=$.error",
		SEARCH_FILTERS,
		LAST);

	
	web_custom_request("web_custom_request",
		"URL=https://snailpet.com/v2/Members/add",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"addr\":\"\",\"cardNumber\": \"1111\",\"mark\": \"\", \"name\":\"{p_name}\", \"pets\": [{\"birthday\":\"\",\"mark\": \"\",\"name\": \"{cat_name}\",\"sex\": {sex},\"color\": \"\",\"weight_new\": 3,\"speciesId\": 16,\"is_sterilization\": 1}],\"phone\": \"{phone}\",\"spare_phone\": \"\",\"sex\":{sex} ,\"is_spending_msg\": 0,\"is_open_upgrade\": {sex}，\"shopId\":\"{shopid}\",\"member_tags\": \"44252,44253,44254\",\"shopId\": {shopid}}",
		LAST);
	
	lr_log_message(lr_eval_string("{check_add}"));
	
	if(atoi(lr_eval_string("{check_add}")) == 1){
		lr_output_message("add_ok");
	}else{
		lr_output_message("add_fail");
	}

	//小工具
	web_reg_save_param_json(
		"ParamName=check_add_pro",
		"QueryString=$..error",
		"SelectAll=Yes",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	web_custom_request("web_custom_request",
		"URL=https://snailpet.com/v2/analysis_es/action",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body= \"shopId\": \"{shopid}\",\"ex_current_page\": \"首页\",\"ex_kind\": \"点击\",\"ex_next_page\": \"小工具\",\"ex_title\": \"小工具\"",
		LAST);
	
	if(atoi(lr_eval_string("{check_add}")) == 1){
		lr_output_message("test_ok");
	}else{
		lr_output_message("test_fail");
	}
	
	//添加支出
	web_reg_save_param_json(
		"ParamName=check_payFor",
		"QueryString=$..error",
		"SelectAll=Yes",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	web_custom_request("payFor",
		"URL=https://snailpet.com/v2/Shop/addSpending",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body=\"actionTime\":\"1585238400\",\"type\"：{sex}\"mark\"=\"%E6%88%BF%E7%A7%9F\",\"amount\":2900,\"shopId\":{shopid}",
		LAST);
	lr_output_message(lr_eval_string("{check_payFor}"));
	if(atoi(lr_eval_string("{check_payFor}")) == 1){
		lr_output_message("test_ok");
	}else{
		lr_output_message("test_fail");
	}
	
	//商品入库
	web_reg_save_param_json(
		"ParamName=check_inputPro",
		"QueryString=$.data",
		"SelectAll=Yes",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	
	web_custom_request("input_product",
		"URL=https://snailpet.com/v2/product/update/stocks",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body=\"productId\": 2133949,\"shopId\": \"{shopid}\",\"number\": 13,\"mark\": \"\",\"inPrice\": 30,\"shelf_life\": 0,\"production_time\": null,\"exp_time\": null,\"shop_id\": 17556",
		LAST);
	
	lr_output_message(lr_eval_string("{check_inputPro}"));
	if(lr_eval_string("{check_inputPro}") == "{success}"){
		lr_output_message("test_ok");
	}else{
		lr_output_message("test_fail");
	}



	return 0;
}

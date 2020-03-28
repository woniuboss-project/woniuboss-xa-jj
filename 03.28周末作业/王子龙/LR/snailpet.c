snailpet()
{
	web_reg_save_param_json(
		"ParamName=resp_json",
		"QueryString=$",
		//"QueryString=$.data.user.phone",
		"SelectAll=No",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	lr_start_transaction("login");

	web_custom_request("web_custom_request",
		"URL=https://snailpet.com/v2/Passport/login",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"RecContentType=application/json",
		"EncType=application/json",
		"Body={\"phone\":\"{login_phone}\",\"password\":\"{login_password}\",\"shop_id\":null}",
		LAST);
	if(strcmp(lr_eval_string("{resp_json}"),lr_eval_string("{login_phone}"))==0){
		lr_end_transaction("login", LR_PASS);

	}else{
		lr_end_transaction("login", LR_FAIL);

	}
	
	web_reg_save_param_json(
		"ParamName=resp_json",
		"QueryString=$.error",
		"SelectAll=No",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	lr_start_transaction("add_member");
	web_custom_request("web_custom_request",
		"URL=https://snailpet.com/v2/Shop/addSpending",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"RecContentType=application/json",
		"EncType=application/json",
		"Body={\"addr\": \"\",\"cardNumber\": \"\",\"mark\": \"\",\"name\": \"{member_name}\",\"pets\": [{\"birthday\": \"\", \"mark\": \"\",\"name\": \"{member_pet}\",\"sex\": \"\",\"color\": \"\",\"weight_new\": 0,\"speciesId\": \"\" }],\"phone\": \"{member_phone}\",\"spare_phone\": \"\",\"sex\": 1,\"is_spending_msg\": 1,\"is_open_upgrade\": 1,\"shopId\": \"17542\",\"member_tags\": \"\",\"shop_id\": 17542}",
		LAST);
	if(atoi("{resp_json}")==0){
		lr_end_transaction("add_member", LR_PASS);

	}else{
		lr_end_transaction("add_member", LR_FAIL);

	}
	
	web_reg_save_param_json(
		"ParamName=resp_json",
		"QueryString=$.error",
		"SelectAll=No",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	lr_start_transaction("expend");

	web_submit_data("web_submit_data",
		"Action=https://snailpet.com/v2/Shop/addSpending",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=actionTime", "Value={spend_date}", ENDITEM,
		"Name=type", "Value=15", ENDITEM,
		"Name=mark", "Value=", ENDITEM,
		"Name=amount", "Value={spend_amount}", ENDITEM,
		"Name=shopId", "Value=17542", ENDITEM,
		"Name=shop_id", "Value=17542", ENDITEM,
		LAST);
	if(atoi("{resp_json}")==0){
		lr_end_transaction("expend", LR_PASS);

	}else{
		lr_end_transaction("expend", LR_FAIL);

	}
	
	web_reg_save_param_json(
		"ParamName=resp_json",
		"QueryString=$.error",
		"SelectAll=No",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	lr_start_transaction("membercard");
	web_custom_request("web_custom_request",
		"URL=https://snailpet.com/v2/Shop/setMemberLevel",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"RecContentType=application/json",
		"EncType=application/json",
		"Body={\"name\": \"{membercard_name}\", \"minPrice\": {membercard_low_price},\"enablePlus\": 1,\"background\": 1,\"discount\": 10,\"discountForService\": 10,\"discount_for_combination\": 10,\"shopId\": 17542,\"shop_id\": 17542}",
		LAST);
	if(atoi("{resp_json}")==0){
		lr_end_transaction("membercard", LR_PASS);

	}else{
		lr_end_transaction("membercard", LR_FAIL);

	}
	
	web_reg_save_param_json(
		"ParamName=resp_json",
		"QueryString=$.error",
		"SelectAll=No",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	lr_start_transaction("shoppingcard");
	web_custom_request("web_custom_request",
		"URL=https://snailpet.com/v2/shopping_card/save",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"RecContentType=application/json",
		"EncType=application/json",
		"Body={\"shopId\": \"17542\",\"name\": \"{shoppingcard_name}\",\"integral_percentage\": {shoppingcard_radio},\"exp_time_type\": 0,\"shop_id\": 17542}",
		LAST);
	if(atoi("{resp_json}")==0){
		lr_end_transaction("shoppingcard", LR_PASS);

	}else{
		lr_end_transaction("shoppingcard", LR_FAIL);

	}	

	return 0;
}

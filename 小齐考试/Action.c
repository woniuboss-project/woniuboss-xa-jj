Action()
{   

	web_reg_save_param_json(
		"ParamName=login",
		"QueryString=$.error",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);

	web_submit_data("login-page",
		"Action=https://snailpet.com/v2/Passport/login",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=uname", "Value=13772135029", ENDITEM,
		"Name=password", "Value=123456", ENDITEM,
		"Name=shop-id", "Value=null", ENDITEM,
		LAST);

	lr_log_message(lr_eval_string("{login}"));
	if (atoi(lr_eval_string("{login}")) == 1){
		lr_output_message("login-pass");
	}else{
		lr_output_message("login-fail");
	}

   
	
	web_reg_save_param_json(
		"ParamName=addcustomer",
		"QueryString=$.error",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);

	web_custom_request("web_custom_request",
		"URL=https://snailpet.com/v2/Shop/setMemberLevel",
		"Method=post",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"addr\": \"\",\n"
		"  \"cardNumber\": \"\",\n"
		"  \"mark\": \"\",\n"
		"  \"name\": \"yummy\",\n"
		"  \"pets\": [\n"
		"    {\n"
		"      \"birthday\": \"\",\n"
		"      \"mark\": \"\",\n"
		"      \"name\": \"mini\",\n"
		"      \"sex\": 1,\n"
		"      \"color\": \"red\",\n"
		"      \"weight_new\": 0,\n"
		"      \"speciesId\": \"1\",\n"
		"      \"is_sterilization\": 1\n"
		"    }\n"
		"  ],\n"
		"  \"phone\": \"13772135029\",\n"
		"  \"spare_phone\": \"\",\n"
		"  \"sex\": 1,\n"
		"  \"is_spending_msg\": 1,\n"
		"  \"is_open_upgrade\": 1,\n"
		"  \"shopId\": \"17533\",\n"
		"  \"member_tags\": \"\",\n"
		"  \"shop_id\": 17533\n"
		"}",
		LAST);

	lr_log_message(lr_eval_string("{addcustomer}"));
	
	
	if (atoi(lr_eval_string("{addcustomer}")) == 1){
		lr_output_message("add-pass");
	}else{
		lr_output_message("add-fail");
	}

	
	
	
	
	web_reg_save_param_json(
		"ParamName=paymant",
		"QueryString=$.error",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);

	
	
	web_submit_data("paymant",
		"Action=https://snailpet.com/v2/Shop/addSpending",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=actionTime", "Value=1583683200", ENDITEM,
		"Name=type", "Value=8", ENDITEM,
		"Name=mark", "Value=shop", ENDITEM,
		"Name=amount", "Value=300", ENDITEM,
		"Name=shopid", "Value=17533", ENDITEM,
		"Name=shop_id", "Value=17533", ENDITEM,
		LAST);

	lr_log_message(lr_eval_string("{paymant}"));

	
	if (atoi(lr_eval_string("{paymant}")) == 1){
		lr_output_message("pay-pass");
	}else{
		lr_output_message("pay-fail");
	}
	
	
	
	
	
	
	
	web_reg_save_param_json(
		"ParamName=merchanindise",
		"QueryString=$.error",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);

	web_submit_data("merchandise",
		"Action=https://snailpet.com/v2/User/getUserInfo?shop_id=17533",
		"Method=GET",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		LAST);
 lr_log_message(lr_eval_string("{merchanindise}"));
 
	if (atoi(lr_eval_string("{merchanindise}")) == 1){
		lr_output_message("query-pass");
	}else{
		lr_output_message("query-fail");
	}
	
 
 
 

	web_reg_save_param_json(
		"ParamName=add-code",
		"QueryString=$.error",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
  

	web_submit_data("addcustomer",
		"Action=https://snailpet.com/v2/Shop/setMemberLevel",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=background", "Value=2", ENDITEM,
		"Name=discount", "Value=10", ENDITEM,
		"Name=discount_for_combination", "Value=10", ENDITEM,
		"Name=discountForService", "Value=10", ENDITEM,
		"Name=enablePlus", "Value=1", ENDITEM,
		"Name=minPrice", "Value=500", ENDITEM,
		"Name=name", "Value=yummy", ENDITEM,
		"Name=shop_id", "Value=17533", ENDITEM,
		"Name=shopId", "Value=17533", ENDITEM,
		LAST);
 lr_log_message(lr_eval_string("{add-code}"));
 
 	if (atoi(lr_eval_string("{add-code}")) == 1){
		lr_output_message("addcode-pass");
	}else{
		lr_output_message("addcode-fail");
	}
	
	
	return 0;
}

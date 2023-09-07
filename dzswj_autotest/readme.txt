层级说明

api---所测试接口的目录，可以再细分目录
	api_service.py------------------存放要测试的接口
	get_token.py--------------------获取cookie
	
case---存放测试用例
	conftest.py---------------------pytest框架自带的，但是要自己新建，里面写固件，百度该py文件的作用
	test_bsjd_service_info.py-------写测试用例脚本
	
common---公共方法封装目录
	connect_mysql.py----------------封装的连接mysql的方法
	connect_oracle.py---------------封装的连接oracle的方法
	logger.py-----------------------封装log日志方法
	request_util.py-----------------封装的公共请求方法，里面有个类变量session
	yml_util.py---------------------封装的对yml文件操作的方法
	
data---放测试数据或者保存测试数据的目录
	save_data-----------------------保存测试用例产生的一些数据，比如接口返回的一些数据，下游接口还需要使用时
	test_data-----------------------测试用例的测试数据
		api_GetBsjd_data.yml--------测试用例脚本使用的测试数据
		api_SubGzsb_data.yml--------测试用例脚本使用的测试数据
	upload_data---------------------上传文件接口的测试数据
	
logs---保存日志文件的目录

reports---保存测试报告的文件，在index..html中

temp---保存临时生成的测试报告的json数据，供allure生成html报告

根目录
	debug_talk.py-------------------yml文件测试用例动态参数热加载，目前没有使用到，还没学会
	getpathinfo.py------------------获取项目根目录方法
	pytest.ini----------------------pytest框架的配置文件
	requirements.txt----------------运行环境框架要求，可以一次执行，方法请百度
	run_main.py---------------------主函数
	
获取会话主要思想：
测试用例执行前会先执行conftest.py文件，里面有一个方法get_token，调用了Get_Token().get_token()里面的登录方法，登录方法用的是RequestUtil().all_send_request中的公共请求方法，all_send_request请求方法又保存了类变量session，只要后续的接口调用仍然使用公共请求方法RequestUtil().all_send_request(),都能共享该方法的session，实现session共享

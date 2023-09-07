层级说明

api---所测试接口的目录，可以再细分目录
	api_service.py------------------存放要测试的接口
	get_token.py--------------------unittest里面没作用，没删除
	
case---存放测试用例
	test_bsjd_service_info.py-------写测试用例脚本
	
common---公共方法封装目录
	connect_mysql.py----------------封装的连接mysql的方法
	connect_oracle.py---------------封装的连接oracle的方法
	logger.py-----------------------封装log日志方法
	dl_session.py-------------------获取登录会话的接口
	fixture.py----------------------夹具
	HTMLTestRunner.py---------------不用管
	request_util.py-----------------封装的公共请求方法，里面有个类变量session，unittest里面没作用，没删除
	yml_util.py---------------------封装的对yml文件操作的方法
	
data---放测试数据或者保存测试数据的目录
	save_data-----------------------保存测试用例产生的一些数据，比如接口返回的一些数据，下游接口还需要使用时
	test_data-----------------------测试用例的测试数据
		api_GetBsjd_data.yml--------测试用例脚本使用的测试数据
		api_SubGzsb_data.yml--------测试用例脚本使用的测试数据
	upload_data---------------------上传文件接口的测试数据

demo---我自己做测试用的
	
logs---保存日志文件的目录

reports---保存测试报告的文件，在index..html中


根目录
	getpathinfo.py------------------获取项目根目录方法
	run_main.py---------------------主函数
	
获取会话主要思想：
有一个夹具fixture.py，里面有个类变量，这个夹具的作用是继承它的类执行脚本前，会先执行夹具里面的方法；dl_session.py是获取登录会话的接口，他继承了夹具那个类，也就有了夹具类的属性和方法；然后api_service.py里面的类继承了dl_session.py的类，此时注意api_service.py里面接口调用的方式，都用了session会话
总结：api_service.py接口被调用前，会先执行被他继承的类中的方法（Login_get_session），执行Login_get_session时保存了会话变量，api接口调用是用这个session去调用可以做到会话共享
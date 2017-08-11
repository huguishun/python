from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
browser = webdriver.Chrome()
browser.get("https://walk.paralworld.com")
# 登陆
browser.find_element_by_xpath("html/body/div[1]/div/div[2]/ul/li[2]/a").click()
browser.find_element_by_name("username").clear()
browser.find_element_by_name("username").send_keys("username")
browser.find_element_by_name("password").clear()
browser.find_element_by_name("password").send_keys("123456")
browser.find_element_by_class_name("ps-btn").click()
# 获得当前窗口
current = browser.current_window_handle
time.sleep(5)
browser.find_element_by_link_text("发布需求").click()
# 获得所有窗口
allcurrent = browser.window_handles
for headle in allcurrent:
	# 判断是否是当前窗口
	if headle != current:
		browser.switch_to_window(headle)
		time.sleep(3)
		browser.find_element_by_class_name("choose-title-span01").click()
		time.sleep(2)
		browser.find_element_by_class_name("choose-detail-sp01").click()
		browser.find_element_by_id("wk-item-tit").send_keys("这是个测试")
		browser.find_element_by_id("pbInput").send_keys("100")
		browser.find_element_by_id("oneBtn").click()
		# 移除原生js，直接输入日期时间
		js = "document.getElementById('wkbiddataend').removeAttribute('readonly')"
		browser.execute_script(js)
		browser.find_element_by_xpath(".//*[@id='wkbiddataend']").send_keys("2017-00-10 16:00:00")
		# 移除原生js，直接输入日期时间
		js = "document.getElementById('wkbiddataend').removeAttribute('readonly')"
		browser.execute_script(js)
		browser.find_element_by_xpath(".//*[@id='wkworddataend']").send_keys("2017-00-11 11:00:00")
		browser.find_element_by_id("wk-item-cont").send_keys("这是一个测试脚本")
		browser.find_element_by_class_name("step2-confirm-tj").click()
		time.sleep(2)
		browser.find_element_by_id("onePayBtn").click()
		time.sleep(2)
		# 支付
		browser.find_element_by_xpath("html/body/div[3]/div[2]/div[2]/div/form/div[1]/div[2]/div[1]").click()
		browser.find_element_by_id("pay-input-value").send_keys("654321")
		# 验证码
		browser.find_element_by_class_name("get-authcode").click()
		time.sleep(30)
		browser.find_element_by_link_text("提交").click()
		browser.find_element_by_link_text("查看订单详情").click()
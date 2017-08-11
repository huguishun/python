# 平行威客——selenium自动化脚本
基于selenium编写的自动化脚本，包含威客首页登陆、发布需求、支付过程。
# 部分说明：
移除原生js，直接输入日期时间
js = "document.getElementById('wkbiddataend').removeAttribute('readonly')"
browser.execute_script(js)
#  
这里是针对弹出的日期选择框，由于网页上通过readonly关键字的原因，这个日期只能读不能写入，尝试过多重定位这个日期选择框依旧没解决，只能通过修改原生js，移除readonly来直接在脚本中输入日期时间。
支付过程中短信验证码问题：在脚本中设置等待时间，手动在网页上输入验证码。
支付密码的输入框做了隐藏，花费了部分时间解决，原理是需要先定位到输入框整体并且做点击操作，然后再定位input这个标签，才能进行输入。（大概就这意思，反正很麻烦）

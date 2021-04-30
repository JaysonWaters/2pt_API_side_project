'''
Jayson Waters
csc3950
2pt API side project
'''

import MailboxValidator

mbv = MailboxValidator.SingleValidation('7ADEY8P743EPI0XG9IHY')
possible_email = input("Enter the email address you would like to validate:")
results = mbv.ValidateEmail(possible_email)

if results is None:
		print("Error connecting to API.\n")#if you can't connect to the API

elif results['error_code'] == '':#if ther are not errors the API
	print('email_address = ' + results['email_address'] + "\n")# lets you know if there is input
	print('domain = ' + results['domain'] + "\n")#lets you know if there is an @domain
	print('is_free = ' + results['is_free'] + "\n")#Whether the email address is from a free email provider
	print('is_syntax = ' + results['is_syntax'] + "\n")#Whether the email address is syntactically correct
	print('is_domain = ' + results['is_domain'] + "\n")#Whether the email address has a valid MX record in its DNS entries
	print('is_smtp = ' + results['is_smtp'] + "\n")#Whether the mail servers specified in the MX records are responding to connections
	print('is_verified = ' + results['is_verified'] + "\n")#Whether the mail server confirms that the email address actually exist
	print('is_server_down = ' + results['is_server_down'] + "\n")#Whether the mail server is currently down or unresponsive
	print('is_greylisted = ' + results['is_greylisted'] + "\n")#Whether the mail server employs greylisting where an email has to be sent a second time at a later time.
	print('is_disposable = ' + results['is_disposable'] + "\n")#Whether the email address is a temporary one from a disposable email provider
	print('is_suppressed = ' + results['is_suppressed'] + "\n")#Whether the email address is in our blacklist
	print('is_role = ' + results['is_role'] + "\n")#Whether the email address is a role-based email address like an admin
	print('is_high_risk = ' + results['is_high_risk'] + "\n")#Whether the email address contains high risk keywords
	print('is_catchall = ' + results['is_catchall'] + "\n")#Whether the email address is a catch-all address
	print('mailboxvalidator_score = ' + str(results['mailboxvalidator_score']) + "\n")#Email address reputation score. Score > 0.70 means good; score > 0.40 means fair; score ≤ 0.40 means poor
	print('time_taken = ' + str(results['time_taken']) + "\n")#The time taken to get the results in seconds.
	print('status = ' + results['status'] + "\n") #let you know if the email is taken
	print('credits_available = ' + str(results['credits_available']) + "\n")#Tells me how many query credits I have left since I only 300 with the free version of the API
else:
	print('error_code = ' + results['error_code'] + "\n")
	print('error_message = ' + results['error_message'] + "\n")

import telepot
import time
import os

bot = telepot.Bot("YOUR_API_TOKEN_HERE") 							
master_id = 999999999	# Your User ID

def messageHandler(message):
	#print message 	# Can print message to find your own user ID
	content_type, chat_type, user_id = telepot.glance2(message)
	if user_id == master_id:
		if content_type == "text":
			text = message["text"]
			if '/shell:' in text:
				cmd = text[7:]
				proc = os.popen(cmd)
				bot.sendMessage(user_id, proc.read())
			elif '/download:' in text:
				path = text[10:]
				doc = open(path, 'rb')
				bot.sendDocument(user_id, doc)
		elif content_type == "document":
			file_id = message["document"]["file_id"]
			file_name = message["document"]["file_name"]
			bot.downloadFile(file_id, file_name)

def main():
	bot.notifyOnMessage(messageHandler)
	while True:
		time.sleep(10)

main()
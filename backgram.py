import telepot
import time
import os

# telegram api token
API_TOKEN = "YOUR_API_TOKEN_HERE"

# telegram account id
# your bot will only listen to commands from this account
MASTER_ID = 999999999

bot = telepot.Bot(API_TOKEN)


def message_handler(message):
    content_type, chat_type, user_id = telepot.glance2(message)

    if user_id == MASTER_ID:
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
    bot.notifyOnMessage(message_handler)

    while True:
        time.sleep(10)


if __name__ == '__main__':
    main()

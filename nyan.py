from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings
from random import randint


class NyanPlugin(WillPlugin):

    @hear("nyan", case_sensitive=False)
    def nyan(self, message):
        resp = """<pre>
-_-_-_-_-_-_-_,------,
_-_-_-_-_-_-_-|   /\_/\  
-_-_-_-_-_-_-~|__( ^ .^) 
              ""  ""     </pre>
        """
        colors = ["yellow", "red", "green", "purple", "gray"]
        rand = randint(0,4)
        self.say(resp, html=True, message=message, color=colors[rand])

    @respond_to("source", case_sensitive=False)
    def github_url(self, message):
        self.reply(message, "My source code is located at https://github.com/Wyvryn/NyanBot")

    @respond_to("murica!", case_sensitive=False)
    def murica(self, message):
        self.reply(message, "http://i.imgur.com/ZQzmPHM.gif")

    @respond_to("classic", case_sensitive=False)
    def classic(self, message):
        self.reply(message, "http://i.imgur.com/ssKsGid.gif")

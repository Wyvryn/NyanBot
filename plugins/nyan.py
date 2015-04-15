from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings
from random import randint


class NyanPlugin(WillPlugin):

    @hear("nyan", case_sensitive=False)
    def hello(self, message):
        resp = """<pre>
-_-_-_-_-_-_-_,------,
_-_-_-_-_-_-_-|   /\_/\  
-_-_-_-_-_-_-~|__( ^ .^) 
              ""  ""     </pre>
        """
        colors = ["yellow", "red", "green", "purple", "gray"]
        rand = randint(0,4)
        self.say(resp, html=True, message=message, color=colors[rand])

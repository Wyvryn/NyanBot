from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings
from jira.client import JIRA
import os

class JiraPlugin(WillPlugin):

    @hear("!jira (?P<case_number>.*)", case_sensitive=False)
    def jira_info(self, message, case_number=None):
        jira = JIRA(os.environ.get('JIRA_SERVER'),
                    basic_auth=(os.environ.get('JIRA_USERNAME'),
                                os.environ.get('JIRA_PASSWORD')))
        case_number = case_number.upper()
        try:
            ticket = jira.issue(case_number)
            name = ticket.fields.summary
            status = ticket.fields.status
            url = "http://jira.texturallc.net/browse/" + case_number
            resp = str(case_number) + "<br /><a href='" + str(url) + "'>JIRA Link</a><br />Name: " + str(name) + "<br />Status: " + str(status)
            self.say(resp, message, html=True)
        except:
            self.say("I couldn't find that.", message)

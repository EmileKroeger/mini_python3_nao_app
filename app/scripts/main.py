"""
An example of a Python Script as an app for NAO/Pepper
"""

__version__ = "0.1.0"

__author__ = 'Emile Kroeger'
__email__ = 'e.kroeger@unitedrobotics.group'

import qi

class Activity:
    "A sample standalone app, that demonstrates simple Python usage"
    APP_ID = "mini_python3_nao_app"
    def __init__(self, qiapp):
        self.qiapp = qiapp
        self.session = qiapp.session

    def on_start(self):
        try:
            self.session.service("ALTextToSpeech").say("Hello everybody! check out my eyes")
            self.session.service("ALLeds").rasta(2.0)
            self.session.service("ALTextToSpeech").say("Neat wasn't it?")
        finally:
            # Note, until we do this, this will run forever (which is sometimes what we want)
            self.stop()

    def stop(self):
        "Standard way of stopping the application."
        self.qiapp.stop()

if __name__ == "__main__":
    qiapp = qi.Application()
    qiapp.start()
    activity = Activity(qiapp)
    qi.runAsync(activity.on_start)
    qiapp.run()

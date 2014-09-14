from jinja2 import Markup


class timeagojs(object):
    def __init__(self, timestamp):
        self.timestamp = timestamp

    def render(self):
        return Markup("%s") % self.timestamp.strftime("%Y-%m-%dT%H:%M:%S Z")

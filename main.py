from tornado import ioloop, web

from forms import ConfigForm
from handlers import BaseHandler
import parser

class MainHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('base.html')


class FormHandler(BaseHandler):
    def get(self, *args, **kwargs):
        form = ConfigForm()
        self.render('form.html', context={'form': form})


if __name__ == '__main__':
    application = web.Application([
        (r'^/$', MainHandler),
        (r'^/form$', FormHandler),
    ],
        debug=True,
        autoreload=True,
    )

    application.listen(8000)
    ioloop.IOLoop.current().start()

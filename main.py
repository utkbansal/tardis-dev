from tornado import ioloop, web

from forms import ConfigForm
from handlers import BaseHandler
from test import create_yaml
import parser

class MainHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('base.html')


class FormHandler(BaseHandler):
    def get(self, *args, **kwargs):
        form = ConfigForm()
        self.render('form.html', context={'form': form})

    def post(self, *args, **kwargs):
        print self.request.arguments

        form = ConfigForm(self.request.arguments)
        if form.validate():
            print 'here'
            data = create_yaml(self.request.arguments)
            data.seek(0)
            self.set_header('Content-Type', 'text/yaml')
            self.set_header('Content-Disposition',
                            'attachment; filename=test.yml')
            self.write(data.read())
            self.finish()

        print form.errors


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

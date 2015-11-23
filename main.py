from tornado import ioloop, web

from forms import ConfigForm
from handlers import BaseHandler
from parser import populate_form_class
from test import create_yaml


# class MainHandler(BaseHandler):
#     def get(self, *args, **kwargs):
#         self.render('base.html')


class FormHandler(BaseHandler):
    def get(self, *args, **kwargs):
        populate_form_class()
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
                            'attachment; filename=config.yml')
            self.write(data.read())
            self.finish()
        else:
            return self.render('form.html', context={'form': form})


if __name__ == '__main__':
    application = web.Application([
        # (r'^/$', MainHandler),
        (r'^/$', FormHandler),
    ],
        debug=True,
        autoreload=True,
    )

    application.listen(8000)
    ioloop.IOLoop.current().start()

from tornado.web import RequestHandler

from settings import jinja_env


class BaseHandler(RequestHandler):
    """
    Basic handler that renders all templates using Jinja2
    """

    def render(self, template_name, context=None, **kwargs):
        if not context:
            context = {}
        context.update(self.get_template_namespace())
        self.write(jinja_env.get_template(template_name).render(context))

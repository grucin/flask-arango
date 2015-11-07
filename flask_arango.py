from flask import _app_ctx_stack

from pyArango.connection import Connection


class Arango(object):

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        app.teardown_appcontext(self._teardown)

    def _teardown(self, exception):
        # pylint: disable=unused-argument,no-self-use
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if hasattr(ctx, 'arango'):
                ctx.arango.session.close()
                del ctx.arango

    @property
    def connection(self):  # pylint: disable=no-self-use
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'arango'):
                ctx.arango = Connection(self.app.config['ARANGO_URL'])
            return ctx.arango

    @property
    def db(self):  # pylint: disable=invalid-name
        return self.connection[self.app.config['ARANGO_DB']]

    @property
    def gdb(self):
        return self.db.graphs[self.app.config['ARANGO_GRAPH']]

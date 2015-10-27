import unittest

from flask import Flask
from pyArango.graph import Graph, EdgeDefinition
from pyArango.collection import Collection, Edges

from flask_arango import Arango


class FlaskRequestTests(unittest.TestCase):

    def setUp(self):
        self.app = Flask('test')
        self.context = self.app.test_request_context('/')
        self.context.push()

    def tearDown(self):
        self.context.pop()


class FlaskArangoConfigTests(FlaskRequestTests):

    def setUp(self):
        super(FlaskArangoConfigTests, self).setUp()
        self.app.config['ARANGO_URL'] = 'http://localhost:8529'
        self.app.config['ARANGO_DB'] = 'flask_arango_test'
        self.app.config['ARANGO_GRAPH'] = 'GraphTest'

    def test_direct_initialization(self):
        arango = Arango(self.app)
        self.assertIsNotNone(arango.connection)

    def test_init_app(self):
        arango = Arango()
        arango.init_app(self.app)
        self.assertIsNotNone(arango.connection)


class FlaskArangoDatabaseTests(FlaskRequestTests):

    def setUp(self):
        super(FlaskArangoDatabaseTests, self).setUp()
        self.app.config['ARANGO_URL'] = 'http://localhost:8529'
        self.app.config['ARANGO_DB'] = 'flask_arango_test'
        self.app.config['ARANGO_GRAPH'] = 'GraphTest'
        self.arango = Arango()
        self.arango.init_app(self.app)
        if not self.arango.connection.hasDatabase('flask_arango_test'):
            self.arango.connection.createDatabase('flask_arango_test')

    def test_database_access(self):
        self.assertIsNotNone(self.arango.db)


class FlaskArangoGraphTests(FlaskRequestTests):

    def setUp(self):
        # pylint: disable=no-init,too-few-public-methods,unused-variable
        super(FlaskArangoGraphTests, self).setUp()
        self.app.config['ARANGO_URL'] = 'http://localhost:8529'
        self.app.config['ARANGO_DB'] = 'flask_arango_test'
        self.app.config['ARANGO_GRAPH'] = 'GraphTest'
        self.arango = Arango()
        self.arango.init_app(self.app)
        if not self.arango.connection.hasDatabase('flask_arango_test'):
            self.arango.connection.createDatabase('flask_arango_test')

        class EdgeTest(Edges):  # pylint: disable=no-init
            pass

        class FromTest(Collection):
            pass

        class ToTest(Collection):
            pass

        class GraphTest(Graph):
            _edgeDefinitions = (EdgeDefinition(
                'EdgeTest',
                fromCollections=['FromTest'],
                toCollections=['ToTest']),)
            _orphanedCollections = ()

        if not self.arango.db.hasGraph('GraphTest'):
            self.arango.db.createGraph('GraphTest')

    def test_database_access(self):
        self.assertIsNotNone(self.arango.gdb)

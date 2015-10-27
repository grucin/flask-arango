# Flask-Arango

A Flask extension that provides integration with the Arango graph database.

These capabilities are made possible by the library:
[pyArango](http://pyarango.tariqdaouda.com/)


# Installation

Using pip:

```
    pip install flask-arango
```


# Usage

Typical usage looks like this::

```
    from flask import Flask

    from flask_arango import Arango

    # Configuration
    ARANGO_URL = 'http://localhot:8529'
    ARANGO_DB = 'flask'
    ARANGO_GRAPH = 'my_graph'

    app = Flask(__name__)
    app.config.from_object(__name__)
    arango = Arango(app)
    arango.gdb.createVertex('MyCollection', {'name': 'my document'})
    print arango.db.AQLQuery(
        """
        FOR doc in MyCollection
            RETURN doc
        """,
        batchSize=1
        )
```

# Links

* [pyArango documentation](http://pyarango.tariqdaouda.com/)

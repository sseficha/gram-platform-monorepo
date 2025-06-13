# this is done so that the models are preloaded when their types are referenced. For example the
# batch model references the process model in its relationships and vice versa.
from .batch import BatchModel  # noqa: F401
from .process import ProcessModel  # noqa: F401

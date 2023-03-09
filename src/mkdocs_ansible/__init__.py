"""mkdocs-ansible theme."""
try:
    from ._version import version as __version__
except ImportError:  # pragma: no cover
    __version__ = "0.1.dev1"

__all__ = ("__version__",)

"""mkdocs-ansible theme."""

from __future__ import annotations

try:
    from ._version import version as __version__  # type: ignore

except ImportError:  # pragma: no cover
    __version__ = "0.1.dev1"
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mkdocs_macros.plugin import MacrosPlugin

__all__ = ("__version__",)


def install_from_adt(name: str) -> str:
    """install_from_adt macro."""
    result = f"""!!! Recommendation

    The **recommended** approach to install `{name}` is using the
    `ansible-dev-tools` package.
    [Ansible Development Tools](https://ansible.readthedocs.io/projects/dev-tools/)
    aims to streamline the setup and usage of several tools needed in order to
    create [Ansible](https://www.ansible.com) content. It combines critical Ansible
    development packages into a unified Python package.

    ```bash
    # This also installs ansible-core if it is not already installed
    pip3 install ansible-dev-tools
    ```
    """
    return result


def define_env(env: MacrosPlugin) -> None:
    """Declare environment for jinja2 templates for markdown."""
    for fn in [install_from_adt]:
        env.macro(fn)

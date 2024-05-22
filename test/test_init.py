"""Tests."""

import mkdocs_ansible


def test_install_from_adt() -> None:
    """Tests presence of the macro."""
    assert callable(mkdocs_ansible.install_from_adt)
    result = mkdocs_ansible.install_from_adt("foo")
    assert isinstance(result, str)

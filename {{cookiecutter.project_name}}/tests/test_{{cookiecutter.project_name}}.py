import pytest


class Test{{ cookiecutter.project_name |capitalize }}():
    """Tests for `{{ cookiecutter.project_name }}` module."""

    def test_one(self):
        assert True


@pytest.mark.integrations
def test_two():
    assert True

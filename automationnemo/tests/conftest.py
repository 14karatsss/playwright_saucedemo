import pytest


@pytest.fixture()
def set_up_tear_down(page) -> None:
   # page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto("https://www.saucedemo.com")
    yield page

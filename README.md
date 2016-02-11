# Perform Base Library

If you encounter any problem with Perform Base please visit:

* [Troubleshooting](https://confluence.performgroup.com/display/PZ/Troubleshooting)
* [How to report a bug](https://confluence.performgroup.com/display/PZ/How+to+report+a+bug)

## PEP Compliance

This projects attempts to comply with PEP8. If you notice compliance oversights, please send a patch via pull request.

## Installation

via pip

```bash
pip install git+ssh://git@stash.performgroup.com/p0/performbase.git#egg=performbase
```

## Usage example

### As setUpClass and tearDownClass with PageObject initialization in one place
```python
from performbase import BaseTestCase


class TestCases(BaseTestCase):
    browser_type = "Chrome"
    url = "http://www.google.com"

    @classmethod
    def pageObjectInit(cls):
        #Initialize all your Page Objects here
        pass

    def test_open_sample_webpage(self):
        self.driver.navigate(self.url)
        assert self.driver.title() == "Google"
```

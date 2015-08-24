# Perform Base Library

If you encounter any problem with Perform Base please visit:

* [Troubleshooting](https://confluence.performgroup.com/display/PZ/Troubleshooting)
* [How to report a bug](https://confluence.performgroup.com/display/PZ/How+to+report+a+bug)

## PEP Compliance

This projects attempts to comply with PEP8. If you notice compliance oversights, please send a patch via pull request.

## Installation

via pip

```bash
pip install git+ssh://git@stash.performgroup.com/qa/performbase.git#egg=performbase
```

## Usage example

### As setUpClass and tearDownClass
```python
from performbase import BaseTestCase


class TestCases(BaseTestCase):
    browser_type = "Chrome"
    url = "http://www.google.com"

    def test_open_sample_webpage(self):
        self.driver.navigate(self.url)
        assert self.driver.title() == "Google"
```
### Get article content from Perform Feeds

```python
from performbase import PfFieldsBuilder
from performbase import PfFilterBuilder
from performbase import PfQueryBuilder
# Perform Feeds related data
PF_DOMAIN = "goalyorkshire-article"
PF_OUTLETKEY = "dk8a1orhjncy1rpirnm9ni6pb"


def fetch_article_content():
    pf_fields_builder = PfFieldsBuilder()
    pf_filter_builder = PfFilterBuilder()
    pf_query_builder = PfQueryBuilder()
    fields = pf_fields_builder.\
        add_field("hl").\
        add_field("tsr").\
        add_field("bd").\
        build()
    filters = pf_filter_builder.\
        filter_by_article_type_id("default").\
        build()
    response = pf_query_builder.fetch_article_list(domain=PF_DOMAIN, outletkey=PF_OUTLETKEY,
                                             fields=fields, filters=filters)
    article = response["articles"][0]
    return article["headline"], article["teaser"], article["body"]
```
### Get matches from Sports Data API
```python
from performbase import SportsDataQueryBuilder
# Sports Data related data
SD_OUTLETKEY = "auth1p1"
TMCAL_UUID = "36v49e365gj6415jilkram7dh"


def fetch_n_matches_description(n):
    response = SportsDataQueryBuilder.fetch_team_calendar(SD_OUTLETKEY, TMCAL_UUID)
    match_info = response["match"]
    matches = list()
    for i in range(0, n):
        matches.append(match_info[i]['matchInfo']['description'])
    return matches
```

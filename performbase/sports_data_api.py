import requests


class SportsDataQueryBuilder(object):
    @staticmethod
    def fetch_team_calendar(outletkey, calendar_uuid):
        url = "http://api.performfeeds.com/soccerdata/match/{}?tmcl={}&_fmt=json".format(outletkey, calendar_uuid)
        return requests.get(url).json()

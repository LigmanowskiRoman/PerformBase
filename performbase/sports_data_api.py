class SportsDataQueryBuilder(object):
    @staticmethod
    def build_team_calendar_url(outletkey, calendar_uuid):
        return "http://api.performfeeds.com/soccerdata/match/{}?tmcl={}&_fmt=json".format(outletkey, calendar_uuid)

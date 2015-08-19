class PfHelper(object):
    @staticmethod
    def append_filter(name, value):
        return '%s=%s' % (name, value)


class PfFieldsBuilder(object):

    def __init__(self):
        self.fields = []

    def add_field(self, field):
        self.fields.append(field)
        return self

    def build(self):
        return "&_fld=" + ",".join(self.fields)


class PfFilterBuilder(PfHelper):

    def __init__(self):
        self.filters = []
        self.uuid_filter = ""

    def filter_by_category(self, category):
        self.filters.append(self.append_filter('ctg', category))
        return self

    def filter_by_category_id(self, category_id):
        self.filters.append(self.append_filter('ctgId', category_id))
        return self

    def filter_by_keyword(self, keyword):
        self.filters.append(self.append_filter('kwd', keyword))
        return self

    def filter_by_article_type_id(self, type_id):
        self.filters.append(self.append_filter('atId', type_id))
        return self

    def filter_by_uuid(self, uuid):
        self.uuid_filter = uuid
        return self

    def filter_with_images(self):
        self.filters.append(self.append_filter('lnk', 'urn:perform:image'))
        return self

    def build(self):
        if self.filters:
            return "&" + "&".join(self.filters)
        if self.uuid_filter:
            return "/" + self.uuid_filter


class PfQueryBuilder(object):

    @staticmethod
    def build_article_url(domain, outletkey, uuid='', fields='', filters=''):
        return "http://{}.performfeeds.com/article/{}{}?_fmt=json&_rt=b{}{}".format(domain, outletkey,
                                                                                    uuid, fields, filters)

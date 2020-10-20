class Auction:

    def __init__(self, title, description, startBid, bid, bidders = 0):
        self.title = title
        self.description = description
        self.startBid = startBid
        self.bid = bid
        self.bidders = bidders
        self.details = {}

    def __repr__(self):
        str_val = "Name: {}, description: {}".format(self.name, self.description)
        return str_val

    def add_detail(self, spec, value):
        self.details[spec] = value

    def del_detail(self, spec):
        del self.details[spec]

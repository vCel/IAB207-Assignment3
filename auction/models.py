class Auction:

    def __init__(self, title, description, startBid, bid, bidders = 0, status = "Open"):
        self.title = title
        self.description = description
        self.startBid = startBid
        self.bid = bid
        self.bidders = bidders
        self.status = status
        self.details = {}
        self.images = list()

    def __repr__(self):
        str_val = "Name: {}, description: {}".format(self.name, self.description)
        return str_val

    def add_detail(self, spec, value):
        self.details[spec] = value

    def del_detail(self, spec):
        del self.details[spec]

    def add_image(self, file):
        self.images.append(file)

    def del_image(self, pos):
        del self.images[pos]


class Review:

    def __init__(self, user, comment, rating):
        self.user = user
        self.comment = comment
        self.rating = rating

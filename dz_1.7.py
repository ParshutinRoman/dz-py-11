

class farm_unit(object):
	feed = 0 # kg
	weight = 0 # kg
	fertility = 0 # units/year
	product = meat
	price_alive = 0 # bitcoins
	price_dead = 0 # bitcoins

	def to_feed(self, value):
		self.feed +=value

	def to_kill(self, weight):
		self.price_dead *=weight

	def to_sell(self, weight):
		self.price_alive *=weight * 0.1

class fourlegs_unit(farm_unit):
	sub_product = horn

class twowings_unit(farm_unit):
	sub_product = (egg, feather)


class cow(fourlegs_unit):
	bonus_product = (milk, skin)


class sheep(fourlegs_unit):
	bonus_product = (fur)


class pig(fourlegs_unit):
	bonus_product = (fat)


class goat(fourlegs_unit):
	bonus_product = (milk)



class duck(twowings_unit):


class chicken(twowings_unit):


class goose(twowings_unit):






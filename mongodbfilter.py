def init():
	app_dict = {}
	mongodbDefault = []
	mongodbSensitive = []
	mongodbDealingFunc = []
	app_dict["default"] = mongodbDefault
	app_dict["sensitive"] = mongodbSensitive
	app_dict["dealingFunc"] = mongodbDealingFunc
	return app_dict

def init():
	app_dict = {}
	sparkDefault = ["spark.blockManager.port", "spark.driver.blockManager.port", "spark.ssl.enabled",
					"spark.ssl.[namespace].port",
					"spark.ssl.enabledAlgorithms", "spark.ssl.needClientAuth"]
	sparkSensitive = ["","","spark.ssl.trustStore", "spark.ssl.trustStorePassword"]
	sparkDealingFunc = []
	app_dict["default"] = sparkDefault
	app_dict["sensitive"] = sparkSensitive
	app_dict["dealingFunc"] = sparkDealingFunc
	return app_dict

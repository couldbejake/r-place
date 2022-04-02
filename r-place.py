from selenium import webdriver

import api.bearer_api as ba
import api.place_api as pa

BearerAPI = ba.Bearer()
PlaceAPI = pa.Place()

api_token = BearerAPI.fetch_token("<USERNAME>", "<PASSWORD>")
result = PlaceAPI.place_tile(0, 999, 2, api_token)

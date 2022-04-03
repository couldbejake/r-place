import api.bearer_api as ba
import api.place_api as pa

BearerAPI = ba.Bearer()
PlaceAPI = pa.Place()

#get the Bearer token
api_token = BearerAPI.fetch_token("<USERNAME>", "<PASSWORD>")

#place a tile at x:0 y:999 with the color 2(bright red) see place_api.py inside of the api folder.
result = PlaceAPI.place_tile(0, 999, 2, api_token)

#get the person who cnaged a certain pixel at x:0 y:999.
person_change_pixel = PlaceAPI.get_pixel_user(0,999,api_token)

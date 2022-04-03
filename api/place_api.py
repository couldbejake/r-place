import requests
class Place:
    def place_tile(self, x, y, col, bearer):
        url = "https://gql-realtime-2.reddit.com/query"

        if y>1000:
            raise ValueError ("Y value needs to be less than 1000")
        canvas_index = 0
        if x>1000:
            canvas_index = 1
            x = x-1000
        color_map = {
            "#FF4500": 2,  # bright red
            "#FFA800": 3,  # orange
            "#FFD635": 4,  # yellow
            "#00A368": 6,  # darker green
            "#7EED56": 8,  # lighter green
            "#2450A4": 12,  # darkest blue
            "#3690EA": 13,  # medium normal blue
            "#51E9F4": 14,  # cyan
            "#811E9F": 18,  # darkest purple
            "#B44AC0": 19,  # normal purple
            "#FF99AA": 23,  # pink
            "#9C6926": 25,  # brown
            "#000000": 27,  # black
            "#898D90": 29,  # grey
            "#D4D7D9": 30,  # light grey
            "#FFFFFF": 31,  # white
        }

        payload="{\"operationName\":\"setPixel\",\"variables\":{\"input\":{\"actionName\":\"r/replace:set_pixel\",\"PixelMessageData\":{\"coordinate\":{\"x\":" + str(x) + ",\"y\":" + str(y) + "},\"colorIndex\":" + str(col) + ",\"canvasIndex\":"+str(canvas_index)+"}}},\"query\":\"mutation setPixel($input: ActInput!) {\\n  act(input: $input) {\\n    data {\\n      ... on BasicMessage {\\n        id\\n        data {\\n          ... on GetUserCooldownResponseMessageData {\\n            nextAvailablePixelTimestamp\\n            __typename\\n          }\\n          ... on SetPixelResponseMessageData {\\n            timestamp\\n            __typename\\n          }\\n          __typename\\n        }\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\"}"
        headers = {
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'apollographql-client-name': 'mona-lisa',
        'sec-ch-ua-mobile': '?0',
        'authorization': 'Bearer ' + str(bearer),
        'content-type': 'application/json',
        'accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
        'apollographql-client-version': '0.0.1',
        'sec-ch-ua-platform': '"macOS"',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return (response.text)
    
    def get_pixel_user(self,x,y,bearer):
        url = "https://gql-realtime-2.reddit.com/query"
        canvas_index = 0
        if y>1000:
            raise ValueError ("Y value needs to be less than 1000")

        if x>1000:
            canvas_index = 1
            x = x-1000
        payload="{\"operationName\":\"pixelHistory\",\"variables\":{\"input\":{\"actionName\":\"r/replace:get_tile_history\",\"PixelMessageData\":{\"coordinate\":{\"x\":" + str(x) + ",\"y\":" + str(y) + "},\"colorIndex\":0,\"canvasIndex\":"+str(canvas_index)+"}}},\"query\":\"mutation pixelHistory($input: ActInput!) {\\n  act(input: $input) {\\n    data {\\n      ... on BasicMessage {\\n        id\\n        data {\\n          ... on GetTileHistoryResponseMessageData {\\n            lastModifiedTimestamp\\n            userInfo {\\n              userID\\n              username\\n              __typename\\n            }\\n            __typename\\n          }\\n          __typename\\n        }\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\"}"
        headers = {
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'apollographql-client-name': 'mona-lisa',
        'sec-ch-ua-mobile': '?0',
        'authorization': 'Bearer ' + str(bearer),
        'content-type': 'application/json',
        'accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
        'apollographql-client-version': '0.0.1',
        'sec-ch-ua-platform': '"macOS"',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty'
        }
        json_res = requests.request("POST", url, headers=headers, data=payload).json()
        return json_res["data"]["act"]["data"][0]["data"]["userInfo"]["username"]

        

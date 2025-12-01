import unittest
import dg_sdk
import json
from demo.demo_config import *



def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    return extend_infos


class TestV2TradeCardbinQueryRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 卡bin信息查询 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradeCardbinQueryRequest()
        request.req_date = ""
        request.req_seq_id = ""
        request.bank_card_no_crypt = "VDFveDULoK6qhWuN34P8XF7tuZow4eg74zEPKjNVwSjQTW572jqmYjpRDbEtX0f56hMQUfFv5wFRjvDIY+yTl+SFKgBmoNlPDm9B3mDjOa8er5FEnI5QWgvyuqSxHWJf2eIjU7OHt3q3/0ZsbetNzIAiaAZdicn9Sawsr9yZ8ZOdBmhIPO5tqJyDkoKO5Tpj0VyZMJ5ugSDx/2XGSmX3dHQ1JKlZ/7rovB+WchA9BzZQzSTcvmmdV6mzuyTPWRzxfhyVPAVLzh5XhKyl6SMKmzOM1zSNMPtzDhTaUG4XLSM5A0+Tqt3O4tSi16f5zn2csgwbN6TMd5jrXNzC8UTpdQ=="

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
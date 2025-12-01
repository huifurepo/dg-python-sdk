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
    # 微信开通数
    extend_infos["wx_open_count"] = "0"
    # 支付宝开通数
    extend_infos["ali_open_count"] = "1"
    # 异步通知地址
    extend_infos["async_url"] = "http://service.example.com/to/path"
    return extend_infos


class TestV2MerchantAtpreventApplyRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 防断链入驻 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2MerchantAtpreventApplyRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000108460751"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
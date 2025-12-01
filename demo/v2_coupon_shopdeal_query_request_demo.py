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
    # 操作人
    extend_infos["operator_id"] = ""
    return extend_infos


class TestV2CouponShopdealQueryRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 美团非餐饮获取团购信息 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2CouponShopdealQueryRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000106057033"
        request.bind_id = "b924ef97a4c14bbe88c72794fa4ce505"
        request.offset = "1"
        request.limit = "100"
        request.source = "2"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
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
    # 机具id
    # extend_infos["device_id"] = ""
    # 操作人id
    # extend_infos["operator_id"] = ""
    # 操作人姓名
    # extend_infos["operator_name"] = ""
    return extend_infos


class TestV2CouponMeituanCancelRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 美团卡券撤销 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2CouponMeituanCancelRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000106057033"
        request.bind_id = "9c2d91f68ba045a998df46ffe395a9ca"
        request.app_shop_account = "123"
        request.app_shop_account_name = "12345"
        request.receipt_code = "5729740654"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
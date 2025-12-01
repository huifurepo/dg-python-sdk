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


class TestV2TradeOnlinepaymentQueryRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 线上交易查询 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradeOnlinepaymentQueryRequest()
        request.huifu_id = "6666000109133323"
        request.org_req_date = "20240401"
        request.org_hf_seq_id = "00600000000240401100725P864ac13645d00000"
        request.org_req_seq_id = "295700155481522176"
        request.pay_type = "QUICK_PAY"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
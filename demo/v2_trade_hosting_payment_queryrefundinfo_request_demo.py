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


class TestV2TradeHostingPaymentQueryrefundinfoRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 托管交易退款查询 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradeHostingPaymentQueryrefundinfoRequest()
        request.req_date = ""
        request.req_seq_id = ""
        request.huifu_id = "6666000003100616"
        request.org_req_date = "20240229"
        request.org_hf_seq_id = ""
        request.org_req_seq_id = "52022070919803411999411514"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
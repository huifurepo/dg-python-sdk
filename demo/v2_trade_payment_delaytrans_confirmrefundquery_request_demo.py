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


class TestV2TradePaymentDelaytransConfirmrefundqueryRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 交易确认退款查询 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradePaymentDelaytransConfirmrefundqueryRequest()
        request.huifu_id = "6666000109133323"
        request.org_req_date = "20240426"
        request.org_req_seq_id = "20211714122436"
        request.org_hf_seq_id = "003100TOP1A240513112100P256ac139cc000000"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
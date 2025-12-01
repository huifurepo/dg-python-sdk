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
    # 交易时间
    # extend_infos["trans_time"] = ""
    # 异步通知地址
    extend_infos["notify_url"] = "https://mock.uutool.cn/fat69kri74k"
    return extend_infos


class TestV2TradePaymentZxeUnknownincomeDisposeRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 不明来账处理 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradePaymentZxeUnknownincomeDisposeRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000109133323"
        request.bank_serial_no = "FRSC202409252NEA000121452600000"
        request.pay_acct = "test"
        request.pay_acct_name = "test"
        request.trans_amt = "test"
        request.trans_date = "test"
        request.operate_type = "0"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
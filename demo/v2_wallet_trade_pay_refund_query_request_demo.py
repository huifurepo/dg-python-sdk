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
    # 钱包用户id
    extend_infos["user_huifu_id"] = "6666000136655020"
    # 原退款交易全局流水号
    extend_infos["org_hf_seq_id"] = "003100TOP1A230816150903P990ac139c0600000"
    return extend_infos


class TestV2WalletTradePayRefundQueryRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 钱包支付退款查询 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2WalletTradePayRefundQueryRequest()
        request.org_req_date = "20230816"
        request.org_req_seq_id = "test"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
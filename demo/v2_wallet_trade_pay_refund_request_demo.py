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
    # 原交易请求流水号
    # extend_infos["org_req_seq_id"] = ""
    # 原交易全局流水号
    # extend_infos["org_hf_seq_id"] = ""
    # 备注
    extend_infos["remark"] = "remark11"
    # 商户扩展信息
    # extend_infos["mer_priv"] = ""
    return extend_infos


class TestV2WalletTradePayRefundRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 钱包支付退款 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2WalletTradePayRefundRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000135653240"
        request.user_huifu_id = "6666000136655020"
        request.trans_amt = "0.02"
        request.org_req_date = "test"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
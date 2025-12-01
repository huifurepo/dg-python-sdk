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
    # 出款方账户
    extend_infos["acct_id"] = "F00598600"
    # 转账描述
    extend_infos["description"] = "用户补贴"
    # 备注
    extend_infos["remark"] = "备注"
    return extend_infos


class TestV2WalletTradeRechargeTransferRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 用户补贴 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2WalletTradeRechargeTransferRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000107309462"
        request.user_huifu_id = "6666000187364826"
        request.trans_amt = "0.01"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
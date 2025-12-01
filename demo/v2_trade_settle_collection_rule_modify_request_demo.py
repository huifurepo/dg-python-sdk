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
    # 转出方账户留存金额
    extend_infos["remained_amt"] = "0.00"
    # 是否关闭
    extend_infos["close"] = ""
    return extend_infos


class TestV2TradeSettleCollectionRuleModifyRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 修改归集配置 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradeSettleCollectionRuleModifyRequest()
        request.req_date = ""
        request.req_seq_id = ""
        request.out_huifu_id = "6666000152758213"
        request.out_acct_id = "F03142591"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
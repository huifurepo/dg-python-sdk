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
    # 原请求流水号
    extend_infos["org_req_seq_id"] = "2021091708126665001"
    # 原请求日期
    extend_infos["org_req_date"] = "20231215"
    # 实际付款方银行卡号
    # extend_infos["bank_card_no"] = ""
    # 实际付款方姓名
    extend_infos["certificate_name"] = "沈显龙"
    # 实际付款日期
    # extend_infos["trans_date"] = ""
    # 交易金额
    # extend_infos["trans_amt"] = ""
    # 收款方账号
    # extend_infos["payee_acct_no"] = ""
    return extend_infos


class TestV2TradeOnlinepaymentTransferBankblotterQueryRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 银行大额未入账流水列表查询 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradeOnlinepaymentTransferBankblotterQueryRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000003100615"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
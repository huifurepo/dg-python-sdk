import unittest
import dg_sdk
import json
from demo.demo_config import *


def get5ff7863bFba14fd185823535ee0a9e52():
    dto = dict()
    # 分账明细
    dto["acct_info"] = get875acdbcEff4424dBa4551dffa06d840()

    return json.dumps(dto)

def get875acdbcEff4424dBa4551dffa06d840():
    dto = dict()
    # 分账金额
    dto["div_amt"] = "20.00"
    # 分账接收方ID
    dto["huifu_id"] = "6666000108898793"
    # 账户号
    dto["acct_id"] = "C03113649"

    return dto;


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 出款方账户号
    extend_infos["out_acct_id"] = "C03117654"
    # 备注
    extend_infos["remark"] = ""
    return extend_infos


class TestV2FlexibleTradeRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 灵工支付 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2FlexibleTradeRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.out_huifu_id = "6666000108903745"
        request.stage_operation_type = "FIRST_STAGE"
        request.phase_hf_seq_id = ""
        request.ord_amt = "20"
        request.acct_split_bunch = get5ff7863bFba14fd185823535ee0a9e52()

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
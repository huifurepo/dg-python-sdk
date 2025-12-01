import unittest
import dg_sdk
import json
from demo.demo_config import *


def getF7787e9670d544d18daf492c5188d4b8():
    dto = dict()
    # 百分比分账标志
    # dto["percentage_flag"] = ""
    # 是否净值分账
    # dto["is_clean_split"] = ""
    # 分账明细
    # dto["acct_infos"] = get78d9342b81254eae998c1de697882410()

    return json.dumps(dto)

def get78d9342b81254eae998c1de697882410():
    dto = dict()
    # 分账金额
    # dto["div_amt"] = "test"
    # 分账接收方商户号
    # dto["huifu_id"] = "test"
    # 分账接收方账户号
    # dto["acct_id"] = ""

    dtoList = [dto]
    return dtoList


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 分账串
    # extend_infos["acct_split_bunch"] = getF7787e9670d544d18daf492c5188d4b8()
    # 原请求流水号
    extend_infos["org_req_seq_id"] = "20241010test10000111qccrr"
    # 原全局流水号
    # extend_infos["org_hf_seq_id"] = ""
    # 交易备注
    # extend_infos["remark"] = ""
    # 异步通知地址
    # extend_infos["notify_url"] = ""
    return extend_infos


class TestV2TradePayafteruseInstallmentRefundRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 分期交易退款 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradePayafteruseInstallmentRefundRequest()
        request.req_date = ""
        request.req_seq_id = ""
        request.huifu_id = "6666000108281250"
        request.ord_amt = "0.01"
        request.org_req_date = "20241010"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
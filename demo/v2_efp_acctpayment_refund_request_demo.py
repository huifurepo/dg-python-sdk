import unittest
import dg_sdk
import json
from demo.demo_config import *


def get5bf3321f6c604d67Ad10C58a4cce226c():
    dto = dict()
    # 退账明细
    dto["acct_infos"] = getE1cff61a45374e07B6a5Fd58a85a8f13()

    return json.dumps(dto)

def getE1cff61a45374e07B6a5Fd58a85a8f13():
    dto = dict()
    # 退款金额
    dto["div_amt"] = "1.00"
    # 退款方ID
    dto["huifu_id"] = "6666000123123123"
    # 退款方账户号
    dto["acct_id"] = "F00598600"

    dtoList = [dto]
    return dtoList


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 备注
    extend_infos["remark"] = "备注"
    return extend_infos


class TestV2EfpAcctpaymentRefundRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 全渠道资金付款到账户退款 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2EfpAcctpaymentRefundRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000123123123"
        request.org_hf_seq_id = "00470topo1A211015160805P090ac132fef00000"
        request.org_req_seq_id = "2021091708126665002"
        request.org_req_date = "20221022"
        request.refund_amt = "10.00"
        request.acct_split_bunch = get5bf3321f6c604d67Ad10C58a4cce226c()

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
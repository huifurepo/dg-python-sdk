import unittest
import dg_sdk
import json
from demo.demo_config import *


def get506673b064014081830918c73b5747ba():
    dto = dict()
    # 转账原因
    dto["transfer_type"] = "04"
    # 产品子类
    dto["sub_product"] = "卡券推广类"

    return json.dumps(dto)

def get9128befdE59846c78e5b5db4cb062ef2():
    dto = dict()
    # 退账明细
    # dto["acct_infos"] = get26f8ea3aF58d4562894b3b3360aa8987()

    return json.dumps(dto)

def get26f8ea3aF58d4562894b3b3360aa8987():
    dto = dict()
    # 退款金额
    # dto["div_amt"] = "test"
    # 退款方ID
    # dto["huifu_id"] = "test"

    dtoList = [dto]
    return dtoList


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 分账对象
    # extend_infos["acct_split_bunch"] = get9128befdE59846c78e5b5db4cb062ef2()
    # 安全信息
    extend_infos["risk_check_data"] = get506673b064014081830918c73b5747ba()
    # 备注
    extend_infos["remark"] = "1234567890"
    return extend_infos


class TestV2TradeAcctpaymentRefundRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 余额支付退款 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradeAcctpaymentRefundRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000109133323"
        request.org_req_date = "20240515"
        request.org_req_seq_id = "20240515132857954fk8wpk2hvwnnfw"
        request.org_hf_seq_id = ""
        request.ord_amt = "0.01"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
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
    # 备注
    extend_infos["remark"] = "remark"
    # 异步通知地址
    extend_infos["notify_url"] = ""
    return extend_infos


class TestV2BillEntRefundRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 企业账单退款 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2BillEntRefundRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000003100615"
        request.bill_no = "ZD2024082486318420"
        request.refund_amt = "0.01"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
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
    return extend_infos


class TestV2InvoiceResendmailRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 发票邮件重发接口 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2InvoiceResendmailRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000107430944"
        request.ivc_number = "25317000000132667193"
        request.mail_addr = "[\"pengbo.Jiang_c@huifu.com\",\"pengbo.Jiang2_c@huifu.com\"]"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
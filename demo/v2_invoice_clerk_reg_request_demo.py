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
    # 开票员名字
    extend_infos["clerk_name"] = "张三"
    return extend_infos


class TestV2InvoiceClerkRegRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 开票员登记 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2InvoiceClerkRegRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000149801800"
        request.clerk_identity = "04"
        request.login_account = "31011520010"
        request.login_password = "1******5"
        request.clerk_phone_no = "17621100776"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
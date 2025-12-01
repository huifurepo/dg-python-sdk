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
    # 变更原因
    extend_infos["remark"] = "测试"
    return extend_infos


class TestV2BillEntChangestatRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 企业账单状态变更 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2BillEntChangestatRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "test"
        request.bill_no = "ZD2024082686348233"
        request.bill_stat = "test"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
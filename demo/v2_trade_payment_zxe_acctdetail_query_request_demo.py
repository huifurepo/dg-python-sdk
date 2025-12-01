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
    # 登记薄类型
    # extend_infos["register_type"] = ""
    # 页码
    extend_infos["page_num"] = "1"
    return extend_infos


class TestV2TradePaymentZxeAcctdetailQueryRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # E账户账务明细查询 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradePaymentZxeAcctdetailQueryRequest()
        request.req_date = ""
        request.req_seq_id = ""
        request.huifu_id = "6666000107941250"
        request.trans_date = "20231227"
        request.trans_type = "03"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
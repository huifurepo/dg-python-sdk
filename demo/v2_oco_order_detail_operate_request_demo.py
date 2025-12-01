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
    # 分账接收方编号
    # extend_infos["in_huifu_id"] = ""
    return extend_infos


class TestV2OcoOrderDetailOperateRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 全渠道订单分账明细操作 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2OcoOrderDetailOperateRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "test"
        request.busi_source = "test"
        request.oco_order_id = "test"
        request.operate_type = "test"
        request.pay_type = "test"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
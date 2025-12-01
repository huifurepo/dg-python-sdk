import unittest
import dg_sdk
import json
from demo.demo_config import *


def getA4340f0d9f434de0910eC4522943e67d():
    dto = dict()
    # 入账方商户号
    dto["in_huifu_id"] = "6666000104558835"
    # 操作类型
    dto["apply_type"] = "ADD"

    dtoList = [dto]
    return json.dumps(dtoList)


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    return extend_infos


class TestV2TradePayrelationApplyRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 付款关系提交 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradePayrelationApplyRequest()
        request.out_huifu_id = "6666000105253412"
        request.req_date = ""
        request.req_seq_id = ""
        request.pay_relations = getA4340f0d9f434de0910eC4522943e67d()

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
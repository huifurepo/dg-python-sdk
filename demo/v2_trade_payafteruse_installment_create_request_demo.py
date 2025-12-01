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
    # 原请求流水号
    extend_infos["org_req_seq_id"] = "20241010test10000111111q"
    # 原请求日期
    extend_infos["org_req_date"] = "20241010"
    # 原全局流水号
    extend_infos["org_hf_seq_id"] = "0056default241010164346P593c0a831b900000"
    # 期数
    extend_infos["fq_num"] = "1"
    return extend_infos


class TestV2TradePayafteruseInstallmentCreateRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 分期单创建 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradePayafteruseInstallmentCreateRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000108281250"
        request.fq_amt = "0.01"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
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
    # 合作平台
    # extend_infos["lg_platform_type"] = ""
    return extend_infos


class TestV2HycInvcategoryQueryRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 开票类目查询 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2HycInvcategoryQueryRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.minor_agent_id = "L20210316173416881"
        request.huifu_id = "test"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
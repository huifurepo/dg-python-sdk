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
    # 开始时间
    extend_infos["start_date"] = "20240112"
    # 结束时间
    extend_infos["end_date"] = "20240112"
    # 合作平台
    # extend_infos["lg_platform_type"] = ""
    return extend_infos


class TestV2HycMersignQueryRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 商户签约查询 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2HycMersignQueryRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000144060581"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
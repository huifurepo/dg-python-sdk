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
    # 分页页码
    extend_infos["page_num"] = "1"
    return extend_infos


class TestV2MerchantAppealRelatedclueQueryRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 关联线索查询 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2MerchantAppealRelatedclueQueryRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.page_size = "20"
        request.assist_id = "202407011807686403687215104"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
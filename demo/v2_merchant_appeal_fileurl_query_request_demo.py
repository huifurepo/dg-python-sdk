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


class TestV2MerchantAppealFileurlQueryRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 申诉文件url查询 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2MerchantAppealFileurlQueryRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.file_id = "66b2d1de-2f18-3103-86c3-3b9a69b03d6"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
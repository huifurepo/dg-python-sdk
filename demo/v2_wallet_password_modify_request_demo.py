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
    # 请求失效时间
    extend_infos["time_expired"] = ""
    return extend_infos


class TestV2WalletPasswordModifyRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 钱包密码修改 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2WalletPasswordModifyRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000107309462"
        request.user_huifu_id = "6666000107355468"
        request.verify_no = "011363"
        request.verify_seq_id = "WALLET0000000054024907"
        request.front_url = "https://www.huifu.com/products-services/"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
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
    # 抖音团购券码
    extend_infos["coupon_code"] = "5729740654"
    # 从二维码解析出来的标识（传参前需要先进行URL编码，注意不要有空格)
    # extend_infos["encrypted_data"] = ""
    return extend_infos


class TestV2CouponDouyinPrepareRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 抖音卡券校验 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2CouponDouyinPrepareRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000107767088"
        request.bind_id = "88fd7c9b63e84a259dfe3eecb811fce8"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
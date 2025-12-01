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
    # 机具id
    # extend_infos["device_id"] = ""
    # 操作人id
    # extend_infos["operator_id"] = ""
    # 操作人姓名
    # extend_infos["operator_name"] = ""
    # 取消核销总次数
    # extend_infos["times_card_cancel_count"] = ""
    # 撤销核销幂等
    # extend_infos["cancel_token"] = ""
    return extend_infos


class TestV2CouponDouyinCancelRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 抖音卡券撤销 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2CouponDouyinCancelRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000107767088"
        request.bind_id = "88fd7c9b63e84a259dfe3eecb811fce8"
        request.encrypted_code = "5584192259"
        request.verify_id = "3435"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
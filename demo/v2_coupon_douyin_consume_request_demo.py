import unittest
import dg_sdk
import json
from demo.demo_config import *


def get014d6e414b0943a3A679383914e2bb49():
    dto = dict()
    # 开台时间（秒）
    # dto["biz_time"] = "test"
    # 实际抵扣金额（分））
    # dto["actual_deduction_amount"] = "test"

    return dto;


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
    # 核销额外参数
    # extend_infos["verify_extra"] = get014d6e414b0943a3A679383914e2bb49()
    return extend_infos


class TestV2CouponDouyinConsumeRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 抖音卡券核销 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2CouponDouyinConsumeRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000107767088"
        request.bind_id = "88fd7c9b63e84a259dfe3eecb811fce8"
        request.encrypted_codes = "[\"2343\",\"5462\"]"
        request.verify_token = "EfdAdS3"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
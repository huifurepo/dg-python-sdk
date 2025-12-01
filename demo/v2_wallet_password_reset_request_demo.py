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
    # 个人证件号码
    # extend_infos["cert_no"] = ""
    # 银行卡号
    extend_infos["card_no"] = ""
    # 银行卡绑定手机号
    # extend_infos["card_mobile"] = ""
    return extend_infos


class TestV2WalletPasswordResetRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 钱包密码重置 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2WalletPasswordResetRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000107309462"
        request.user_huifu_id = "6666000107355468"
        request.cust_mobile = "13771817106"
        request.verify_no = "652364"
        request.verify_seq_id = "WALLET0000000054024907"
        request.front_url = ""

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
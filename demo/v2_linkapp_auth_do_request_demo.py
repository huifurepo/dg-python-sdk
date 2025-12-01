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
    # 回调地址
    # extend_infos["callback_url"] = ""
    # 
    # extend_infos["以下仅RPA授权输入"] = ""
    # 登录账号名称
    # extend_infos["account_name"] = ""
    # 登录账号密码
    # extend_infos["account_password"] = ""
    # 门店名称
    # extend_infos["shop_name"] = ""
    # 管理员手机号
    # extend_infos["admin_phone_num"] = ""
    return extend_infos


class TestV2LinkappAuthDoRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 商户公域授权 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2LinkappAuthDoRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000107203801"
        request.platform_type = "21"
        request.contract_url = "https://cloudpnrcdn.oss-cn-shanghai.aliyuncs.com/spin/files/斗拱增值业务服务协议 V1.020231120.docx"
        request.contract_mer_name = "于云飞"
        request.contract_time = "1744008692000"
        request.phone_number = "test"
        request.merchant_type = "test"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
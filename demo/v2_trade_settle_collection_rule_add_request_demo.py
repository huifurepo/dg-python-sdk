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
    # 转入方账户号
    extend_infos["in_acct_id"] = ""
    # 转出方账户号
    extend_infos["out_acct_id"] = ""
    # 转出方账户留存金额
    extend_infos["remained_amt"] = "1.01"
    # 协议类型
    extend_infos["agreement_type"] = "1"
    # 异步消息接收地址
    extend_infos["async_return_url"] = "http://service.testexample.com/to/path"
    return extend_infos


class TestV2TradeSettleCollectionRuleAddRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 新增归集配置 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradeSettleCollectionRuleAddRequest()
        request.req_date = ""
        request.req_seq_id = ""
        request.in_huifu_id = "6666000143571659"
        request.out_huifu_id = "6666000152758213"
        request.sign_user_mobile_no = ""
        request.file_id = "f80a4c17-d7c5-3e31-9e70-daf2bd6be29e"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
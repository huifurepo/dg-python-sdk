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
    # 密码页面类型
    extend_infos["request_type"] = "M"
    # 备注
    extend_infos["remark"] = "remark11"
    return extend_infos


class TestV2WalletTradeWithdrawalRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 钱包提现下单 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2WalletTradeWithdrawalRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000135653240"
        request.user_huifu_id = "6666000136655020"
        request.token_no = "10043478052"
        request.trans_amt = "test"
        request.front_url = "http://www.huifu.com"
        request.notify_url = "https://"
        request.into_acct_date_type = "D0"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
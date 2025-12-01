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
    # 原请求流水号
    extend_infos["efp_req_seq_id"] = "20241128164919defaultit687891821"
    # 原请求日期
    extend_infos["efp_req_date"] = "20241128"
    # 备注
    extend_infos["remark"] = "saas取现"
    # 异步通知地址
    extend_infos["notify_url"] = "http://www.service.com/getresp"
    return extend_infos


class TestV2EfpEncashRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 全渠道资金提现申请 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2EfpEncashRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000108422302"
        request.cash_amt = "0.01"
        request.token_no = "10001933531"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
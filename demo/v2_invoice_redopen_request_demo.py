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
    # 备注
    extend_infos["resv"] = "备注"
    # 开票结果异步通知地址
    extend_infos["callback_url"] = "virgo://http://192.168.85.157:30031/sspm/testVirgo"
    return extend_infos


class TestV2InvoiceRedopenRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 红字发票开具接口 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2InvoiceRedopenRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000107430944"
        request.ori_ivc_number = "25317000000132667193"
        request.red_apply_reason = "02"
        request.red_apply_source = "01"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
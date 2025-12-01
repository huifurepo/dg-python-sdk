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
    # 异步地址
    extend_infos["asyn_url"] = "https://www.baidu.com"
    # 接收人手机号
    extend_infos["receive_mobile"] = "13945641357"
    # 接收人姓名
    extend_infos["receive_name"] = "黄二"
    # 快递地址
    extend_infos["courier_address"] = "长江大街161号上海长江经济园"
    # 购方税号
    extend_infos["invoice_tax_no"] = "91310230MA1JTWAK98"
    # 购方公司名称
    extend_infos["invoice_name"] = "上海汇涵信息科技服务有限公司"
    # 购方公司地址
    extend_infos["invoice_address"] = "长江大街161号上海长江经济园"
    # 购方公司银行账号
    extend_infos["invoice_card_num"] = "631252533"
    # 购方银行名称
    extend_infos["invoice_bank_name"] = "中国民生银行股份有限公司"
    # 购方联系电话
    extend_infos["invoice_phone"] = "400-820-2819"
    # 发票类型
    extend_infos["invoice_type"] = "1"
    # 备注
    extend_infos["remarks"] = ""
    # 合作平台
    # extend_infos["lg_platform_type"] = ""
    return extend_infos


class TestV2HycInvoiceApplyRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 申请开票 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2HycInvoiceApplyRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000109133323"
        request.invoice_category = "信息技术服务*软件测试服务"
        request.hf_seq_ids = "0035000topB250922101351P997c0a8414a00000,0035000topB250922092931P351c0a8414a00000"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
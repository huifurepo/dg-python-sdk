import unittest
import dg_sdk
import json
from demo.demo_config import *


def get864f5a50D5064cea9423A5f3ca9e73a7():
    dto = dict()
    # 商户商品ID
    dto["out_item_id"] = "1234567"
    # 商品名称
    dto["goods_name"] = "快充"
    # 商品数量
    dto["item_cnt"] = "1"
    # 商品单价
    dto["sale_price"] = "0.30"
    # 商品的编号
    dto["goods_id"] = "Ldkc00001"
    # 商品分期信息
    dto["item_installment_info"] = get1efd507a9385411f80f998b1c37876d9()

    dtoList = [dto]
    return json.dumps(dtoList)

def get1efd507a9385411f80f998b1c37876d9():
    dto = dict()
    # 总分期数
    dto["period_num"] = 1
    # 每期最大金额
    dto["period_max_price"] = 0.30
    # 每期金额
    # dto["period_price"] = ""

    return dto;


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 异步通知地址
    extend_infos["notify_url"] = "https://mock.uutool.cn/4pga0jqv8vv0"
    # 追踪ID
    extend_infos["source_id"] = "MjA4ODcwMjY5OTkwODI1N3wyMDIxMDAzMTUwNjM4MTE2fDE3Mjg1NDk3OTU0OTl8ZmFsc2V8VE9LRU5fSVNfTlVMTA=="
    # 支付宝交易号
    extend_infos["trade_no"] = "2024092722001408251414114417"
    # 代扣协议签约场景
    extend_infos["deduct_sign_scene"] = "INDUSTRY|XIANXIANG_BIKE_CHARGE"
    # 芝麻信用外部类⽬
    extend_infos["zm_category_id"] = "credit_pay_for_battery_charging"
    # 是否不需要核身
    # extend_infos["no_need_verify_identity"] = ""
    # 开通成功后跳转地址
    # extend_infos["acceptance_jump_url"] = ""
    return extend_infos


class TestV2TradePayafteruseCreditbizorderCreateRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 服务单创建 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradePayafteruseCreditbizorderCreateRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000108281250"
        request.trans_amt = "0.01"
        request.buyer_id = "2088000000000000"
        request.title = "测试001"
        request.merchant_biz_type = "INDIRECT_CHARGE_WITHHOLD"
        request.path = "https://www.baidu.com/"
        request.zm_service_id = "2024081500001003000081751200"
        request.item_infos = get864f5a50D5064cea9423A5f3ca9e73a7()

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
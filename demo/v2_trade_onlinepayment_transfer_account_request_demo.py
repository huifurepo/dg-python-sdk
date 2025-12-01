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
    # 用户客户号
    extend_infos["user_huifu_id"] = "6666000103905031"
    # 收款方账户号
    extend_infos["acct_id"] = "A01199826"
    # 页面标识
    # extend_infos["page_flag"] = ""
    # 付款方名称
    extend_infos["certificate_name"] = "沈显龙"
    # 付款方银行卡号
    extend_infos["bank_card_no"] = "Xmjm1RB4AAOaFYQ+PgjBlpugXbd8VAYAGB3J2zrbLfC42Bh5xiB47OOV1EdXyGpBq4H8je7mB/MlyEEs6O8PX6aoI4QHumr8VglrLM6uzbVNCIc3S5RPSmi2M+9+EdIQ6nlWd5+XQ7RJXX5Uvnegn74XzQBcN1d4gd04buwKbLpUPV3tWd1qjQwEE8w4gwEtH3L5AP75Mynz+wHFrUKJF3BTiW2/zJlcq5GJomOl06GEW52AZkXwn6U2suP3a0ySd0Rxbf1yQ1lj3SP56NeeEzuBaFLQWB7mEqJfZF3pE9MHNfi6tR1xwLdcxt98bdIqlteKdNAmgfQzcS13UcwH+w=="
    # 订单类型
    # extend_infos["order_type"] = ""
    # 备注
    extend_infos["remark"] = "标记123"
    # 异步通知地址
    extend_infos["notify_url"] = "http://www.huifu.com/getResp"
    # 入账模式
    # extend_infos["acct_mode"] = ""
    # 银行模式
    # extend_infos["bank_mode"] = ""
    # 延时标记
    # extend_infos["delay_acct_flag"] = ""
    # 订单模式
    # extend_infos["order_mode"] = ""
    # 原汇款订单号
    # extend_infos["org_remittance_order_id"] = ""
    # 动态码标识
    # extend_infos["dynamic_flag"] = ""
    # 订单失效时间
    # extend_infos["time_expire"] = ""
    # 手续费扣款标志
    # extend_infos["fee_flag"] = ""
    return extend_infos


class TestV2TradeOnlinepaymentTransferAccountRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 银行大额支付 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradeOnlinepaymentTransferAccountRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000003100616"
        request.trans_amt = "10.00"
        request.goods_desc = "商品描述001"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
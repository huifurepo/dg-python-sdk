import unittest
import dg_sdk
import json
from demo.demo_config import *


def get86e6396a54f5492cB3b06678723bed4b():
    dto = dict()
    # 终端设备号
    # dto["device_id"] = "test"

    return json.dumps(dto)

def getE6adb6f3591a41ec9c6137c27ca2398d():
    dto = dict()
    # 小程序id
    # dto["app_id"] = ""

    return json.dumps(dto)

def get72948c317e164ae79d4a93cef8895c95():
    dto = dict()
    # 基站地址
    dto["base_station"] = "7"
    # ip地址
    dto["ip_addr"] = "172.28.52.52"
    # 纬度
    dto["latitude"] = "4"
    # 经度
    dto["longitude"] = "3"

    return json.dumps(dto)

def get938f9796E5bd4f85A4cf2ce4a306837d():
    dto = dict()
    # 分账明细
    # dto["acct_infos"] = get0aa0431065074e9f92016d99005ce03e()
    # 百分比分账标志
    # dto["percentage_flag"] = ""
    # 是否净值分账
    # dto["is_clean_split"] = ""

    return json.dumps(dto)

def get0aa0431065074e9f92016d99005ce03e():
    dto = dict()
    # 分账金额
    # dto["div_amt"] = ""
    # 分账接收方ID
    # dto["huifu_id"] = ""
    # 账户号
    # dto["acct_id"] = ""
    # 分账百分比%
    # dto["percentage_div"] = ""

    dtoList = [dto]
    return dtoList


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 卡号锁定标识
    extend_infos["card_number_lock"] = ""
    # 直通模式的银行标识
    extend_infos["ebank_en_abbr"] = ""
    # 交易银行卡卡号
    extend_infos["pay_card_no"] = ""
    # 支付卡类型
    # extend_infos["pay_card_type"] = ""
    # 订单失效时间
    extend_infos["time_expire"] = ""
    # 前端跳转地址
    extend_infos["front_url"] = "https://www.service.com/getresp"
    # 异步通知地址
    extend_infos["notify_url"] = "https://www.service.com/getresp"
    # 备注
    extend_infos["remark"] = "merPriv11"
    # 支付场景
    # extend_infos["pay_scene"] = ""
    # 签约令牌号
    # extend_infos["sign_token_no"] = ""
    # 延时标记
    extend_infos["delay_acct_flag"] = "Y"
    # 手续费扣款标志
    # extend_infos["fee_flag"] = ""
    # 分账对象
    # extend_infos["acct_split_bunch"] = get938f9796E5bd4f85A4cf2ce4a306837d()
    # 设备信息数据
    # extend_infos["terminal_device_data"] = get86e6396a54f5492cB3b06678723bed4b()
    return extend_infos


class TestV2TradeOnlinepaymentUnionpayRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 银联统一在线收银台 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradeOnlinepaymentUnionpayRequest()
        request.huifu_id = "6666000109133323"
        request.req_date = ""
        request.req_seq_id = ""
        request.trans_amt = "0.11"
        request.order_desc = "通用性商品1"
        request.risk_check_data = get72948c317e164ae79d4a93cef8895c95()
        request.third_pay_data = getE6adb6f3591a41ec9c6137c27ca2398d()

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
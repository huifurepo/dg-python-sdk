import unittest
import dg_sdk
import json
from demo.demo_config import *


def getAa3a4591240343e2Bad5D6a0764f06dc():
    dto = dict()
    # 省份付款方为对公账户时必填，参见省市地区码；示例值：0013
    # dto["province"] = "test"
    # 地区付款方为对公账户时必填，参见省市地区码；示例值：1301
    # dto["area"] = "test"
    # 银行编号付款方为对公账户时必填，参考：银行编码； 示例值：01040000
    # dto["bank_code"] = "test"
    # 联行号付款方为对公账户时必填，参见：银行支行编码； 示例值：102290026507
    # dto["correspondent_code"] = "test"
    # 付款方账户类型
    # dto["card_acct_type"] = ""

    return json.dumps(dto)

def get8d8843c250f94e9b80a253d37ec6f80a():
    dto = dict()
    # 设备类型
    dto["device_type"] = "4"
    # 交易设备IP
    # dto["device_ip"] = ""
    # 交易设备MAC
    # dto["device_mac"] = ""
    # 交易设备GPS
    # dto["device_gps"] = ""
    # 交易设备IMEI
    # dto["device_imei"] = ""
    # 交易设备IMSI
    # dto["device_imsi"] = ""
    # 交易设备ICCID
    # dto["device_icc_id"] = ""
    # 交易设备WIFIMAC
    # dto["device_wifi_mac"] = ""

    return json.dumps(dto)

def get195595a868964f2bB023E9566fcd0297():
    dto = dict()
    # ip地址
    # dto["ip_addr"] = ""
    # 基站地址
    # dto["base_station"] = ""
    # 纬度
    # dto["latitude"] = ""
    # 经度
    # dto["longitude"] = ""

    return json.dumps(dto)

def get4a68d378Cb6e41dfA9405a589b476160():
    dto = dict()
    # 分账明细
    dto["acct_infos"] = get33a52525B1614d3bBc18Ff7d935b2bca()

    return json.dumps(dto)

def get33a52525B1614d3bBc18Ff7d935b2bca():
    dto = dict()
    # 分账金额
    dto["div_amt"] = "0.12"
    # 分账接收方ID
    dto["huifu_id"] = "6666000003100616"

    dtoList = [dto]
    return dtoList


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 原交易全局流水号
    extend_infos["org_hf_seq_id"] = ""
    # 原交易微信支付宝的商户单号
    extend_infos["org_party_order_id"] = ""
    # 原交易请求流水号
    extend_infos["org_req_seq_id"] = "202207099803123123199941"
    # 分账对象
    extend_infos["acct_split_bunch"] = get4a68d378Cb6e41dfA9405a589b476160()
    # 备注
    # extend_infos["remark"] = ""
    # 异步通知地址
    extend_infos["notify_url"] = "http://www.baidu.com"
    return extend_infos


class TestV2TradeHostingPaymentHtrefundRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 托管交易退款 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradeHostingPaymentHtrefundRequest()
        request.req_date = ""
        request.req_seq_id = ""
        request.huifu_id = "6666000003100616"
        request.ord_amt = "0.01"
        request.org_req_date = "20240229"
        request.risk_check_data = get195595a868964f2bB023E9566fcd0297()
        request.terminal_device_data = get8d8843c250f94e9b80a253d37ec6f80a()
        request.bank_info_data = getAa3a4591240343e2Bad5D6a0764f06dc()

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
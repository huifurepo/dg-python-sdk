import unittest
import dg_sdk
import json
from demo.demo_config import *


def get289bf626B24d46cdA273Fdaa77310b55():
    dto = dict()
    # 银行编号
    # dto["bank_code"] = ""
    # 付款方账户类型
    # dto["card_acct_type"] = ""

    return json.dumps(dto)

def getF6ac280047d84b54Af3cFc21f6942cf0():
    dto = dict()
    # 补贴方汇付编号
    # dto["huifu_id"] = "test"
    # 补贴方类型
    # dto["user_type"] = "test"
    # 补贴方账户号
    # dto["acct_id"] = "test"
    # 补贴金额
    # dto["amount"] = "test"

    dtoList = [dto]
    return json.dumps(dtoList)

def getF25a2614657744d4Bc59741b0034991d():
    dto = dict()
    # 经度
    # dto["longitude"] = "test"
    # 纬度
    # dto["latitude"] = "test"
    # 基站地址
    # dto["base_station"] = "test"
    # ip地址
    dto["ip_addr"] = "172.1.1.1"

    return json.dumps(dto)

def get35d4a53eD6c1411a9ced250654fb32bc():
    dto = dict()
    # 交易设备ip
    dto["device_ip"] = "172.31.31.145"
    # 设备类型
    dto["device_type"] = "1"
    # 交易设备gps
    dto["device_gps"] = "07"
    # 交易设备iccid
    dto["device_icc_id"] = "05"
    # 交易设备imei
    dto["device_imei"] = "02"
    # 交易设备imsi
    dto["device_imsi"] = "03"
    # 交易设备mac
    dto["device_mac"] = "01"
    # 交易设备wifimac
    dto["device_wifi_mac"] = "06"
    # 终端设备号
    # dto["device_id"] = ""

    return json.dumps(dto)

def getB2063bd6B0444da8A946Df04df4862fd():
    dto = dict()
    # 分账信息列表
    # dto["acct_infos"] = get1e71bbb43d3d4de7A4a590b7e2ca4d2c()

    return json.dumps(dto)

def get1e71bbb43d3d4de7A4a590b7e2ca4d2c():
    dto = dict()
    # 商户号
    # dto["huifu_id"] = "test"
    # 支付金额
    # dto["div_amt"] = ""
    # 账户号
    # dto["acct_id"] = ""

    dtoList = [dto]
    return dtoList


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 原交易请求日期
    extend_infos["org_req_date"] = "20240401"
    # 原交易全局流水号
    extend_infos["org_hf_seq_id"] = ""
    # 原交易请求流水号
    extend_infos["org_req_seq_id"] = "295700155481522176"
    # 分账对象
    # extend_infos["acct_split_bunch"] = getB2063bd6B0444da8A946Df04df4862fd()
    # 备注
    # extend_infos["remark"] = ""
    # 异步通知地址
    extend_infos["notify_url"] = "http://www.baidu.com"
    # 补贴支付信息
    # extend_infos["combinedpay_data"] = getF6ac280047d84b54Af3cFc21f6942cf0()
    # 大额转账支付账户信息数据
    # extend_infos["bank_info_data"] = get289bf626B24d46cdA273Fdaa77310b55()
    return extend_infos


class TestV2TradeOnlinepaymentRefundRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 线上交易退款 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradeOnlinepaymentRefundRequest()
        request.req_date = ""
        request.req_seq_id = ""
        request.huifu_id = "6666000109133323"
        request.ord_amt = "0.01"
        request.terminal_device_data = get35d4a53eD6c1411a9ced250654fb32bc()
        request.risk_check_data = getF25a2614657744d4Bc59741b0034991d()

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
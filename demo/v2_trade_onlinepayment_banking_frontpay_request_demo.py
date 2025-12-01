import unittest
import dg_sdk
import json
from demo.demo_config import *


def get8334e31082524280943eE90c27c8c86e():
    dto = dict()
    # ip地址
    dto["ip_addr"] = "1"
    # 基站地址
    dto["base_station"] = "2"
    # 纬度
    dto["latitude"] = "3"
    # 经度
    dto["longitude"] = "4"

    return json.dumps(dto)

def get6cbdad332b5f4dfe89d107e7e323b3ff():
    dto = dict()
    # 交易设备类型
    dto["device_type"] = "1"
    # 交易设备IP
    dto["device_ip"] = "127.0.0.1"
    # 交易设备MAC
    # dto["device_mac"] = ""
    # 交易终端设备IMEI
    # dto["device_imei"] = ""
    # 交易设备IMSI
    # dto["device_imsi"] = ""
    # 交易设备ICCID
    # dto["device_icc_id"] = ""
    # 交易设备WIFIMAC
    # dto["device_wifi_mac"] = ""
    # 交易设备GPS
    # dto["device_gps"] = ""

    return json.dumps(dto)

def get41a3882943be433986df896d5ad9bbc7():
    dto = dict()
    # 商品简称
    dto["goods_short_name"] = "011111"
    # 网关支付受理渠道
    dto["gw_chnnl_tp"] = "01"
    # 业务种类
    dto["biz_tp"] = "123451"

    return json.dumps(dto)

def get2e3d17e1485d440aA68a0dede46dd8b3():
    dto = dict()
    # 分账明细
    # dto["acct_infos"] = getF5794a341ce740feB74dDfd50cfb54d0()
    # 百分比分账标志
    # dto["percentage_flag"] = ""
    # 是否净值分账
    # dto["is_clean_split"] = ""

    return json.dumps(dto)

def getF5794a341ce740feB74dDfd50cfb54d0():
    dto = dict()
    # 分账金额
    # dto["div_amt"] = ""
    # 分账接收方ID
    # dto["huifu_id"] = ""
    # 接收方账户号
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
    # 收款汇付账户号
    extend_infos["acct_id"] = ""
    # 订单类型
    extend_infos["order_type"] = "P"
    # 付款方银行编号
    extend_infos["bank_id"] = ""
    # 卡类型
    extend_infos["card_type"] = "D"
    # 备注
    extend_infos["remark"] = "网银支付接口"
    # 订单失效时间
    extend_infos["time_expire"] = ""
    # 网关支付类型
    extend_infos["gate_type"] = "01"
    # 延时标记
    extend_infos["delay_acct_flag"] = "N"
    # 分账对象
    # extend_infos["acct_split_bunch"] = get2e3d17e1485d440aA68a0dede46dd8b3()
    # 手续费扣款标志
    # extend_infos["fee_flag"] = ""
    # 页面跳转地址
    extend_infos["front_url"] = "http://www.chinapnr.com"
    return extend_infos


class TestV2TradeOnlinepaymentBankingFrontpayRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 网银支付 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradeOnlinepaymentBankingFrontpayRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000109133323"
        request.trans_amt = "0.02"
        request.goods_desc = "网银支付下单"
        request.extend_pay_data = get41a3882943be433986df896d5ad9bbc7()
        request.terminal_device_data = get6cbdad332b5f4dfe89d107e7e323b3ff()
        request.risk_check_data = get8334e31082524280943eE90c27c8c86e()
        request.notify_url = "http://www.chinapnr.com"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
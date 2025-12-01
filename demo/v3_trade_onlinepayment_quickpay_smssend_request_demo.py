import unittest
import dg_sdk
import json
from demo.demo_config import *


def get79bd2ee956e844ee8bb65e2f3ebf8096():
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

def getBe09da814577476eA71c6d47f2fac2ac():
    dto = dict()
    # ip地址
    dto["ip_addr"] = "106.33.180.238"
    # 基站地址
    # dto["base_station"] = ""
    # 纬度
    # dto["latitude"] = ""
    # 经度
    # dto["longitude"] = ""

    return json.dumps(dto)

def getEb10401d27a0468aA840Fd020391c341():
    dto = dict()
    # 设备类型
    dto["device_type"] = "1"
    # 交易设备ip
    dto["device_ip"] = "106.33.180.238"
    # 交易设备mac
    # dto["device_mac"] = ""
    # 交易设备imei
    # dto["device_imei"] = ""
    # 交易设备imsi
    # dto["device_imsi"] = ""
    # 交易设备iccid
    # dto["device_icc_id"] = ""
    # 交易设备wifimac
    # dto["device_wifi_mac"] = ""
    # 交易设备gps
    # dto["device_gps"] = ""

    return json.dumps(dto)

def getA552c831Cd0846b8830f0ce1be990e53():
    dto = dict()
    # 商品简称
    # dto["goods_short_name"] = "test"
    # 网关支付受理渠道
    # dto["gw_chnnl_tp"] = "test"
    # 业务种类
    # dto["biz_tp"] = "test"

    return json.dumps(dto)

def get0fda4a7803b94a2fB5f17a083f8b015f():
    dto = dict()
    # 百分比分账标志
    # dto["percentage_flag"] = ""
    # 是否净值分账
    # dto["is_clean_split"] = ""
    # 分账信息列表，Array格式
    # dto["acct_infos"] = getAdfb77e661f444deB2ddF0631bb7f4d4()

    return json.dumps(dto)

def getAdfb77e661f444deB2ddF0631bb7f4d4():
    dto = dict()
    # 分账接收方ID
    # dto["huifu_id"] = "test"
    # 分账金额
    # dto["div_amt"] = ""
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
    # 订单类型
    # extend_infos["order_type"] = ""
    # 备注
    # extend_infos["remark"] = ""
    # 订单失效时间
    # extend_infos["time_expire"] = ""
    # 分账对象
    # extend_infos["acct_split_bunch"] = get0fda4a7803b94a2fB5f17a083f8b015f()
    # 是否延迟交易
    # extend_infos["delay_acct_flag"] = ""
    # 账户号
    # extend_infos["acct_id"] = ""
    # 手续费扣款标志
    # extend_infos["fee_flag"] = ""
    # 补贴支付信息
    # extend_infos["combinedpay_data"] = get79bd2ee956e844ee8bb65e2f3ebf8096()
    return extend_infos


class TestV3TradeOnlinepaymentQuickpaySmssendRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 快捷短信发送 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V3TradeOnlinepaymentQuickpaySmssendRequest()
        request.req_date = ""
        request.req_seq_id = ""
        request.huifu_id = "6666000109133323"
        request.user_huifu_id = "6666000149909053"
        request.card_bind_id = "10049847200"
        request.trans_amt = "10.00"
        request.notify_url = "http://tianyi.demo.test.cn/core/extend/BsPaySdk/notify_quick.php"
        request.nucc_data = getA552c831Cd0846b8830f0ce1be990e53()
        request.terminal_device_data = getEb10401d27a0468aA840Fd020391c341()
        request.risk_check_data = getBe09da814577476eA71c6d47f2fac2ac()

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
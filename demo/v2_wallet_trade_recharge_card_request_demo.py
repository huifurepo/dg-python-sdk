import unittest
import dg_sdk
import json
from demo.demo_config import *


def get1a9a249fFf56429c8a73E7a93ef80c2b():
    dto = dict()
    # 交易类型
    # dto["trade_type"] = "test"
    # 买家的支付宝唯一用户号
    # dto["buyer_id"] = "test"
    # 支付宝的店铺编号
    # dto["alipay_store_id"] = ""
    # 渠道号
    # dto["channel_no"] = ""
    # 场景类型
    # dto["pay_scene"] = ""

    return json.dumps(dto)

def get5aab43a511384703Aee9A17b6d476396():
    dto = dict()
    # 交易类型
    # dto["trade_type"] = "test"
    # 子商户公众账号ID
    # dto["sub_appid"] = ""
    # 用户标识
    # dto["openid"] = ""
    # 子商户用户标识
    # dto["sub_openid"] = ""
    # 渠道号
    # dto["channel_no"] = ""
    # 场景类型
    # dto["pay_scene"] = ""

    return json.dumps(dto)

def get0994fa46Ea53463295f1Db4d35a9e9ed():
    dto = dict()
    # 银行卡序列号
    dto["token_no"] = "10000136685"
    # 跳转地址
    dto["front_url"] = "http://www.baidu.com"
    # 网联扩展数据
    dto["extend_pay_data"] = get718333af8b7c4fffAe5a25a0c20f8d7e()
    # 设备信息
    dto["terminal_device_data"] = getCecd9a03C90045d6881d47baf8ff4e54()
    # 安全信息
    dto["risk_check_data"] = getA619b5347d694307A1a8C1ef90627a60()
    # 密码页面类型
    dto["request_type"] = "M"

    return json.dumps(dto)

def getA619b5347d694307A1a8C1ef90627a60():
    dto = dict()
    # 经度
    dto["longitude"] = "2"
    # 纬度
    dto["latitude"] = "1"
    # 基站地址
    dto["base_station"] = "460001039217563"
    # IP地址
    dto["ip_addr"] = "172.28.52.52"

    return json.dumps(dto)

def getCecd9a03C90045d6881d47baf8ff4e54():
    dto = dict()
    # 交易设备类型
    dto["device_type"] = "3"
    # 交易设备IP
    dto["device_ip"] = "172.31.31.145"
    # 交易设备MAC
    dto["device_mac"] = "F0E1D2C3B4A5"
    # 交易终端设备IMEI
    dto["device_imei"] = "460030912121001"
    # 交易设备IMSI
    dto["device_imsi"] = "460030912121001"
    # 交易设备ICCID
    dto["device_icc_id"] = "898600680113F0123014"
    # 交易设备WIFI MAC
    dto["device_wifi_mac"] = "968778695A4B"
    # 交易设备经纬度
    dto["device_gps"] = "20.346790,-4.654321"

    return json.dumps(dto)

def get718333af8b7c4fffAe5a25a0c20f8d7e():
    dto = dict()
    # 业务种类编码
    dto["biz_tp"] = "100099"
    # 商品简称
    dto["goods_short_name"] = "个人电脑"
    # 支付页面类型
    dto["gw_chnnl_tp"] = "02"

    return json.dumps(dto)


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 订单失效时间
    extend_infos["time_expire"] = ""
    # 备注
    extend_infos["remark"] = "remark11"
    # 充值方式
    extend_infos["recharge_type"] = "A01"
    # 绑定卡充值信息
    extend_infos["bank_recharge_info"] = get0994fa46Ea53463295f1Db4d35a9e9ed()
    # 异步通知地址
    extend_infos["notify_url"] = "archer://C_TOPAT_NOTIFY"
    return extend_infos


class TestV2WalletTradeRechargeCardRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 钱包绑卡充值下单 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2WalletTradeRechargeCardRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000003100615"
        request.user_huifu_id = "6666000108133109"
        request.trans_amt = "10.00"
        request.wx_rechare_info = get5aab43a511384703Aee9A17b6d476396()
        request.alipay_recharge_info = get1a9a249fFf56429c8a73E7a93ef80c2b()

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
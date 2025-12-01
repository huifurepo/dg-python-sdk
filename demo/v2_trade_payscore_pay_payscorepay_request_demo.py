import unittest
import dg_sdk
import json
from demo.demo_config import *


def get471b78176649480eAacf4528fabca41b():
    dto = dict()
    # 设备类型
    # dto["device_type"] = ""
    # 交易设备IP
    # dto["device_ip"] = ""
    # 交易设备MAC
    # dto["device_mac"] = ""
    # 交易设备IMEI
    # dto["device_imei"] = ""
    # 交易设备IMSI
    # dto["device_imsi"] = ""
    # 交易设备ICCID
    # dto["device_icc_id"] = ""
    # 交易设备WIFIMAC
    # dto["device_wifi_mac"] = ""
    # 交易设备GPS
    # dto["device_gps"] = ""
    # 商户终端应用程序版
    # dto["app_version"] = ""

    return json.dumps(dto)

def get52d96afbF87746fd9cb2Beb3e46d7bd5():
    dto = dict()
    # ip地址
    dto["ip_address"] = "127.0.0.1"
    # 基站地址
    # dto["base_station"] = ""
    # 纬度
    # dto["latitude"] = ""
    # 经度
    # dto["longitude"] = ""

    return json.dumps(dto)

def get19a634c3D0034464Bcc050d33458448f():
    dto = dict()
    # 分账明细
    # dto["acct_infos"] = getE3905e1c9bd4475c81bcEa7a29aa75f8()

    return json.dumps(dto)

def getE3905e1c9bd4475c81bcEa7a29aa75f8():
    dto = dict()
    # 分账金额
    # dto["div_amt"] = "test"
    # 分账接收方ID
    # dto["huifu_id"] = "test"

    dtoList = [dto]
    return dtoList

def get2678bcc52a4848679dc2413aa3da407f():
    dto = dict()
    # 子商户用户标识
    # dto["sub_openid"] = "test"
    # 子商户公众账号id
    # dto["sub_appid"] = ""
    # 用户标识
    # dto["openid"] = ""
    # 设备号
    # dto["device_info"] = ""

    return json.dumps(dto)


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 聚合反扫微信参数集合
    # extend_infos["wx_data"] = get2678bcc52a4848679dc2413aa3da407f()
    # 是否延迟交易
    # extend_infos["delay_acct_flag"] = ""
    # 分账对象
    # extend_infos["acct_split_bunch"] = get19a634c3D0034464Bcc050d33458448f()
    # 设备信息
    # extend_infos["terminal_device_info"] = get471b78176649480eAacf4528fabca41b()
    # 交易备注
    # extend_infos["remark"] = ""
    # 商户回调地址
    # extend_infos["notify_url"] = ""
    return extend_infos


class TestV2TradePayscorePayPayscorepayRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 支付分扣款 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradePayscorePayPayscorepayRequest()
        request.req_date = ""
        request.req_seq_id = ""
        request.huifu_id = "6666000141569791"
        request.deduct_req_seq_id = "1726841301594394626"
        request.deduct_hf_seq_id = "test"
        request.out_trade_no = "03212311224952047516172"
        request.goods_desc = "bp充电"
        request.risk_check_data = get52d96afbF87746fd9cb2Beb3e46d7bd5()

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
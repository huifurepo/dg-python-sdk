import unittest
import dg_sdk
import json
from demo.demo_config import *


def getCc367526F93249e6A323E13395783a0a():
    dto = dict()
    # 收款方附加数据
    # dto["addn_data"] = ""

    return json.dumps(dto)

def get411d7c00147943a3965dF6bba761ee53():
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

    return json.dumps(dto)

def get0b045ad32faa435bBd5574b03e9e9e98():
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

def get3920c70aA6c149efBce679fc1c8d0819():
    dto = dict()
    # 补贴支付手续费承担方汇付编号
    # dto["huifu_id"] = ""
    # 补贴支付手续费承担方账户号
    # dto["acct_id"] = ""

    return json.dumps(dto)

def getC44b0e407056405aAd573d294d10ef39():
    dto = dict()
    # 汇付商户号
    # dto["huifu_id"] = "test"
    # 补贴方类型
    # dto["user_type"] = "test"
    # 补贴方账户号
    # dto["acct_id"] = "test"
    # 补贴金额
    # dto["amount"] = "test"

    dtoList = [dto]
    return json.dumps(dtoList)

def get200ed59d3a0446c68e4c07c854b89648():
    dto = dict()
    # 退款原因
    # dto["refund_desc"] = ""

    return json.dumps(dto)

def get8127ea82Bb624aa79327Cc2f375d3de1():
    dto = dict()
    # 退款商品详情
    # dto["detail"] = get0dbb50d42cbf47d9Bf0929cb435e6de5()
    # 退款原因
    # dto["refund_desc"] = ""

    return json.dumps(dto)

def get0dbb50d42cbf47d9Bf0929cb435e6de5():
    dto = dict()
    # 商品详情列表
    # dto["goods_detail"] = get0059e5f35941405694a8B9ff28bd7946()

    return dto;

def get0059e5f35941405694a8B9ff28bd7946():
    dto = dict()
    # 商品编码
    # dto["goods_id"] = "test"
    # 商品退款金额
    # dto["refund_amt"] = "test"
    # 商品退款数量
    # dto["refund_quantity"] = "test"
    # 商品单价
    # dto["price"] = "test"
    # 微信支付商品编码
    # dto["wxpay_goods_id"] = ""
    # 商品名称
    # dto["goods_name"] = ""

    dtoList = [dto]
    return dtoList

def get4629bffb4aeb4056BccfD91677682781():
    dto = dict()
    # 分账信息列表
    # dto["acct_infos"] = get87cc28b5Fc79456cB1a59d08e88fe304()

    return json.dumps(dto)

def get87cc28b5Fc79456cB1a59d08e88fe304():
    dto = dict()
    # 分账金额
    # dto["div_amt"] = "test"
    # 分账接收方ID
    # dto["huifu_id"] = "test"
    # 垫资金额
    # dto["part_loan_amt"] = ""

    dtoList = [dto]
    return dtoList


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 原交易全局流水号
    extend_infos["org_hf_seq_id"] = "002900TOP3B221107142320P992ac139c0c00000"
    # 原交易微信支付宝的商户单号
    # extend_infos["org_party_order_id"] = ""
    # 原交易请求流水号
    # extend_infos["org_req_seq_id"] = ""
    # 分账对象
    # extend_infos["acct_split_bunch"] = get4629bffb4aeb4056BccfD91677682781()
    # 聚合正扫微信拓展参数集合
    # extend_infos["wx_data"] = get8127ea82Bb624aa79327Cc2f375d3de1()
    # 数字货币扩展参数集合
    # extend_infos["digital_currency_data"] = get200ed59d3a0446c68e4c07c854b89648()
    # 补贴支付信息
    # extend_infos["combinedpay_data"] = getC44b0e407056405aAd573d294d10ef39()
    # 补贴支付手续费承担方信息
    # extend_infos["combinedpay_data_fee_info"] = get3920c70aA6c149efBce679fc1c8d0819()
    # 备注
    # extend_infos["remark"] = ""
    # 是否垫资退款
    # extend_infos["loan_flag"] = ""
    # 垫资承担者
    # extend_infos["loan_undertaker"] = ""
    # 垫资账户类型
    # extend_infos["loan_acct_type"] = ""
    # 安全信息
    # extend_infos["risk_check_data"] = get0b045ad32faa435bBd5574b03e9e9e98()
    # 设备信息
    # extend_infos["terminal_device_data"] = get411d7c00147943a3965dF6bba761ee53()
    # 异步通知地址
    # extend_infos["notify_url"] = ""
    # 银联参数集合
    # extend_infos["unionpay_data"] = getCc367526F93249e6A323E13395783a0a()
    return extend_infos


class TestV3TradePaymentScanpayRefundRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 扫码交易退款 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V3TradePaymentScanpayRefundRequest()
        request.req_date = ""
        request.req_seq_id = ""
        request.huifu_id = "6666000108854952"
        request.ord_amt = "0.01"
        request.org_req_date = "20221107"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
import unittest
import dg_sdk
import json
from demo.demo_config import *


def get0a1da7886929470c9e95Fb2789cec338():
    dto = dict()
    # 收款方附加数据
    # dto["addn_data"] = ""

    return json.dumps(dto)

def get12d1a96eBb384ca6A52c497be48f399a():
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

def get57d1c866D0554233975688940a9456ee():
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

def get4c09223048e044e3885fC33b82bc6824():
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

def get275b21c978344c1a8e42D801d27cc946():
    dto = dict()
    # 退款原因
    # dto["refund_desc"] = ""

    return json.dumps(dto)

def get306ab7a74a214b9685bf9f8b803d0799():
    dto = dict()
    # 退款商品详情
    # dto["detail"] = getD8986f4e6d8c4855A8f06f1fd2afb044()

    return json.dumps(dto)

def getD8986f4e6d8c4855A8f06f1fd2afb044():
    dto = dict()
    # 商品详情列表
    # dto["goods_detail"] = getAedeead20c724363A574D8b7611a331c()

    return dto;

def getAedeead20c724363A574D8b7611a331c():
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

def getDe44bbe09b23407c803428fb32ec77f2():
    dto = dict()
    # 分账信息列表
    # dto["acct_infos"] = get6fd50ab7Ff504f34B69cCfd37afa62c6()

    return json.dumps(dto)

def get6fd50ab7Ff504f34B69cCfd37afa62c6():
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
    # extend_infos["acct_split_bunch"] = getDe44bbe09b23407c803428fb32ec77f2()
    # 聚合正扫微信拓展参数集合
    # extend_infos["wx_data"] = get306ab7a74a214b9685bf9f8b803d0799()
    # 数字货币扩展参数集合
    # extend_infos["digital_currency_data"] = get275b21c978344c1a8e42D801d27cc946()
    # 补贴支付信息
    # extend_infos["combinedpay_data"] = get4c09223048e044e3885fC33b82bc6824()
    # 备注
    # extend_infos["remark"] = ""
    # 是否垫资退款
    # extend_infos["loan_flag"] = ""
    # 垫资承担者
    # extend_infos["loan_undertaker"] = ""
    # 垫资账户类型
    # extend_infos["loan_acct_type"] = ""
    # 安全信息
    # extend_infos["risk_check_data"] = get57d1c866D0554233975688940a9456ee()
    # 设备信息
    # extend_infos["terminal_device_data"] = get12d1a96eBb384ca6A52c497be48f399a()
    # 异步通知地址
    # extend_infos["notify_url"] = ""
    # 银联参数集合
    # extend_infos["unionpay_data"] = get0a1da7886929470c9e95Fb2789cec338()
    return extend_infos


class TestV2TradePaymentScanpayRefundRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 扫码交易退款 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradePaymentScanpayRefundRequest()
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
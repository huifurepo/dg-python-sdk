import unittest
import dg_sdk
import json
from demo.demo_config import *


def getB1c390dfB189490aAeb41d9cf8494335():
    dto = dict()
    # 业务扩展参数
    dto["extend_params"] = get7450295cC01444418648417b36ccfa18()
    # 支付宝的店铺编号
    dto["alipay_store_id"] = ""
    # 商户操作员编号
    # dto["operator_id"] = ""
    # 商户业务信息
    # dto["ali_business_params"] = ""
    # 订单包含的商品列表信息
    # dto["goods_detail"] = getD00a3da6E2774af9A886Ce75da002699()

    return json.dumps(dto)

def get7450295cC01444418648417b36ccfa18():
    dto = dict()
    # 业务主单号
    dto["trade_component_order_id"] = "2024101001502300000002570023887054"
    # 分期履约单号
    dto["tc_installment_order_id"] = "2024101001502301900002570004797346"
    # 系统商编号
    # dto["sys_service_provider_id"] = ""
    # 行业场景类型
    # dto["business_type"] = ""

    return json.dumps(dto)

def getD00a3da6E2774af9A886Ce75da002699():
    dto = dict()
    # 商品的编号
    # dto["goods_id"] = "test"
    # 商品名称
    # dto["goods_name"] = "test"
    # 商品数量
    # dto["quantity"] = "test"
    # 商品单价
    # dto["price"] = "test"
    # 商品类目
    # dto["goods_category"] = ""
    # 商品描述信息
    # dto["body"] = ""
    # 商品的展示地址
    # dto["show_url"] = ""

    dtoList = [dto]
    return dtoList

def getC9018f09676e4a9d8ff20e82c776a8d2():
    dto = dict()
    # 商户设备类型
    dto["mer_device_type"] = "01"
    # 商户终端实时经纬度信息
    dto["location"] = "+32.10520/+118.80593"
    # 商户交易设备IP
    dto["mer_device_ip"] = "10.11.12.13"
    # 设备类型
    dto["device_type"] = "1"
    # 交易设备IP
    dto["device_ip"] = "10.10.0.1"
    # 交易设备MAC
    dto["device_mac"] = "F0E1D2C3B4A5"
    # 交易设备GPS
    dto["device_gps"] = "20.346790"
    # 交易设备IMEI
    dto["device_imei"] = "660035730311000126101"
    # 交易设备IMSI
    dto["device_imsi"] = "460030912121001"
    # 交易设备ICCID
    dto["device_icc_id"] = "660035730311000126101"
    # 交易设备WIFIMAC
    dto["device_wifi_mac"] = "968778695A4B"

    return json.dumps(dto)

def get217763f244c74d4f9f6e0976741d47af():
    dto = dict()
    # IP地址
    # dto["ip_addr"] = "test"
    # 经度
    dto["longitude"] = "1"
    # 纬度
    dto["latitude"] = "2"

    return json.dumps(dto)

def get4c088b857a3c4ba38a93A3e19ae54eed():
    dto = dict()
    # 百分比分账标志
    # dto["percentage_flag"] = ""
    # 是否净值分账
    # dto["is_clean_split"] = ""
    # 分账明细
    # dto["acct_infos"] = getBb0eaeb0451a4e16Ba1095925f7b0cc5()

    return json.dumps(dto)

def getBb0eaeb0451a4e16Ba1095925f7b0cc5():
    dto = dict()
    # 分账接收方商户号
    # dto["huifu_id"] = "test"
    # 分账金额
    # dto["div_amt"] = ""
    # 分账接收方账户号
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
    # 入账账户号
    extend_infos["acct_id"] = "C02682415"
    # 交易备注
    extend_infos["remark"] = ""
    # 是否延迟交易
    # extend_infos["delay_acct_flag"] = ""
    # 分账串
    # extend_infos["acct_split_bunch"] = get4c088b857a3c4ba38a93A3e19ae54eed()
    # 设备信息
    extend_infos["terminal_device_info"] = getC9018f09676e4a9d8ff20e82c776a8d2()
    # 异步通知地址
    extend_infos["notify_url"] = "http://www.baidu.com"
    return extend_infos


class TestV2TradePayafteruseInstallmentPayRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 分期扣款 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradePayafteruseInstallmentPayRequest()
        request.req_date = ""
        request.req_seq_id = ""
        request.huifu_id = "6666000108281250"
        request.trans_amt = "0.01"
        request.goods_desc = "聚合反扫消费"
        request.risk_check_data = get217763f244c74d4f9f6e0976741d47af()
        request.alipay_data = getB1c390dfB189490aAeb41d9cf8494335()

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
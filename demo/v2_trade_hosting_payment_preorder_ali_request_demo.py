import unittest
import dg_sdk
import json
from demo.demo_config import *


def getF04a9999C9c04b2aB67dF236ec65e9b5():
    dto = dict()
    # 汇付机具号
    # dto["devs_id"] = "test"

    return json.dumps(dto)

def getD8bf3b9981df4dc996eeBe8a2bbf0087():
    dto = dict()
    # 支付宝的店铺编号
    # dto["alipay_store_id"] = ""
    # 业务扩展参数
    # dto["extend_params"] = get09625386Cefa438086d641e9521ab631()
    # 订单包含的商品列表信息
    # dto["goods_detail"] = getE60ac0f1570a4ad193e2A3bf37aa4d61()
    # 商户原始订单号
    # dto["merchant_order_no"] = ""
    # 商户操作员编号
    # dto["operator_id"] = ""
    # 产品码
    # dto["product_code"] = ""
    # 卖家支付宝用户号
    # dto["seller_id"] = ""
    # 商户门店编号
    # dto["store_id"] = ""
    # 订单标题
    # dto["subject"] = ""
    # 商家门店名称
    # dto["store_name"] = ""
    # 商户业务信息
    # dto["ali_business_params"] = ""

    return json.dumps(dto)

def getE60ac0f1570a4ad193e2A3bf37aa4d61():
    dto = dict()
    # 商品的编号
    # dto["goods_id"] = "test"
    # 商品名称
    # dto["goods_name"] = "test"
    # 商品单价(元)
    # dto["price"] = "test"
    # 商品数量
    # dto["quantity"] = "test"
    # 商品描述信息
    # dto["body"] = ""
    # 商品类目树
    # dto["categories_tree"] = ""
    # 商品类目
    # dto["goods_category"] = ""
    # 商品的展示地址
    # dto["show_url"] = ""

    dtoList = [dto]
    return dtoList

def get09625386Cefa438086d641e9521ab631():
    dto = dict()
    # 卡类型
    # dto["card_type"] = ""
    # 支付宝点餐场景类型
    # dto["food_order_type"] = ""
    # 花呗分期数
    # dto["hb_fq_num"] = ""
    # 花呗卖家手续费百分比
    # dto["hb_fq_seller_percent"] = ""
    # 行业数据回流信息
    # dto["industry_reflux_info"] = ""
    # 信用卡分期资产方式
    # dto["fq_channels"] = ""
    # 停车场id
    # dto["parking_id"] = ""
    # 系统商编号
    # dto["sys_service_provider_id"] = ""

    return dto;

def getE439a9c81e3c4577B9d3F2ef6165b83a():
    dto = dict()
    # 付款人验证（支付宝）
    # dto["payer_check_ali"] = getC5c6064e96834bceAbc7F0a3c884e3ad()
    # 个人付款人信息
    # dto["person_payer"] = getF68e675219cb4c4c9f218f85b0649774()

    return json.dumps(dto)

def getF68e675219cb4c4c9f218f85b0649774():
    dto = dict()
    # 姓名
    # dto["name"] = ""
    # 证件类型
    # dto["cert_type"] = ""
    # 证件号
    # dto["cert_no"] = ""
    # 手机号
    # dto["mobile"] = ""

    return dto;

def getC5c6064e96834bceAbc7F0a3c884e3ad():
    dto = dict()
    # 是否提供校验身份信息
    # dto["need_check_info"] = ""
    # 允许的最小买家年龄
    # dto["min_age"] = ""
    # 是否强制校验付款人身份信息
    # dto["fix_buyer"] = ""

    return dto;

def getA59791f4782447b7B929Aa2d40a6948d():
    dto = dict()
    # 小程序返回码
    dto["app_schema"] = "app跳转链接"
    # 支付宝小程序ID
    # dto["appid"] = ""
    # 私有信息
    # dto["private_info"] = ""

    return json.dumps(dto)

def get1bd403a21c424545B0601f805ef21cb4():
    dto = dict()
    # 分账明细
    dto["acct_infos"] = getEaee68182a8a41f5825379f782066dc3()
    # 百分比分账标志
    # dto["percentage_flag"] = ""
    # 是否净值分账
    # dto["is_clean_split"] = ""

    return json.dumps(dto)

def getEaee68182a8a41f5825379f782066dc3():
    dto = dict()
    # 分账金额
    dto["div_amt"] = "0.08"
    # 分账接收方ID
    dto["huifu_id"] = "6666000109133323"
    # 收款汇付账户号
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
    # extend_infos["acct_id"] = ""
    # 收银台样式
    # extend_infos["style_id"] = ""
    # 是否延迟交易
    extend_infos["delay_acct_flag"] = "N"
    # 分账对象
    extend_infos["acct_split_bunch"] = get1bd403a21c424545B0601f805ef21cb4()
    # 交易失效时间
    # extend_infos["time_expire"] = ""
    # 业务信息
    # extend_infos["biz_info"] = getE439a9c81e3c4577B9d3F2ef6165b83a()
    # 异步通知地址
    extend_infos["notify_url"] = "https://callback.service.com/xx"
    # 支付宝参数集合
    # extend_infos["alipay_data"] = getD8bf3b9981df4dc996eeBe8a2bbf0087()
    # 设备信息
    # extend_infos["terminal_device_data"] = getF04a9999C9c04b2aB67dF236ec65e9b5()
    # 手续费场景标识
    # extend_infos["fee_sign"] = ""
    return extend_infos


class TestV2TradeHostingPaymentPreorderAliRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 支付宝小程序预下单接口 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradeHostingPaymentPreorderAliRequest()
        request.huifu_id = "6666000109133323"
        request.req_date = ""
        request.req_seq_id = ""
        request.pre_order_type = "2"
        request.trans_amt = "0.10"
        request.goods_desc = "app跳支付宝消费"
        request.app_data = getA59791f4782447b7B929Aa2d40a6948d()

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
import unittest
import dg_sdk
import json
from demo.demo_config import *


def getDf28f0797b0a4813A6124c6c56213e64():
    dto = dict()
    # 付款方名称
    # dto["certificate_name"] = ""
    # 付款方银行卡号
    # dto["bank_card_no"] = ""

    return json.dumps(dto)

def get7bffc93484104442A936B8c498cbd556():
    dto = dict()
    # 汇付机具号
    # dto["devs_id"] = "test"

    return json.dumps(dto)

def get202af90c83484ed99c3837f1d649d8a1():
    dto = dict()
    # 收款方附加数据
    # dto["addn_data"] = ""
    # 地区信息
    # dto["area_info"] = ""
    # 前台通知地址
    # dto["front_url"] = ""
    # 收款方附言
    # dto["payee_comments"] = ""
    # 收款方信息
    # dto["payee_info"] = getD841636a9b5c49a19c9b4377c1512042()
    # 银联分配的服务商机构标识码
    # dto["pnr_ins_id_cd"] = ""
    # 请求方自定义域
    # dto["req_reserved"] = ""
    # 终端信息
    # dto["term_info"] = ""

    return json.dumps(dto)

def getD841636a9b5c49a19c9b4377c1512042():
    dto = dict()
    # 商户类别
    # dto["mer_cat_code"] = ""
    # 二级商户代码
    # dto["sub_id"] = ""
    # 二级商户名称
    # dto["sub_name"] = ""
    # 终端号
    # dto["term_id"] = ""

    return dto;

def getF36723caCbff4fcdAbb04bc7093d6141():
    dto = dict()
    # 支付宝的店铺编号
    # dto["alipay_store_id"] = ""
    # 业务扩展参数
    # dto["extend_params"] = get1afdd3fcD2f742fb8fe4357c3af38ffa()
    # 订单包含的商品列表信息
    # dto["goods_detail"] = getFc60e043428a45c698e9D45039edb5ac()
    # 商户原始订单号
    # dto["merchant_order_no"] = ""
    # 商户操作员编号
    # dto["operator_id"] = ""
    # 销售产品码
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

def getFc60e043428a45c698e9D45039edb5ac():
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

def get1afdd3fcD2f742fb8fe4357c3af38ffa():
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

def getDc7480bf77aa4372Bf792090dafaadc0():
    dto = dict()
    # 附加数据
    # dto["attach"] = ""
    # 商品详情
    # dto["detail"] = get9a4b9c11E708418d80bf709c75484902()
    # 订单优惠标记
    # dto["goods_tag"] = ""
    # 开发票入口开放标识
    # dto["receipt"] = ""
    # 场景信息
    # dto["scene_info"] = get0cdc6b3d5da5404c94586977aa934f1b()
    # 单品优惠标识
    # dto["promotion_flag"] = ""
    # 新增商品ID
    # dto["product_id"] = ""

    return json.dumps(dto)

def get0cdc6b3d5da5404c94586977aa934f1b():
    dto = dict()
    # 门店信息
    # dto["store_info"] = get33b30d0bF6e244349ec3D0490f82a2e6()

    return dto;

def get33b30d0bF6e244349ec3D0490f82a2e6():
    dto = dict()
    # 门店id
    # dto["id"] = ""
    # 门店名称
    # dto["name"] = ""
    # 门店行政区划码
    # dto["area_code"] = ""
    # 门店详细地址
    # dto["address"] = ""

    return dto;

def get9a4b9c11E708418d80bf709c75484902():
    dto = dict()
    # 单品列表
    # dto["goods_detail"] = get6ab36618Bab44515B1ad6c4e46ab800c()
    # 订单原价(元)
    # dto["cost_price"] = ""
    # 商品小票ID
    # dto["receipt_id"] = ""

    return dto;

def get6ab36618Bab44515B1ad6c4e46ab800c():
    dto = dict()
    # 商品编码
    # dto["goods_id"] = ""
    # 商品名称
    # dto["goods_name"] = ""
    # 商品单价(元)
    # dto["price"] = ""
    # 商品数量
    # dto["quantity"] = ""
    # 微信侧商品编码
    # dto["wxpay_goods_id"] = ""

    dtoList = [dto]
    return dtoList

def get1dcf846eCd4643199ca7E0dc052820ec():
    dto = dict()
    # 付款人验证（支付宝）
    dto["payer_check_ali"] = get3a6eeb7c3a574d468e3965cc2909c3df()
    # 付款人验证（微信）
    dto["payer_check_wx"] = getBd8a3cc7Dea74d14Ad9d12dd880476c5()
    # 个人付款人信息
    dto["person_payer"] = getFb490fd14ca14b05B239D03a18bc0f50()

    return json.dumps(dto)

def getFb490fd14ca14b05B239D03a18bc0f50():
    dto = dict()
    # 姓名
    dto["name"] = "张三"
    # 证件类型
    dto["cert_type"] = "IDENTITY_CARD"
    # 证件号
    dto["cert_no"] = "OLOxrl809XmVIMmPRTIyIpJHxi4HFMJNmxGz1nhZAtps9xPEVDysU3UZPBZfsNFLFcXEMENPsJ+tymbYt42dNQ+76hyEtx+qz0BQhU8SKV8H5itrI4kaXpaJf+sV8OewrJkhDidPdz01vqMEDQRhaMnNwl8snHZxDdpu7HVUz5JwsLYfBbZP2Q4CZpVWS3NunQahZ8zHQ+8EhvYVH1vE7f/M6nJt1/4GoHz9C/UnuYudV0S2uBhlywbX+YkRGNMl/oz5+UNeMDA2jqhtTreSD4+w7S82L53rqKsAbosodOPo4OAMZk4/0QOH5LDbqFByVM97mzHfw7z+Tx/dsXJ8QQ=="
    # 手机号
    dto["mobile"] = "15012345678"

    return dto;

def getBd8a3cc7Dea74d14Ad9d12dd880476c5():
    dto = dict()
    # 指定支付者
    dto["limit_payer"] = "ADULT"
    # 微信实名验证
    dto["real_name_flag"] = "Y"

    return dto;

def get3a6eeb7c3a574d468e3965cc2909c3df():
    dto = dict()
    # 是否提供校验身份信息
    dto["need_check_info"] = "T"
    # 允许的最小买家年龄
    dto["min_age"] = "12"
    # 是否强制校验付款人身份信息
    dto["fix_buyer"] = "F"

    return dto;

def get37ecf69dA85e4c9b83792e74236ed4bb():
    dto = dict()
    # 项目标题
    dto["project_title"] = "收银台标题"
    # 半支付托管项目号
    dto["project_id"] = "PROJECTID2023101225142567"
    # 请求类型P:PC页面版，默认：P；M:H5页面版；指定交易类型时必填；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：M&lt;/font&gt;
    # dto["request_type"] = "test"
    # 商户私有信息
    dto["private_info"] = "商户私有信息test"
    # 回调地址
    dto["callback_url"] = "https://paas.huifu.com"

    return json.dumps(dto)

def get73e4de8eDcbd43a3A5de320ee8bd6af4():
    dto = dict()
    # 分账明细
    dto["acct_infos"] = getF8427a32B7714f6bB784Cf4dfe1d5b25()
    # 百分比分账标志
    # dto["percentage_flag"] = ""
    # 是否净值分账
    # dto["is_clean_split"] = ""

    return json.dumps(dto)

def getF8427a32B7714f6bB784Cf4dfe1d5b25():
    dto = dict()
    # 分账金额
    dto["div_amt"] = "0.08"
    # 分账接收方ID
    dto["huifu_id"] = "6666000111546360"
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
    extend_infos["acct_split_bunch"] = get73e4de8eDcbd43a3A5de320ee8bd6af4()
    # 交易失效时间
    # extend_infos["time_expire"] = ""
    # 业务信息
    extend_infos["biz_info"] = get1dcf846eCd4643199ca7E0dc052820ec()
    # 交易异步通知地址
    extend_infos["notify_url"] = "https://callback.service.com/xx"
    # 使用类型
    # extend_infos["usage_type"] = ""
    # 交易类型
    # extend_infos["trans_type"] = ""
    # 微信参数集合
    # extend_infos["wx_data"] = getDc7480bf77aa4372Bf792090dafaadc0()
    # 支付宝参数集合
    # extend_infos["alipay_data"] = getF36723caCbff4fcdAbb04bc7093d6141()
    # 银联参数集合
    # extend_infos["unionpay_data"] = get202af90c83484ed99c3837f1d649d8a1()
    # 设备信息
    # extend_infos["terminal_device_data"] = get7bffc93484104442A936B8c498cbd556()
    # 大额支付参数集合
    # extend_infos["largeamt_data"] = getDf28f0797b0a4813A6124c6c56213e64()
    # 手续费场景标识
    # extend_infos["fee_sign"] = ""
    return extend_infos


class TestV2TradeHostingPaymentPreorderH5RequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # H5、PC预下单接口 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradeHostingPaymentPreorderH5Request()
        request.req_date = ""
        request.req_seq_id = ""
        request.huifu_id = "6666000109133323"
        request.trans_amt = "0.10"
        request.goods_desc = "支付托管消费"
        request.pre_order_type = "1"
        request.hosting_data = get37ecf69dA85e4c9b83792e74236ed4bb()

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
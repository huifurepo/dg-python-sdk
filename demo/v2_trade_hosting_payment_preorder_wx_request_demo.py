import unittest
import dg_sdk
import json
from demo.demo_config import *


def getBdcc7a87Bd574726Ae464bc885001747():
    dto = dict()
    # 汇付机具号
    # dto["devs_id"] = "test"

    return json.dumps(dto)

def get7c4aa8daB6d1451c90cfA6751e4d9f0d():
    dto = dict()
    # 子商户应用ID
    # dto["sub_appid"] = ""
    # 子商户用户标识
    # dto["sub_openid"] = ""
    # 附加数据
    # dto["attach"] = ""
    # 商品描述
    # dto["body"] = ""
    # 商品详情
    # dto["detail"] = getD712cf5d2f73456b8fab949fd2e1a700()
    # 设备号
    # dto["device_info"] = ""
    # 订单优惠标记
    # dto["goods_tag"] = ""
    # 实名支付
    # dto["identity"] = ""
    # 开发票入口开放标识
    # dto["receipt"] = ""
    # 场景信息
    # dto["scene_info"] = get8ecdd17236d443efA658588f1ef4423e()
    # 终端ip
    # dto["spbill_create_ip"] = ""
    # 单品优惠标识
    # dto["promotion_flag"] = ""
    # 新增商品ID
    # dto["product_id"] = ""
    # 指定支付者
    # dto["limit_payer"] = ""

    return json.dumps(dto)

def get8ecdd17236d443efA658588f1ef4423e():
    dto = dict()
    # 门店信息
    # dto["store_info"] = get3aa653d3Ea7c439796442e4081f90632()

    return dto;

def get3aa653d3Ea7c439796442e4081f90632():
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

def getD712cf5d2f73456b8fab949fd2e1a700():
    dto = dict()
    # 单品列表
    # dto["goods_detail"] = get0721682d885649fa92cfD1e681717a29()
    # 订单原价(元)
    # dto["cost_price"] = ""
    # 商品小票ID
    # dto["receipt_id"] = ""

    return dto;

def get0721682d885649fa92cfD1e681717a29():
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

def get35bc1601Bbc5479784b211331242cfae():
    dto = dict()
    # 付款人验证（微信）
    # dto["payer_check_wx"] = getE57e418fDfb94900923c2706a59737ff()
    # 个人付款人信息
    # dto["person_payer"] = get5d523d34B85c47f691acBbd78621478c()

    return json.dumps(dto)

def get5d523d34B85c47f691acBbd78621478c():
    dto = dict()
    # 姓名
    # dto["name"] = ""
    # 证件类型
    # dto["cert_type"] = ""
    # 证件号
    # dto["cert_no"] = ""

    return dto;

def getE57e418fDfb94900923c2706a59737ff():
    dto = dict()
    # 指定支付者
    # dto["limit_payer"] = ""
    # 微信实名验证
    # dto["real_name_flag"] = ""

    return dto;

def get50a16b756e9f4049866045ba95867e3e():
    dto = dict()
    # 是否生成scheme_code
    dto["need_scheme"] = "Y"
    # 应用ID
    dto["seq_id"] = "APP_2022100912694428"
    # 私有信息
    dto["private_info"] = "oppsHosting://"

    return json.dumps(dto)

def getEdc0148eE93744c893439bd821fc43ad():
    dto = dict()
    # 分账明细
    dto["acct_infos"] = get5262a85dDb4b49b099bbE54ed86e108e()
    # 百分比分账标志
    # dto["percentage_flag"] = ""
    # 是否净值分账
    # dto["is_clean_split"] = ""

    return json.dumps(dto)

def get5262a85dDb4b49b099bbE54ed86e108e():
    dto = dict()
    # 分账金额
    dto["div_amt"] = "0.01"
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
    extend_infos["delay_acct_flag"] = "Y"
    # 分账对象
    extend_infos["acct_split_bunch"] = getEdc0148eE93744c893439bd821fc43ad()
    # 交易失效时间
    # extend_infos["time_expire"] = ""
    # 业务信息
    # extend_infos["biz_info"] = get35bc1601Bbc5479784b211331242cfae()
    # 交易异步通知地址
    extend_infos["notify_url"] = "https://callback.service.com/xx"
    # 微信参数集合
    # extend_infos["wx_data"] = get7c4aa8daB6d1451c90cfA6751e4d9f0d()
    # 设备信息
    # extend_infos["terminal_device_data"] = getBdcc7a87Bd574726Ae464bc885001747()
    # 手续费场景标识
    # extend_infos["fee_sign"] = ""
    return extend_infos


class TestV2TradeHostingPaymentPreorderWxRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 微信小程序预下单接口 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradeHostingPaymentPreorderWxRequest()
        request.pre_order_type = "3"
        request.req_date = ""
        request.req_seq_id = ""
        request.huifu_id = "6666000109133323"
        request.trans_amt = "0.13"
        request.goods_desc = "app跳微信消费"
        request.miniapp_data = get50a16b756e9f4049866045ba95867e3e()

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
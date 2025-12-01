import unittest
import dg_sdk
import json
from demo.demo_config import *


def get16acf574F7904075A9126791d0c9da04():
    dto = dict()
    # 补贴手续费金额
    # dto["allowance_fee_amt"] = ""

    return json.dumps(dto)

def get81274b9d8e3d42149963F4e1b89ec35d():
    dto = dict()
    # 商户设备类型
    # dto["mer_device_type"] = "test"
    # 汇付机具号
    # dto["devs_id"] = "test"
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
    # 加密随机因子
    # dto["encrypt_rand_num"] = ""
    # SIM 卡卡号
    # dto["icc_id"] = ""
    # 商户终端实时经纬度信息
    # dto["location"] = ""
    # 商户交易设备IP
    # dto["mer_device_ip"] = ""
    # 移动国家代码
    # dto["mobile_country_cd"] = ""
    # 移动网络号码
    # dto["mobile_net_num"] = ""
    # 商户终端入网认证编号
    # dto["network_license"] = ""
    # 密文数据
    # dto["secret_text"] = ""
    # 商户终端序列号
    # dto["serial_num"] = ""

    return json.dumps(dto)

def get8ada1c173b4c47978f5eB45fa38e37ba():
    dto = dict()
    # ip地址
    dto["ip_addr"] = "180.167.105.130"
    # 基站地址
    dto["base_station"] = "192.168.1.1"
    # 纬度
    dto["latitude"] = "33.3"
    # 经度
    dto["longitude"] = "33.3"

    return json.dumps(dto)

def getBfe9f1aeEc3344f8A0a29fcf25ffbeaf():
    dto = dict()
    # 币种
    # dto["currency_code"] = ""
    # 支持发票
    # dto["invoice_st"] = ""
    # 商户类别
    # dto["mer_cat_code"] = ""
    # 服务商机构标识码
    # dto["pnr_ins_id_cd"] = ""
    # 特殊计费信息
    # dto["specfeeinfo"] = ""
    # 终端号
    # dto["term_id"] = ""
    # 收款方附加数据
    # dto["addn_data"] = ""
    # 服务商信息
    # dto["pid_info"] = get3affa45e13324e7299cdE790ac4a6999()

    return json.dumps(dto)

def get3affa45e13324e7299cdE790ac4a6999():
    dto = dict()
    # 服务商订单编号
    # dto["pnr_order_id"] = ""
    # 服务商密文
    # dto["pid_sct"] = ""
    # 场景标识
    # dto["trade_scene"] = ""

    return json.dumps(dto)

def get3696663b36214cbc85804c2680eb063d():
    dto = dict()
    # 支付宝的店铺编号
    # dto["alipay_store_id"] = ""
    # 订单包含的商品列表信息
    # dto["goods_detail"] = get6d95e247415c48feB7c6Ad25369b0f83()
    # 业务扩展参数
    # dto["extend_params"] = get0ff5e0cd6d77445a9c0352167fb46151()
    # 商户操作员编号
    # dto["operator_id"] = ""
    # 商户门店编号
    # dto["store_id"] = ""
    # 外部指定买家
    # dto["ext_user_info"] = get150c4c4368e242f6Bd0eE2894211c7f7()
    # 商户业务信息
    # dto["ali_business_params"] = ""
    # 订单描述
    # dto["body"] = ""
    # 优惠明细参数
    # dto["ali_promo_params"] = ""

    return json.dumps(dto)

def get150c4c4368e242f6Bd0eE2894211c7f7():
    dto = dict()
    # 姓名
    # dto["name"] = ""
    # 手机号
    # dto["mobile"] = ""
    # 证件类型
    # dto["cert_type"] = ""
    # 证件号
    # dto["cert_no"] = ""
    # 允许的最小买家年龄
    # dto["min_age"] = ""
    # 是否强制校验付款人身份信息
    # dto["fix_buyer"] = ""
    # 是否强制校验身份信息
    # dto["need_check_info"] = ""

    return dto;

def get0ff5e0cd6d77445a9c0352167fb46151():
    dto = dict()
    # 卡类型
    # dto["card_type"] = ""
    # 支付宝点餐场景类型
    # dto["food_order_type"] = ""
    # 花呗分期数
    # dto["hb_fq_num"] = ""
    # 花呗卖家承担的手续费百分比
    # dto["hb_fq_seller_percent"] = ""
    # 行业数据回流信息
    # dto["industry_reflux_info"] = ""
    # 停车场id
    # dto["parking_id"] = ""
    # 系统商编号
    # dto["sys_service_provider_id"] = ""

    return dto;

def get6d95e247415c48feB7c6Ad25369b0f83():
    dto = dict()
    # 商品的编号
    # dto["goods_id"] = "test"
    # 商品名称
    # dto["goods_name"] = "test"
    # 商品数量
    # dto["quantity"] = "test"
    # 商品单价
    # dto["price"] = "test"
    # 商品类目树
    # dto["categories_tree"] = ""
    # 商品类目
    # dto["goods_category"] = ""
    # 商品描述信息
    # dto["body"] = ""
    # 商品的展示地址
    # dto["show_url"] = ""

    dtoList = [dto]
    return dtoList

def getE2d5c6f716214518B0642e617526019e():
    dto = dict()
    # 收款设备IP直联模式必填字段；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：192.168.2.2&lt;/font&gt;
    # dto["spbill_create_ip"] = "test"
    # 子商户公众账号id
    # dto["sub_appid"] = ""
    # 设备号
    # dto["device_info"] = ""
    # 订单优惠标记
    # dto["goods_tag"] = ""
    # 附加数据
    # dto["attach"] = ""
    # 商品详情
    # dto["detail"] = get8a7dae8b501c42f1Affc93fcf9294b5e()
    # 场景信息
    # dto["scene_info"] = get0024c022809a490dA32810cdf7f92112()
    # 单品优惠标识
    # dto["promotion_flag"] = ""
    # 电子发票入口开放标识
    # dto["receipt"] = ""

    return json.dumps(dto)

def get0024c022809a490dA32810cdf7f92112():
    dto = dict()
    # 门店信息
    # dto["store_info"] = get673bfda44340408b9569F81c0ae0f4ec()

    return dto;

def get673bfda44340408b9569F81c0ae0f4ec():
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

def get8a7dae8b501c42f1Affc93fcf9294b5e():
    dto = dict()
    # 单品列表
    # dto["goods_detail"] = get698af00f52ea45909f10676ff299e1db()
    # 订单原价
    # dto["cost_price"] = ""
    # 商品小票ID
    # dto["receipt_id"] = ""

    return dto;

def get698af00f52ea45909f10676ff299e1db():
    dto = dict()
    # 商品编码
    # dto["goods_id"] = "test"
    # 商品数量
    # dto["quantity"] = "test"
    # 商品名称
    # dto["goods_name"] = ""
    # 商品单价
    # dto["price"] = ""
    # 微信侧商品编码
    # dto["wxpay_goods_id"] = ""

    dtoList = [dto]
    return dtoList

def get1eaecea3C37847bbB185D542b2bd9633():
    dto = dict()
    # 分账明细
    # dto["acct_infos"] = get0a57a55bB9ab42dbA559F4deac2b9a08()
    # 百分比分账标志
    # dto["percentage_flag"] = ""
    # 是否净值分账
    # dto["is_clean_split"] = ""

    return json.dumps(dto)

def get0a57a55bB9ab42dbA559F4deac2b9a08():
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

def get4a22b71a758c410981f22f3d2c0cf586():
    dto = dict()
    # 补贴支付手续费承担方汇付编号
    # dto["huifu_id"] = ""
    # 补贴支付手续费承担方账户号
    # dto["acct_id"] = ""

    return json.dumps(dto)

def getC8bf1fd60e2047518c0a373def697c94():
    dto = dict()
    # 补贴方汇付商户号
    # dto["huifu_id"] = "test"
    # 补贴方类型
    # dto["user_type"] = "test"
    # 补贴方账户号
    # dto["acct_id"] = "test"
    # 补贴金额
    # dto["amount"] = "test"

    dtoList = [dto]
    return json.dumps(dtoList)


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 交易有效期
    # extend_infos["time_expire"] = ""
    # 手续费扣款标志
    # extend_infos["fee_flag"] = ""
    # 禁用支付方式
    # extend_infos["limit_pay_type"] = ""
    # 是否延迟交易
    # extend_infos["delay_acct_flag"] = ""
    # 渠道号
    # extend_infos["channel_no"] = ""
    # 补贴支付信息
    # extend_infos["combinedpay_data"] = getC8bf1fd60e2047518c0a373def697c94()
    # 补贴支付手续费承担方信息
    # extend_infos["combinedpay_data_fee_info"] = get4a22b71a758c410981f22f3d2c0cf586()
    # 场景类型
    # extend_infos["pay_scene"] = ""
    # 分账对象
    # extend_infos["acct_split_bunch"] = get1eaecea3C37847bbB185D542b2bd9633()
    # 传入分帐遇到优惠的处理规则
    # extend_infos["term_div_coupon_type"] = ""
    # 聚合反扫微信参数集合
    # extend_infos["wx_data"] = getE2d5c6f716214518B0642e617526019e()
    # 支付宝扩展参数集合
    # extend_infos["alipay_data"] = get3696663b36214cbc85804c2680eb063d()
    # 银联参数集合
    # extend_infos["unionpay_data"] = getBfe9f1aeEc3344f8A0a29fcf25ffbeaf()
    # 设备信息
    # extend_infos["terminal_device_info"] = get81274b9d8e3d42149963F4e1b89ec35d()
    # 异步通知地址
    extend_infos["notify_url"] = "http://www.baidu.com"
    # 交易备注
    # extend_infos["remark"] = ""
    # 账户号
    # extend_infos["acct_id"] = ""
    # 手续费补贴信息
    # extend_infos["trans_fee_allowance_info"] = get16acf574F7904075A9126791d0c9da04()
    # 手续费场景标识
    # extend_infos["fee_sign"] = ""
    return extend_infos


class TestV3TradePaymentMicropayRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 聚合反扫 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V3TradePaymentMicropayRequest()
        request.req_date = ""
        request.req_seq_id = ""
        request.huifu_id = "6666000109133323"
        request.trans_amt = "1.01"
        request.goods_desc = "聚合反扫消费"
        request.auth_code = "131135212661863252"
        request.risk_check_data = get8ada1c173b4c47978f5eB45fa38e37ba()

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
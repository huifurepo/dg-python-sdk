import unittest
import dg_sdk
import json
from demo.demo_config import *


def getDddbce9400d34548Aa28C4b1e2065d66():
    dto = dict()
    # 限定付款银行卡号原文最大为20位，密文最大长度为2048；使用斗拱公钥做RSA加密；限定付款银行卡号与限定付款银行卡号掩码仅需上送一个,若限定了卡号信息该笔订单无法在pay_info拉起支付页面更换卡号支付示例值：b9LE5RccVVLChrHgo9lvp……PhWhjKrWg2NPfbe0mkQ&#x3D;&#x3D;
    # dto["limit_pay_card_no"] = "test"
    # 限定付款银行卡号掩码商户限定付款银行卡号掩码支付，需同时上送用户手机号码，仅在scene_flag&#x3D;02联合登陆场景下使用。卡号与卡号掩码仅需上送一个(掩码卡号必须是前六后四中间6个\*)
    # dto["limit_pay_card_no_mask"] = "test"
    # 手机号原文最大为11位，密文最大长度为2048；使用斗拱公钥做RSA加密；联合登陆场景下上送用户手机号(白名单商户才能支持联登)示例值：b9LE5RccVVLChrHgo9lvp……PhWhjKrWg2NPfbe0mkQ&#x3D;&#x3D;
    # dto["phone_no"] = "test"
    # 限定付款卡号银行代码简称商户想指定银行分期支付，则填上该值，取值银行代码简称，多个银行代码用&amp;分开。若上送了卡号或卡号掩码无需上送改字段，若上送需与卡号对应银行保持一致。银行代码简称：ICBC
    # dto["limit_bank_name"] = "test"
    # 场景标识01-保险实名认证：仅对保险商户使用，聚分期在持卡人分期付款前获取用户授权同意后向通过“保险实名验证接口”向商户加密传输实名信息，由保险商户验证是否与保单实名信息一致，若一致继续付款。（保险实名验证场景下无法进行联合登陆）02-联合登陆：商户侧对持卡人完成了登陆验证且为银联可信商户，聚分期对持卡人不进行登陆验证。在该场景下需同时上送登陆状态。03-限定身份信息：商户上送持卡人实名信息（customer_info）（需同时上送姓名、证件类型、证件号），银联会校验持卡人付款卡号的实名信息与商户上送的是否一致，若不一致则无法支付。若在联合登陆场景下使用限定身份信息功能，则场景标志为03-限定身份信息，同时上送登陆状态及手机号。
    # dto["scene_flag"] = "test"
    # 登录状态N-未登录，Y-已登录，登录状态：联合登陆场景下上送登陆状态，表明用户在商户侧的登陆状态，不上送默认为N。
    # dto["login_state"] = "test"
    # 门店标识用来标识商户的门店信息
    # dto["store_info"] = "test"
    # 门店名称用于前端展示商户门店名称。（需与store_info一起上送该字段，不能单独上送），不能超过15个汉字和字符
    # dto["store_name"] = "test"
    # 身份信息身份信息：场景标识为“01-实名认证”情况下，必须上送实名信息；场景标识为“02-联合登陆”下，可选上送。注：（1）实名认证场景下需同时上送姓名及证件号码（2）联合登录场景下可选上送姓名及证件号码（3）限定身份信息场景下必须上送姓名，证件号码可选上送，支持上送全量证件。
    # dto["customer_info"] = get3e5c04694365421bA9f34d0688df02b4()
    # 商品详细信息
    # dto["body_info"] = ""
    # 同步通知页面
    # dto["callback_url"] = ""
    # 标记化支付信息
    # dto["token_pay_info"] = get5b725ca8698d42779af34d580d28300a()

    return json.dumps(dto)

def get5b725ca8698d42779af34d580d28300a():
    dto = dict()
    # 标记类型
    # dto["token_type"] = "test"
    # 标记请求id
    # dto["token_id"] = "test"
    # 支付标记
    # dto["token"] = "test"

    return dto;

def get3e5c04694365421bA9f34d0688df02b4():
    dto = dict()
    # 证件类型
    # dto["certify_type"] = "test"
    # 证件号码原文最大为20位，密文最大长度为2048；使用斗拱公钥做RSA加密；示例值：b9LE5RccVVLChrHgo9lvp……PhWhjKrWg2NPfbe0mkQ&#x3D;&#x3D;
    # dto["certify_no"] = "test"
    # 姓名
    # dto["customer_name"] = "test"

    return dto;

def get8c5acd7aCf444fc2Bc680dd4aee003b4():
    dto = dict()
    # 商品数量
    dto["goods_num"] = "3"
    # 下单来源
    dto["order_source"] = "微信APP扫一扫"
    # 请求来源类型
    dto["order_source_type"] = "H5"
    # 同步通知页面
    dto["callback_url"] = "https://www.baidu.com"

    return json.dumps(dto)

def get1257a32f2ef14be2B961Db0c19b3d9f2():
    dto = dict()
    # 经度
    dto["longitude"] = "126.630128"
    # 纬度
    dto["latitude"] = "126.630128"
    # 基站地址
    dto["base_station"] = "3"
    # IP地址
    dto["ip_addr"] = "182.33.21.4"

    return json.dumps(dto)

def getD4fa236f35a2438d92a3E082b9201759():
    dto = dict()
    # 百分比分账标志
    dto["percentage_flag"] = "Y"
    # 是否净值分账
    dto["is_clean_split"] = "N"
    # 分账明细
    dto["acct_infos"] = get98bef6f0C9c94035A281E381ea90aa2e()

    return json.dumps(dto)

def get98bef6f0C9c94035A281E381ea90aa2e():
    dto = dict()
    # 商户号
    dto["huifu_id"] = "6666000100000000"
    # 分账金额
    dto["div_amt"] = ""
    # 分账百分比
    dto["percentage_div"] = "70.00"
    # 账户号
    dto["acct_id"] = ""

    dtoList = [dto]
    return dtoList


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 账户号
    # extend_infos["acct_id"] = ""
    # 交易类型
    # extend_infos["trans_type"] = ""
    # 支付场景
    # extend_infos["pay_scene"] = ""
    # 交易有效期
    extend_infos["time_expire"] = "20241008235959"
    # 手续费扣款标志
    # extend_infos["fee_flag"] = ""
    # 延时标识
    # extend_infos["delay_acct_flag"] = ""
    # 备注
    extend_infos["remark"] = "备注"
    # 异步通知地址
    extend_infos["notify_url"] = "https://www.baidu.com/onlineAsync"
    # 商户贴息标记
    # extend_infos["fq_mer_discount_flag"] = ""
    # 分账对象
    extend_infos["acct_split_bunch"] = getD4fa236f35a2438d92a3E082b9201759()
    return extend_infos


class TestV2TradeInstallmentPaymentRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 分期支付 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradeInstallmentPaymentRequest()
        request.req_date = ""
        request.req_seq_id = ""
        request.huifu_id = "6666000100000000"
        request.trans_amt = "100.00"
        request.installment_num = "3"
        request.goods_desc = "手机"
        request.risk_check_data = get1257a32f2ef14be2B961Db0c19b3d9f2()
        request.jdbt_data = get8c5acd7aCf444fc2Bc680dd4aee003b4()
        request.yljfq_data = getDddbce9400d34548Aa28C4b1e2065d66()

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
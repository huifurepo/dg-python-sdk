import unittest
import dg_sdk
import json
from demo.demo_config import *


def get0602d7b28b514194Ae8fE744b7156bb8():
    dto = dict()
    # 文件id
    # dto["file_id"] = "test"
    # 文件类型
    # dto["file_type"] = "test"

    dtoList = [dto]
    return json.dumps(dtoList)

def get5da5abafC1b84272A6d9468e68131012():
    dto = dict()
    # 电子账户开关
    # dto["switch_state"] = "test"
    # 账户类型
    # dto["acct_type"] = "test"
    # 电子账户提现手续费承担方
    # dto["cash_fee_party"] = "test"
    # 场景类型
    # dto["scene"] = "test"
    # 角色类型
    # dto["role_type"] = "test"
    # 签约成功标志
    # dto["sign_success_flag"] = "test"
    # 银行卡信息
    # dto["elec_card_list"] = get6894f407Cbb3490e88ff132ad8b2202b()
    # 中信签约短信流水号
    # dto["elec_acct_sign_seq_id"] = ""

    return json.dumps(dto)

def get6894f407Cbb3490e88ff132ad8b2202b():
    dto = dict()
    # 银行编码
    # dto["bank_code"] = "test"
    # 支行联行号
    # dto["branch_code"] = "test"
    # 支行名称
    # dto["branch_name"] = "test"
    # 结算账户名
    # dto["card_name"] = "test"
    # 银行卡号
    # dto["card_no"] = "test"
    # 卡类型
    # dto["card_type"] = "test"
    # 银行绑定手机号为空取联系人手机号，注意如果联系人非持卡人银行会报错；&lt;!--2024.5.19--&gt;&lt;font color&#x3D;&quot;green&quot;&gt;示例值:13911111111&lt;/font&gt;
    # dto["mp"] = "test"
    # 用户授权协议版本号该字段在绑定个人账户时必填，取值商户自定义。与个人用户签约的电子协议版本号，通过该版本号能够确定协议的具体内容
    # dto["auth_version"] = "test"
    # 用户授权协议号该字段在绑定个人账户时必填，取值商户自定义。与个人用户签约的授权交易流水号，通过该流水号应能确定电子协议版本号、签约人、签约时间
    # dto["auth_no"] = "test"
    # 银行所在省
    # dto["prov_id"] = ""
    # 银行所在市
    # dto["area_id"] = ""
    # 默认卡标识
    # dto["default_cash_flag"] = ""

    dtoList = [dto]
    return dtoList

def getC936e4be129540a78c77D4760c3c581a():
    dto = dict()
    # 取现类型
    dto["cash_type"] = "D1"
    # 提现手续费（固定/元）fix_amt与fee_rate至少填写一项， 需保留小数点后两位，不收费请填写0.00；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：1.00&lt;/font&gt;注：当cash_type&#x3D;D1时为节假日取现手续费
    dto["fix_amt"] = "1.00"
    # 提现手续费率（%）fix_amt与fee_rate至少填写一项，需保留小数点后两位，取值范围[0.00,100.00]，不收费请填写0.00；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：0.05&lt;/font&gt;注：1、如果fix_amt与fee_rate都填写了则手续费&#x3D;fix_amt+支付金额\*fee_rate2、当cash_type&#x3D;D1时为节假日取现手续费
    dto["fee_rate"] = ""
    # D1工作日取现手续费固定金额单位元，需保留小数点后两位。不收费请填写0.00；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：1.00&lt;/font&gt;cash_type&#x3D;T1时，不生效 ；cash_type取现类型为D1时，遇工作日按此费率结算，若未配置则默认按照节假日手续费计算
    # dto["weekday_fix_amt"] = "test"
    # D1工作日取现手续费率单位%，需保留小数点后两位。取值范围[0.00，100.00]，不收费请填写0.00；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：0.05&lt;/font&gt;cash_type&#x3D;T1时，不生效 ；cash_type取现类型为D1时，遇工作日按此费率结算 ，若未配置则默认按照节假日手续费计算
    # dto["weekday_fee_rate"] = "test"
    # 手续费承担方手续费外扣时必需指定手续费承担方ID； &lt;font color&#x3D;&quot;green&quot;&gt;示例值：6666000123123123&lt;/font&gt;
    # dto["out_fee_huifu_id"] = "test"
    # 是否交易手续费外扣
    # dto["out_fee_flag"] = ""
    # 交易手续费外扣的账户类型
    # dto["out_fee_acct_type"] = ""
    # 是否优先到账
    # dto["is_priority_receipt"] = ""

    dtoList = [dto]
    return json.dumps(dtoList)

def getE27d5818314e42e8B024Fc83008d709c():
    dto = dict()
    # 结算周期
    dto["settle_cycle"] = "D1"
    # 结算手续费外扣商户号结算手续费外扣商户号，填写承担手续费的汇付商户号&lt;br/&gt;当out_settle_flag&#x3D;1时必填，否则非必填；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：6666000123123123&lt;/font&gt;
    dto["out_settle_huifuid"] = ""
    # 结算批次号settle_cycle为TS时不填。结算方式为P0：批次结算时必填，即将按指定结算批次号进行资金结算；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：100&lt;/font&gt;；[参见结算批次说明](https://paas.huifu.com/open/doc/api/#/csfl/api_csfl_jspc)
    # dto["settle_batch_no"] = "test"
    # 自定义结算处理时间settle_cycle为TS时不填。当settle_pattern&#x3D;P1/P2自定义时间结算时必填；注意：00:00到00:30不能指定；&lt;br/&gt;到账时间，格式：HHmmss；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：103000&lt;/font&gt;
    # dto["settle_time"] = "test"
    # 节假日结算手续费率settle_cycle为D1、TS时必填。单位%，需保留小数点后两位。取值范围[0.00，100.00]，不收费请填写0.00；settle_cycle&#x3D;T1时，不生效 ；settle_cycle为D1时，遇节假日按此费率结算 ；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：0.05&lt;/font&gt;
    dto["fixed_ratio"] = "5.00"
    # 节假日结算手续费固定金额settle_cycle为D1、TS时必填。单位元，需保留小数点后两位。不收费请填写0.00；settle_cycle结算周期为D1时，遇节假日按此费率结算 ；&lt;br/&gt; &lt;font color&#x3D;&quot;green&quot;&gt;示例值：1.00&lt;/font&gt;
    # dto["constant_amt"] = "test"
    # 起结金额
    dto["min_amt"] = "1.00"
    # 留存金额
    dto["remained_amt"] = "2.00"
    # 结算摘要
    dto["settle_abstract"] = "我这里显示结算摘要"
    # 手续费外扣标记
    dto["out_settle_flag"] = "2"
    # 结算手续费外扣账户类型
    # dto["out_settle_acct_type"] = ""
    # 结算方式
    # dto["settle_pattern"] = ""
    # 是否优先到账
    # dto["is_priority_receipt"] = ""
    # 工作日结算手续费率
    # dto["workday_fixed_ratio"] = ""
    # 工作日结算手续费固定金额
    # dto["workday_constant_amt"] = ""

    return json.dumps(dto)

def getE66472f287674547A782A4f93b296ae7():
    dto = dict()
    # 卡户名
    dto["card_name"] = "张天德"
    # 结算账号
    dto["card_no"] = "4367421217494235081"
    # 银行所在市
    dto["area_id"] = "310100"
    # 持卡人证件类型
    dto["cert_type"] = "00"
    # 持卡人证件号码
    dto["cert_no"] = "321084198912066512"
    # 持卡人证件有效期类型
    dto["cert_validity_type"] = "0"
    # 持卡人证件有效期开始
    dto["cert_begin_date"] = "20180824"
    # 持卡人证件有效期截止日期格式yyyyMMdd，以北京时间为准。&lt;font color&#x3D;&quot;green&quot;&gt;示例值：20220125&lt;/font&gt;&lt;br/&gt;当cert_validity_type&#x3D;0时必填  &lt;br/&gt;当cert_validity_type&#x3D;1时为空
    dto["cert_end_date"] = "20380824"
    # 银行所在省
    dto["prov_id"] = "310000"
    # 银行编号
    dto["bank_code"] = "01030000"
    # 结算人手机号
    dto["mp"] = "13700000214"
    # 默认结算卡标志
    # dto["is_settle_default"] = ""

    return json.dumps(dto)


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 商户简称
    extend_infos["short_name"] = "张天德"
    # 经营省
    extend_infos["prov_id"] = "310000"
    # 经营市
    extend_infos["area_id"] = "310100"
    # 负责人证件有效期类型
    # extend_infos["legal_cert_validity_type"] = ""
    # 负责人职业
    # extend_infos["occupation"] = ""
    # 结算规则配置
    extend_infos["settle_config"] = getE27d5818314e42e8B024Fc83008d709c()
    # 取现信息配置
    extend_infos["cash_config"] = getC936e4be129540a78c77D4760c3c581a()
    # 商户通知标识
    extend_infos["sms_send_flag"] = "1"
    # 管理员账号
    extend_infos["login_name"] = "tinysword0116"
    # 商户主页URL
    # extend_infos["mer_url"] = ""
    # 外部商户号
    # extend_infos["ext_mer_id"] = ""
    # 备注
    # extend_infos["remarks"] = ""
    # 异步通知地址
    extend_infos["async_return_url"] = "http://192.168.85.157:30031/sspm/testVirgo"
    # 商户身份
    # extend_infos["head_office_flag"] = ""
    # 斗拱e账户功能配置
    # extend_infos["elec_acct_config"] = get5da5abafC1b84272A6d9468e68131012()
    # 扩展资料包
    # extend_infos["extended_material_list"] = get0602d7b28b514194Ae8fE744b7156bb8()
    return extend_infos


class TestV2MerchantBasicdataIndvRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 个人商户进件 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2MerchantBasicdataIndvRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.upper_huifu_id = "6666000107803321"
        request.reg_name = "张天德"
        request.mcc = "test"
        request.scene_type = "test"
        request.district_id = "310105"
        request.detail_addr = "上海市长宁区定西路1310号"
        request.legal_cert_no = "test"
        request.legal_cert_begin_date = "test"
        request.legal_cert_end_date = "test"
        request.legal_addr = "test"
        request.legal_cert_back_pic = "test"
        request.legal_cert_front_pic = "test"
        request.contact_mobile_no = "13111112222"
        request.contact_email = "jeff.peng@huifu.com"
        request.card_info = getE66472f287674547A782A4f93b296ae7()
        request.settle_card_front_pic = "test"
        request.mer_icp = "test"
        request.store_header_pic = "test"
        request.store_indoor_pic = "test"
        request.store_cashier_desk_pic = "test"
        request.head_huifu_id = "test"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
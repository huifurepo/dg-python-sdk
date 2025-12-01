import unittest
import dg_sdk
import json
from demo.demo_config import *


def get7c866c8e94dd469680cb2ce189818771():
    dto = dict()
    # 文件id
    # dto["file_id"] = "test"
    # 文件类型
    # dto["file_type"] = "test"

    dtoList = [dto]
    return json.dumps(dtoList)

def get941092a9E47f432dA9eaBc518bc37c90():
    dto = dict()
    # 签约人类型
    # dto["type"] = "test"
    # 姓名签约人类型&#x3D;联系人（经办人），必填；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：张三&lt;/font&gt;
    # dto["name"] = "test"
    # 身份证签约人类型&#x3D;联系人（经办人），必填 ；注意：**签约人会做姓名+身份证+手机号验证，请正确填写**；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：320946195712025082&lt;/font&gt;
    # dto["cert_no"] = "test"
    # 手机号签约人类型&#x3D;法人 ，必填；注意：**签约人会做姓名+身份证+手机号验证，请正确填写**；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：13917463536&lt;/font&gt;
    # dto["mobile_no"] = "test"

    return json.dumps(dto)

def get0f7d1485C48f40e4A89f8bb2d5a8e37f():
    dto = dict()
    # 是否交易手续费外扣
    # dto["out_fee_flag"] = "test"
    # 手续费(%)
    # dto["fee_rate"] = ""
    # 手续费（固定/元）
    # dto["fix_amt"] = ""
    # 外扣规则
    # dto["out_charge_mode"] = ""
    # 手续费外扣时的账户ID
    # dto["out_fee_acct_id"] = ""
    # 手续费外扣汇付ID
    # dto["out_fee_huifu_id"] = ""

    return json.dumps(dto)

def get178a42fe248246caA7c86bef48306cd7():
    dto = dict()
    # 业务类型
    # dto["pay_type"] = ""
    # 手续费外扣时的账户类型
    # dto["out_fee_acct_type"] = ""
    # 手续费外扣汇付ID
    # dto["out_fee_huifuid"] = ""
    # 是否交易手续费外扣
    # dto["out_fee_flag"] = ""

    dtoList = [dto]
    return json.dumps(dtoList)

def get048d7eb9D88b4fb18b2626380c29a731():
    dto = dict()
    # 银行编码
    # dto["bank_id"] = "test"
    # 功能开关状态
    # dto["stat_flag"] = "test"
    # 借贷标志
    # dto["dc_flag"] = "test"
    # 银行名称
    # dto["bank_name"] = ""
    # 银行中文简称
    # dto["bank_short_chn"] = ""
    # 手续费（固定/元）
    # dto["fix_amt"] = ""
    # 费率（%）
    # dto["fee_rate"] = ""

    dtoList = [dto]
    return json.dumps(dtoList)

def get4d136003Feea4f46A004Bae8c56a9346():
    dto = dict()
    # 大额支付配置列表
    # dto["large_amt_pay_config_info_list"] = getE5dbae6aFff34bd08d77953b717c7723()
    # 交易手续费外扣huifuId交易手续费外扣时必填；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：6666000108854952&lt;/font&gt;
    # dto["out_fee_huifu_id"] = "test"
    # 交易手续费外扣账户号交易手续费外扣时必填；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：F00598602&lt;/font&gt;
    # dto["out_fee_acct_id"] = "test"
    # 交易手续费外扣标记
    # dto["out_fee_flag"] = ""

    return json.dumps(dto)

def getE5dbae6aFff34bd08d77953b717c7723():
    dto = dict()
    # 费率（%）开通大额业务时必须填写一种收费方式；大于0,保留2位小数；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：1.00&lt;/font&gt;
    # dto["fee_rate"] = "test"
    # 交易手续费（固定/元）开通大额业务时必须填写一种收费方式；大于0,保留2位小数；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：10.00&lt;/font&gt;
    # dto["fee_fix_amt"] = "test"
    # 功能开关
    # dto["switch_state"] = ""
    # 大额调账标识申请类型
    # dto["biz_type"] = ""
    # 是否允许绑卡支付
    # dto["mer_same_card_recharge_flag"] = ""
    # 是否允许用户入账
    # dto["allow_user_deposit_flag"] = ""
    # 备付金固定账号模式自动退款
    # dto["provisions_auto_refund_flag"] = ""

    dtoList = [dto]
    return dtoList

def get556900d53afc493094233c83bc3778e0():
    dto = dict()
    # 取现手续费（固定/元）fix_amt与fee_rate至少填写一项， 需保留小数点后两位，不收费请填写0.00；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：1.00&lt;/font&gt;注：当cash_type&#x3D;D1时为节假日取现手续费；当cash_type&#x3D;T1时为工作日取现手续费
    # dto["fix_amt"] = "test"
    # 取现手续费率（%）fix_amt与fee_rate至少填写一项，需保留小数点后两位，取值范围[0.00,100.00]，不收费请填写0.00；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：0.05&lt;/font&gt;注：1、如果fix_amt与fee_rate都填写了则手续费&#x3D;fix_amt+支付金额\*fee_rate2、当cash_type&#x3D;D1时为节假日取现手续费；当cash_type&#x3D;T1时为工作日取现手续费
    # dto["fee_rate"] = "test"
    # D1工作日取现手续费固定金额单位元，需保留小数点后两位。不收费请填写0.00；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：1.00&lt;/font&gt;cash_type&#x3D;T1时，不生效 ；cash_type取现类型为D1时，遇工作日按此费率结算，若未配置则默认按照节假日手续费计算
    # dto["weekday_fix_amt"] = "test"
    # D1工作日取现手续费率单位%，需保留小数点后两位。取值范围[0.00，100.00]，不收费请填写0.00；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：0.05&lt;/font&gt;cash_type&#x3D;T1时，不生效 ；cash_type取现类型为D1时，遇工作日按此费率结算 ，若未配置则默认按照节假日手续费计算
    # dto["weekday_fee_rate"] = "test"
    # 手续费承担方手续费外扣时必需指定手续费承担方ID ；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：6666000123123123&lt;/font&gt;
    # dto["out_fee_huifu_id"] = "test"
    # 取现类型
    # dto["cash_type"] = ""
    # 是否取现手续费外扣
    # dto["out_fee_flag"] = ""
    # 手续费外扣的账户类型
    # dto["out_fee_acct_type"] = ""
    # 是否优先到账
    # dto["is_priority_receipt"] = ""

    dtoList = [dto]
    return json.dumps(dtoList)

def get73bc9771Ae734780938dBc671ab12fb8():
    dto = dict()
    # 银行账户名
    dto["card_name"] = "圆务铁白事"
    # 银行账号
    dto["card_no"] = "6222021287358404424"
    # 银行所在市
    dto["area_id"] = "310100"
    # 银行编码
    dto["bank_code"] = "01050000"
    # 联行号
    dto["branch_code"] = "105290071050"
    # 银行所在省
    dto["prov_id"] = "310000"

    return json.dumps(dto)


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 商户通知标识
    extend_infos["sms_send_flag"] = "1"
    # 证照类型
    extend_infos["license_type"] = "NATIONAL_LEGAL_MERGE"
    # 注册省
    extend_infos["reg_prov_id"] = "310000"
    # 注册市
    extend_infos["reg_area_id"] = "310100"
    # 法人手机号
    extend_infos["legal_mobile_no"] = "13074561767"
    # 联系人姓名
    extend_infos["contact_name"] = "文超"
    # 取现业务配置
    # extend_infos["cash_config"] = get556900d53afc493094233c83bc3778e0()
    # 大额支付配置
    # extend_infos["large_amt_pay_config"] = get4d136003Feea4f46A004Bae8c56a9346()
    # 是否开通网银充值
    # extend_infos["online_recharge_flag"] = ""
    # 线上费率配置
    # extend_infos["online_fee_conf_list"] = get048d7eb9D88b4fb18b2626380c29a731()
    # 线上手续费承担方配置
    # extend_infos["online_pay_fee_conf_list"] = get178a42fe248246caA7c86bef48306cd7()
    # 灵工支付配置
    # extend_infos["flexible_pay_config"] = get0f7d1485C48f40e4A89f8bb2d5a8e37f()
    # 电子协议异步通知地址
    # extend_infos["agreement_async_return_url"] = ""
    # 异步请求地址
    # extend_infos["async_return_url"] = ""
    # 业务开通结果异步消息接收地址
    # extend_infos["busi_async_return_url"] = ""
    # 扩展资料包
    # extend_infos["extended_material_list"] = get7c866c8e94dd469680cb2ce189818771()
    return extend_infos


class TestV2FlexibleEntRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 灵工企业商户进件接口 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2FlexibleEntRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.upper_huifu_id = "6666000108406684"
        request.mer_role = "test"
        request.local_company_type = "test"
        request.reg_name = "圆务铁白事"
        request.short_name = "沈桂英"
        request.license_pic = "f6fc539b-73ff-3645-8539-ad318971cc48"
        request.license_code = "91440101MA20250618"
        request.license_validity_type = "1"
        request.license_begin_date = "20240314"
        request.license_end_date = ""
        request.found_date = "20240314"
        request.reg_district_id = "310104"
        request.reg_detail = "方立全气气目队得形"
        request.legal_name = "天天优先"
        request.legal_cert_type = "00"
        request.legal_cert_no = "110101199003072551"
        request.legal_cert_validity_type = "1"
        request.legal_cert_begin_date = "19710718"
        request.legal_cert_end_date = ""
        request.legal_addr = "信约候再研情其常"
        request.legal_cert_back_pic = "f6fc539b-73ff-3645-8539-ad318971cc48"
        request.legal_cert_front_pic = "f6fc539b-73ff-3645-8539-ad318971cc48"
        request.store_header_pic = "f6fc539b-73ff-3645-8539-ad318971cc48"
        request.contact_mobile_no = "13074561767"
        request.contact_email = "c.vwpjkqx@urgr.be"
        request.login_name = "req2025061853130071"
        request.card_info = get73bc9771Ae734780938dBc671ab12fb8()
        request.sign_user_info = get941092a9E47f432dA9eaBc518bc37c90()

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
import unittest
import dg_sdk
import json
from demo.demo_config import *


def get30ec05a8D26c45c39e9aA02b3b1711b6():
    dto = dict()
    # 卡号
    dto["card_no"] = "6217001210064762890"
    # 银行所在省
    dto["prov_id"] = "510000"
    # 银行所在市
    dto["area_id"] = "510100"

    return json.dumps(dto)

def get2367ebbb376546c292f24ed51433e1fe():
    dto = dict()
    # 提现手续费（固定/元）fix_amt与fee_rate至少填写一项， 需保留小数点后两位，不收费请填写0.00；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：1.00&lt;/font&gt;注：当cash_type&#x3D;D1时为节假日取现手续费
    dto["fix_amt"] = ""
    # 提现手续费率（%）fix_amt与fee_rate至少填写一项，需保留小数点后两位，取值范围[0.00,100.00]，不收费请填写0.00；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：0.05&lt;/font&gt;注：1、如果fix_amt与fee_rate都填写了则手续费&#x3D;fix_amt+支付金额\*fee_rate2、当cash_type&#x3D;D1时为节假日取现手续费
    dto["fee_rate"] = "10.00"
    # D1工作日取现手续费固定金额单位元，需保留小数点后两位。不收费请填写0.00；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：1.00&lt;/font&gt;D1取现配置时选填，其他取现配置无效；cash_type取现类型为D1时，遇工作日按此费率结算，若未配置则默认按照节假日手续费计算
    dto["weekday_fix_amt"] = ""
    # D1工作日取现手续费率单位%，需保留小数点后两位。取值范围[0.00，100.00]，不收费请填写0.00；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：0.05&lt;/font&gt;D1取现配置时选填，其他取现配置无效；cash_type取现类型为D1时，遇工作日按此费率结算 ，若未配置则默认按照节假日手续费计算
    dto["weekday_fee_rate"] = ""
    # 业务类型
    dto["cash_type"] = "D1"
    # 是否交易手续费外扣
    dto["out_fee_flag"] = ""
    # 手续费承担方
    dto["out_fee_huifu_id"] = ""
    # 交易手续费外扣的账户类型
    dto["out_fee_acct_type"] = ""
    # 是否优先到账
    dto["is_priority_receipt"] = ""

    dtoList = [dto]
    return json.dumps(dtoList)

def get629fab27E82346a2860242a3c0b0d61a():
    dto = dict()
    # 个人姓名
    dto["name"] = "张三"
    # 个人身份证号码
    dto["cert_no"] = "513701195007166573"
    # 个人证件有效期类型
    dto["cert_validity_type"] = "0"
    # 个人证件有效期开始日期
    dto["cert_begin_date"] = "20120101"
    # 手机号
    dto["mobile_no"] = "13917354627"
    # 个人证件有效期截止日期
    dto["cert_end_date"] = "20320101"
    # 电子邮箱
    dto["email"] = ""
    # 管理员账号
    dto["login_name"] = "LG20250619148194131"
    # 是否发送短信标识
    dto["sms_send_flag"] = ""
    # 拓展方字段
    dto["expand_id"] = ""

    return json.dumps(dto)


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 取现配置列表
    extend_infos["cash_config"] = get2367ebbb376546c292f24ed51433e1fe()
    return extend_infos


class TestV2FlexibleIndvRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 灵工个人用户进件 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2FlexibleIndvRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.upper_huifu_id = "6666000108900391"
        request.basic_info = get629fab27E82346a2860242a3c0b0d61a()
        request.card_info = get30ec05a8D26c45c39e9aA02b3b1711b6()

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
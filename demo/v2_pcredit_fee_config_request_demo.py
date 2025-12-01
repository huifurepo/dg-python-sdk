import unittest
import dg_sdk
import json
from demo.demo_config import *


def getD940990307634ddcBaafDcdb0dd06c87():
    dto = dict()
    # 商户汇付Id
    # dto["huifu_id"] = "test"
    # 签约人类型
    # dto["sign_user_type"] = "test"
    # 签约人手机号
    # dto["mobile_no"] = "test"
    # 银联聚分期费率数据
    # dto["yljfq_fee_data"] = get582500aeD6b3421eAfa3Aacb46bbc89c()
    # 签约人姓名
    # dto["name"] = ""
    # 签约人身份证号
    # dto["cert_no"] = ""
    # 补充业务信息
    # dto["file_list"] = get5b3906c269e9412387cf7c5707a32c92()

    return json.dumps(dto)

def get5b3906c269e9412387cf7c5707a32c92():
    dto = dict()
    # 文件id
    # dto["file_id"] = "test"
    # 文件类型
    # dto["file_type"] = ""

    dtoList = [dto]
    return dtoList

def get582500aeD6b3421eAfa3Aacb46bbc89c():
    dto = dict()
    # 支付场景
    # dto["pay_scene"] = "test"
    # 业务开通标识
    # dto["open_flag"] = "test"
    # 贴息模式
    # dto["discount_model"] = ""
    # 手续费率(%)
    # dto["fee_rate"] = ""
    # 手续费扣取方式
    # dto["fee_rec_type"] = ""
    # 交易手续费扣款标记
    # dto["fee_flag"] = ""
    # 手续费外扣的汇付商户号
    # dto["out_fee_huifu_id"] = ""
    # 手续费外扣的汇付账户号
    # dto["out_fee_acct_id"] = ""

    dtoList = [dto]
    return dtoList

def get5c64baa01d644dac8995286b4cffca1b():
    dto = dict()
    # 商户汇付Id
    # dto["huifu_id"] = "test"
    # 签约人类型
    # dto["sign_user_type"] = "test"
    # 签约人手机号
    # dto["mobile_no"] = "test"
    # 挂网协议地址3-挂网协议必填；示例值：https://cloudpnrcdn.oss-cn-shanghai.aliyuncs.com/opps/api/prod/dg_gwxy/PaymentServiceAgreement_xxxx.html
    # dto["agreement_url"] = "test"
    # 京东白条费率数据
    # dto["jdbt_fee_data"] = get8e5138faDdb344b6805a94d933246d0d()
    # 签约人姓名
    # dto["name"] = ""
    # 签约人身份证号
    # dto["cert_no"] = ""
    # 协议类型
    # dto["agreement_type"] = ""

    return json.dumps(dto)

def get8e5138faDdb344b6805a94d933246d0d():
    dto = dict()
    # 支付场景
    # dto["pay_scene"] = "test"
    # 业务开通标识
    # dto["open_flag"] = "test"
    # 手续费率(%)
    # dto["fee_rate"] = ""
    # 手续费扣取方式
    # dto["fee_rec_type"] = ""
    # 交易手续费扣款标记
    # dto["fee_flag"] = ""
    # 手续费外扣的汇付商户号
    # dto["out_fee_huifu_id"] = ""
    # 手续费外扣的汇付账户号
    # dto["out_fee_acct_id"] = ""
    # 斗拱终端付息方式
    # dto["discount_model"] = ""

    dtoList = [dto]
    return dtoList

def get33058a553e95455aA0255248d770c221():
    dto = dict()
    # 商户汇付Id
    dto["huifu_id"] = "6666000003156435"
    # 花呗分期状态
    # dto["hb_fq_status"] = ""
    # 花呗分期3期开关
    dto["hb_three_period_switch"] = "Y"
    # 花呗收单分期3期费率（%）
    dto["hb_three_acq_period"] = "5"
    # 花呗分期3期利率（%）
    dto["hb_three_period"] = "10"
    # 花呗分期6期开关
    dto["hb_six_period_switch"] = "Y"
    # 花呗收单分期6期费率（%）
    dto["hb_six_acq_period"] = "5"
    # 花呗分期6期利率（%）
    dto["hb_six_period"] = "10"
    # 花呗分期12期开关
    dto["hb_twelve_period_switch"] = "Y"
    # 花呗收单分期12期费率（%）
    dto["hb_twelve_acq_period"] = "15"
    # 花呗分期12期利率（%）
    dto["hb_twelve_period"] = "11"
    # 交易手续费外扣标记
    dto["out_fee_flag"] = ""
    # 手续费外扣的汇付商户号
    dto["out_fee_huifu_id"] = ""
    # 花呗分期24期开关
    # dto["hb_twentyfour_period_switch"] = ""
    # 花呗收单分期24期费率（%）
    # dto["hb_twentyfour_acq_period"] = ""
    # 花呗分期24期利率（%）
    # dto["hb_twentyfour_period"] = ""

    dtoList = [dto]
    return json.dumps(dtoList)


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 异步通知地址
    extend_infos["async_return_url"] = "http://192.168.85.157:30031/sspm/testVirgo"
    # 花呗分期费率
    extend_infos["hb_fq_fee_list"] = get33058a553e95455aA0255248d770c221()
    # 白条分期配置对象
    # extend_infos["jdbt_data"] = get5c64baa01d644dac8995286b4cffca1b()
    # 银联聚分期配置对象
    # extend_infos["yljfq_data"] = getD940990307634ddcBaafDcdb0dd06c87()
    return extend_infos


class TestV2PcreditFeeConfigRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 商户分期配置 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2PcreditFeeConfigRequest()
        request.req_date = ""
        request.req_seq_id = ""

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
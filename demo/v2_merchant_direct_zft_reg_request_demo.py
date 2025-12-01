import unittest
import dg_sdk
import json
from demo.demo_config import *


def getA2582375Fa7747589f63B935d5a58216():
    dto = dict()
    # 文件类型
    dto["file_type"] = "F41"
    # 文件ID
    dto["file_id"] = "c679752a-9abc-326d-bb02-8cf770f56d12"
    # 文件名称
    dto["file_name"] = "身份证国徽面"

    dtoList = [dto]
    return json.dumps(dtoList)

def get75d5b1e84abd448b919eF4973ee262a0():
    dto = dict()
    # 站点类型
    dto["site_type"] = "02"
    # 站点地址
    dto["site_url"] = "站点地址"
    # 站点名称
    dto["site_name"] = "站点名称"
    # 测试账号
    dto["account"] = ""
    # 测试密码
    dto["password"] = "测试密码"

    dtoList = [dto]
    return json.dumps(dtoList)

def get0086fad238754ed3B04c0ffb7d8ce54e():
    dto = dict()
    # 卡类型
    dto["card_type"] = "1"
    # 卡借贷类型
    dto["card_flag"] = "D"
    # 户名
    dto["card_name"] = "雷均一"
    # 卡号
    dto["card_no"] = "6228480123456789"
    # 银行所在省
    dto["prov_id"] = "310000"
    # 银行所在市
    dto["area_id"] = "310100"
    # 银行号
    dto["bank_code"] = "01030000"
    # 银行名称
    dto["bank_name"] = "中国农业银行"
    # 联行号
    dto["branch_code"] = "103290076178"
    # 支行名称
    dto["branch_name"] = "中国农业银行股份有限公司上海徐汇支行"

    dtoList = [dto]
    return json.dumps(dtoList)


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 渠道商汇付ID
    extend_infos["upper_huifu_id"] = "6666000108290240"
    # 商户别名
    extend_infos["alias_name"] = "哈市盈超市"
    # 法人证件类型
    extend_infos["legal_cert_type"] = "100"
    # 联系人身份证号
    extend_infos["contact_id_card_no"] = "120101199003071300"
    # 联系人电话
    extend_infos["contact_phone"] = "13576266246"
    # 联系人电子邮箱
    extend_infos["contact_email"] = "a066545074@qq.com"
    # 商户站点信息
    extend_infos["zft_site_info_list"] = get75d5b1e84abd448b919eF4973ee262a0()
    # 审核结果异步通知地址
    extend_infos["async_return_url"] = "http://192.168.85.157:30031/sspm/testVirgo"
    # 直付通退款不退手续费开关
    extend_infos["no_refund_flag"] = "N"
    return extend_infos


class TestV2MerchantDirectZftRegRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 直付通商户入驻 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2MerchantDirectZftRegRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000108942745"
        request.name = "雷均一"
        request.merchant_type = "0"
        request.mcc = "5331"
        request.cert_type = "100"
        request.cert_no = "120101199003071300"
        request.cert_name = "I_cert_name"
        request.legal_name = "雷均一"
        request.legal_cert_no = "120101199003071300"
        request.service_phone = "10086"
        request.prov_id = "310000"
        request.area_id = "310100"
        request.district_id = "310104"
        request.detail_addr = "上海市徐汇区"
        request.contact_name = "张三"
        request.contact_tag = "02"
        request.contact_type = "LEGAL_PERSON"
        request.contact_mobile_no = "13576266246"
        request.zft_card_info_list = get0086fad238754ed3B04c0ffb7d8ce54e()
        request.alipay_logon_id = "13576266246"
        request.industry_qualification_type = ""
        request.service = "2"
        request.sign_time_with_isv = "2021-01-27"
        request.binding_alipay_logon_id = "13576266246"
        request.default_settle_type = "alipayAccount"
        request.file_list = getA2582375Fa7747589f63B935d5a58216()

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
import unittest
import dg_sdk
import json
from demo.demo_config import *


def get4da1733e10a041c7Aa241338ac87fac0():
    dto = dict()
    # 税源地ID
    # dto["tax_area_id"] = ""
    # 任务模板ID
    # dto["template_id"] = ""

    return json.dumps(dto)

def get5dc1f4fb2ca7478382dc4811aa4903f8():
    dto = dict()
    # ip地址
    # dto["ip_addr"] = ""
    # 基站地址
    dto["base_station"] = "3"
    # 纬度
    dto["latitude"] = "2"
    # 经度
    dto["longitude"] = "1"
    # 产品子类
    # dto["sub_product"] = ""
    # 转账原因
    # dto["transfer_type"] = ""

    return json.dumps(dto)

def getA7256caaCe6b490680ba86babafe4967():
    dto = dict()
    # 分账总金额（元）本次交易确认总额。需保留小数点后两位&lt;br/&gt;percentage_flag&#x3D;Y时必填。该金额与分账百分比用来计算分账金额。&lt;font color&#x3D;&quot;green&quot;&gt;示例值：10.00&lt;/font&gt;；
    # dto["total_div_amt"] = "test"
    # 百分比分账标志
    # dto["percentage_flag"] = ""
    # 分账明细
    dto["acct_infos"] = getF77aaa99F28d44d5820628512e341eac()

    return json.dumps(dto)

def getF77aaa99F28d44d5820628512e341eac():
    dto = dict()
    # 分账金额(元)单位元，需保留小数点后两位，最低传入0.01 ，&lt;font color&#x3D;&quot;green&quot;&gt;示例值：1.00&lt;/font&gt; ，percentage_flag非Y时必填；&lt;br/&gt;percentage_flag&#x3D;Y时div_amt不填，div_amt&#x3D;total_div_amt*percentage_div
    dto["div_amt"] = "0.01"
    # 分账接收方ID
    dto["huifu_id"] = "6666000109133323"
    # 分账百分比%
    # dto["percentage_div"] = ""
    # 分账接收方账户号
    # dto["acct_id"] = ""

    dtoList = [dto]
    return dtoList


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 原交易请求日期
    extend_infos["org_req_date"] = "20220512"
    # 原交易请求流水号
    extend_infos["org_req_seq_id"] = "20220512195832E06521"
    # 原交易商户订单号
    # extend_infos["org_mer_ord_id"] = ""
    # 原交易全局流水号
    extend_infos["org_hf_seq_id"] = ""
    # 分账对象
    extend_infos["acct_split_bunch"] = getA7256caaCe6b490680ba86babafe4967()
    # 安全信息
    extend_infos["risk_check_data"] = get5dc1f4fb2ca7478382dc4811aa4903f8()
    # 备注
    extend_infos["remark"] = "remark123"
    # 灵活用工标志
    # extend_infos["hyc_flag"] = ""
    # 灵活用工平台
    # extend_infos["lg_platform_type"] = ""
    # 代发模式
    # extend_infos["salary_modle_type"] = ""
    # 落地公司商户号
    # extend_infos["bmember_id"] = ""
    # 乐接活请求参数集合
    # extend_infos["ljh_data"] = get4da1733e10a041c7Aa241338ac87fac0()
    # 异步通知地址
    # extend_infos["notify_url"] = ""
    return extend_infos


class TestV2TradePaymentDelaytransConfirmRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 交易确认 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradePaymentDelaytransConfirmRequest()
        request.req_date = ""
        request.req_seq_id = ""
        request.huifu_id = "6666000109133323"
        request.pay_type = "test"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
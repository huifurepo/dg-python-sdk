import unittest
import dg_sdk
import json
from demo.demo_config import *


def get0684ecf9C4b64c0d88de7d9a0f6077a7():
    dto = dict()
    # 税源地ID
    # dto["tax_area_id"] = ""
    # 任务模板ID
    # dto["template_id"] = ""

    return json.dumps(dto)

def get21c1ce39685d47d0Abd2F5d0467e7471():
    dto = dict()
    # 转账原因
    dto["transfer_type"] = "04"
    # 产品子类
    dto["sub_product"] = "1"
    # 纬度
    # dto["latitude"] = ""
    # 经度
    # dto["longitude"] = ""
    # 基站地址
    # dto["base_station"] = ""
    # IP地址
    # dto["ip_addr"] = ""

    return json.dumps(dto)

def get9d0bec22F44249219196A84b6c917fe9():
    dto = dict()
    # 分账明细
    dto["acct_infos"] = get14a36f48897b45ef815dDb697428ce53()
    # 百分比分账标志
    # dto["percentage_flag"] = ""
    # 是否净值分账
    # dto["is_clean_split"] = ""

    return json.dumps(dto)

def get14a36f48897b45ef815dDb697428ce53():
    dto = dict()
    # 分账接收方ID
    dto["huifu_id"] = "6666000109133323"
    # 分账金额
    dto["div_amt"] = "0.01"
    # 账户号
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
    # 发起方商户号
    # extend_infos["huifu_id"] = ""
    # 商品描述
    # extend_infos["good_desc"] = ""
    # 备注
    # extend_infos["remark"] = ""
    # 是否延迟交易
    # extend_infos["delay_acct_flag"] = ""
    # 出款方账户号
    # extend_infos["out_acct_id"] = ""
    # 支付渠道
    # extend_infos["acct_channel"] = ""
    # 灵活用工标志
    # extend_infos["hyc_flag"] = ""
    # 灵活用工平台
    # extend_infos["lg_platform_type"] = ""
    # 落地公司商户号
    # extend_infos["bmember_id"] = ""
    # 乐接活请求参数集合
    # extend_infos["ljh_data"] = get0684ecf9C4b64c0d88de7d9a0f6077a7()
    # 异步通知地址
    # extend_infos["notify_url"] = ""
    # 余额支付安全核验方式
    # extend_infos["verify_type"] = ""
    return extend_infos


class TestV2TradeAcctpaymentPayRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 余额支付 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradeAcctpaymentPayRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.out_huifu_id = "6666000109133323"
        request.ord_amt = "0.01"
        request.acct_split_bunch = get9d0bec22F44249219196A84b6c917fe9()
        request.risk_check_data = get21c1ce39685d47d0Abd2F5d0467e7471()
        request.fund_type = "test"
        request.trans_fee_take_flag = "test"
        request.verify_value = "test"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
import unittest
import dg_sdk
import json
from demo.demo_config import *


def get0e2f635866394677B0d5B3a21c33cd34():
    dto = dict()
    # 实际打款日期
    # dto["actual_remit_date"] = "test"
    # 实际打款方姓名
    # dto["actual_remit_name"] = "test"
    # 实际打款金额
    # dto["actual_remit_amt"] = "test"
    # 实际打款方银行卡号
    # dto["actual_remit_card_no"] = "test"
    # 汇款凭证文件ID
    # dto["certificate_file_id"] = "test"
    # 退款卡标识
    # dto["refund_card_flag"] = "test"
    # 实际打款卡号银行名称
    # dto["actual_bank_name"] = ""

    dtoList = [dto]
    return json.dumps(dtoList)

def get8343a18fF467422b9e9c3cb76615a2bd():
    dto = dict()
    # 分账信息列表
    # dto["acct_infos"] = get506c558490c1479fA9af45d48e357290()

    return json.dumps(dto)

def get506c558490c1479fA9af45d48e357290():
    dto = dict()
    # 支付金额
    # dto["div_amt"] = ""
    # 商户号
    # dto["huifu_id"] = ""

    dtoList = [dto]
    return dtoList

def getCc3485bd801d49f7A19455ba65bbbee5():
    dto = dict()
    # 银行编号
    dto["bank_code"] = "03080000"
    # 对公对私标识
    dto["card_acct_type"] = "P"

    return json.dumps(dto)


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 下单标识
    # extend_infos["order_flag"] = ""
    # 银行模式
    # extend_infos["bank_mode"] = ""
    # 原汇款订单号
    # extend_infos["org_remittance_order_id"] = ""
    # 备注
    extend_infos["remark"] = "大额支付补入账验证"
    # 银行信息数据
    extend_infos["bank_info_data"] = getCc3485bd801d49f7A19455ba65bbbee5()
    # 延时标记
    # extend_infos["delay_acct_flag"] = ""
    # 分账对象
    # extend_infos["acct_split_bunch"] = get8343a18fF467422b9e9c3cb76615a2bd()
    # 实际打款信息
    # extend_infos["actual_remit_data"] = get0e2f635866394677B0d5B3a21c33cd34()
    return extend_infos


class TestV2TradeOnlinepaymentTransferBankmistakeApplyRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 银行大额支付差错申请 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2TradeOnlinepaymentTransferBankmistakeApplyRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000110468104"
        request.trans_amt = "0.01"
        request.order_type = "REFUND"
        request.org_req_seq_id = "202308312345678931"
        request.org_req_date = "20230831"
        request.notify_url = "http://www.baidu.com"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
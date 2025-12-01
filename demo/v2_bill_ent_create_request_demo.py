import unittest
import dg_sdk
import json
from demo.demo_config import *


def get0117bed87ef6433bAc7f831d09c77a76():
    dto = dict()
    # 收款联系人姓名
    dto["payee_name"] = "黄云"
    # 收款联系人手机payee_mobile_no、payee_tel、payee_email 三选一必填
    dto["payee_mobile_no"] = "13456787678"
    # 收款联系人座机payee_mobile_no、payee_tel、payee_email 三选一必填
    dto["payee_tel"] = "0211234444"
    # 收款联系人邮箱payee_mobile_no、payee_tel、payee_email 三选一必填
    dto["payee_email"] = "lieecho@163.com"

    return json.dumps(dto)

def get0d92fec96d1c42aaA519B4fe44b194f4():
    dto = dict()
    # 字段名
    dto["extend_name"] = "备注"
    # 字段值
    dto["extend_value"] = "额外额外"

    dtoList = [dto]
    return json.dumps(dtoList)

def get00cfe2af4f494258A34084b55e2d10f9():
    dto = dict()
    # 字段名
    dto["extend_name"] = "账单金额"
    # 字段值
    dto["extend_value"] = "128.00"

    dtoList = [dto]
    return json.dumps(dtoList)


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 账单说明
    extend_infos["bill_remark"] = "您本次 SaaS 服务周期为[开始日期]至[结束日期]。费用包括基础服务套餐[X]元，高级功能模块[X]元，总计[X]元。"
    # 汇总信息
    extend_infos["bill_summary_info"] = get00cfe2af4f494258A34084b55e2d10f9()
    # 更多信息
    extend_infos["bill_extend_info"] = get0d92fec96d1c42aaA519B4fe44b194f4()
    # 账单推送方式
    extend_infos["push_type"] = "EMAIL"
    # 抄送邮箱
    extend_infos["copy_email"] = "xxx@163.com,xxxx@163.com"
    # 备注信息
    extend_infos["remark"] = "I_remark"
    # 账单信息异步通知地址
    extend_infos["notify_url"] = "https://spin-test.cloudpnr.com/trade/billing/pcredit/status"
    # 回调地址
    extend_infos["front_url"] = "https://spin-test.cloudpnr.com/trade/billing/pcredit/status"
    return extend_infos


class TestV2BillEntCreateRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 创建企业账单 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2BillEntCreateRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000003100615"
        request.payer_id = "P2024082286286456"
        request.bill_name = "账单名称是水电费吧"
        request.bill_amt = "0.02"
        request.support_pay_type = "wx,alipay,online_b2c,online_b2b"
        request.bill_end_date = "20990909"
        request.payee_info = get0117bed87ef6433bAc7f831d09c77a76()

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
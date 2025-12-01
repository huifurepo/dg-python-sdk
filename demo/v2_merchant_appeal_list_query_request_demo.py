import unittest
import dg_sdk
import json
from demo.demo_config import *



def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 分页页码
    extend_infos["page_num"] = "1"
    # 协查单号
    extend_infos["assist_id"] = ""
    # 渠道/代理/商户/用户编号
    extend_infos["huifu_id"] = "6666000108285670"
    # 商户名称
    extend_infos["mer_name"] = ""
    # 申诉状态
    extend_infos["appeal_node"] = ""
    # 审核结论
    extend_infos["audit_result"] = ""
    # 运营处理状态
    extend_infos["operation_status"] = ""
    # 汇付处置等级
    extend_infos["handle_degree"] = ""
    return extend_infos


class TestV2MerchantAppealListQueryRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 申诉单列表查询 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2MerchantAppealListQueryRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.page_size = "20"
        request.begin_date = "20240701"
        request.end_date = "20240731"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
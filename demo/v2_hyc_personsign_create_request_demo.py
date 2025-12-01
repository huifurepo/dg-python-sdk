import unittest
import dg_sdk
import json
from demo.demo_config import *


def get9da578f4F26f413a84051de657eb1c07():
    dto = dict()
    # 合同模板id合作平台为乐接活时必填 数字格式
    # dto["contract_template_id"] = "test"
    # 任务模板id合作平台为乐接活时必填 数字格式
    # dto["task_template_id"] = "test"
    # 税源地id合作平台为乐接活时必填 数字格式
    # dto["tax_area_id"] = "test"

    return json.dumps(dto)


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 合作平台
    # extend_infos["lg_platform_type"] = ""
    # 是否发送签约短信
    extend_infos["send_sms_flag"] = "Y"
    # 签约结果通知地址
    extend_infos["asyn_url"] = ""
    return extend_infos


class TestV2HycPersonsignCreateRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 个人签约发起 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2HycPersonsignCreateRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000145962643"
        request.minor_agent_id = "L20231113140106443"
        request.ljh_data = get9da578f4F26f413a84051de657eb1c07()

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
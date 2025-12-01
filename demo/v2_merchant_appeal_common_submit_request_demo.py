import unittest
import dg_sdk
import json
from demo.demo_config import *


def get0c986afe8b424cad8c63F947666296c8():
    dto = dict()
    # 申诉文件名称
    dto["item_name"] = "法人身份证正面"
    # 申诉文件Id
    dto["file_id"] = "fede0ba8-4994-386c-966a-sd23"
    # 申诉文件类型
    dto["file_code"] = "F01"

    dtoList = [dto]
    return json.dumps(dtoList)


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 商户营业执照号
    extend_infos["mer_business_license_no"] = "916501042135"
    # app名称
    extend_infos["app_name"] = "app名称"
    # app下载链接
    extend_infos["app_url"] = "XXX"
    # 电商网址
    extend_infos["commerce_url"] = "www.baidu.com"
    # ICP备案号
    extend_infos["icp_record_no"] = "京ICP21003632-7"
    # 实际经营地址
    extend_infos["business_address"] = "实际经营地址"
    # 营业用地性质
    extend_infos["business_location_nature"] = "01"
    # 经营时长
    extend_infos["business_time"] = "09:00:00-21:30:00"
    # 经营地段
    extend_infos["business_location_type"] = "01"
    # 员工人数
    extend_infos["employee_cnt"] = "10"
    # 申诉文件列表
    extend_infos["appeal_file_list"] = get0c986afe8b424cad8c63F947666296c8()
    return extend_infos


class TestV2MerchantAppealCommonSubmitRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 提交申诉 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2MerchantAppealCommonSubmitRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.business_pattern = "03"
        request.assist_id = "202407021808060672701923328"
        request.appeal_id = "202407021808060674786492416"
        request.mer_type = "01"
        request.appeal_person_name = "张三"
        request.appeal_person_cert_no = "41162719213519"
        request.appeal_person_phone_no = "186234508"
        request.legal_name = "张三"
        request.legal_cert_no = "411627199509123"
        request.legal_phone_no = "186234502"
        request.main_business = "批发零食饮料"
        request.appeal_desc = "因XX申诉"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
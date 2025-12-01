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
    # 区分商品创建者的查询方式
    extend_infos["goods_creator_type"] = "0"
    # 商品名称
    # extend_infos["product_name"] = ""
    # 是否查询商品全量关联门店
    # extend_infos["query_all_poi"] = ""
    # 筛选在线状态
    extend_infos["status"] = "1"
    # 光标
    # extend_infos["cursor"] = ""
    # 分页数量
    # extend_infos["count"] = ""
    # 门店ID list
    extend_infos["poi_ids"] = "[23,45]"
    # 外部门店ID list
    # extend_infos["ext_ids"] = ""
    return extend_infos


class TestV2CouponDouyinProductQueryRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 抖音套餐映射接口 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2CouponDouyinProductQueryRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000108412345"
        request.bind_id = "7123fc6e5c564f539e73031c08912345"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
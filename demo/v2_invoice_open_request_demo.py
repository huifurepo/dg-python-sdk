import unittest
import dg_sdk
import json
from demo.demo_config import *


def get5a5792e6625649409ab3956876eba831():
    dto = dict()
    # 不动产地址
    # dto["addr"] = "test"
    # 不动产详细地址
    # dto["detail_addr"] = "test"
    # 跨地（市）标志
    # dto["area_flag"] = "test"
    # 租赁日期起
    # dto["start_date"] = "test"
    # 租赁日期止
    # dto["end_date"] = "test"
    # 房屋产权证书/不动产产权号
    # dto["estate_no"] = "test"
    # 不动产单位
    # dto["unit"] = "test"

    dtoList = [dto]
    return json.dumps(dtoList)

def get61765e5d4e3547ea986fE0b02a336bd0():
    dto = dict()
    # 不动产地址
    # dto["addr"] = "test"
    # 不动产详细地址
    # dto["detail_addr"] = "test"
    # 跨地（市）标志
    # dto["area_flag"] = "test"
    # 土地增值税项目编号
    # dto["tax_item_no"] = "test"
    # 不动产单元代码/网签合同备案编号
    # dto["record_no"] = "test"
    # 核定计税价格
    # dto["total_amt"] = "test"
    # 实际成交含税金额
    # dto["deal_amt"] = "test"
    # 房屋产权证书/不动产产权号
    # dto["estate_no"] = "test"
    # 不动产单位
    # dto["unit"] = "test"

    dtoList = [dto]
    return json.dumps(dtoList)

def get5ff3cd19637443d4A6faEa720f02c952():
    dto = dict()
    # 开票人
    dto["payer_name"] = "开票人"
    # 收款人
    dto["payee"] = "收款人"
    # 复核人
    dto["reviewer"] = "复核"

    return json.dumps(dto)

def get0836ea582ea54a2eBf31B03c514a80e0():
    dto = dict()
    # 发票行性质
    dto["ivc_nature"] = "0"
    # 商品序号ivc_type&#x3D;1 红票必填，要与开具的蓝票商品一致；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：备注&lt;/font&gt;
    dto["goods_serial_num"] = ""
    # 商品id二选一必填，税收分类编码优先；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：&lt;/font&gt;
    dto["goods_id"] = ""
    # 商品税收分类编码参考[商品编码](https://cloudpnrcdn.oss-cn-shanghai.aliyuncs.com/opps/api/prod/download_file/fp/%E7%94%B5%E5%AD%90%E5%8F%91%E7%A5%A8%E5%95%86%E5%93%81%E7%BC%96%E7%A0%81.xlsx)；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：1010101090000000000&lt;/font&gt;
    dto["goods_code"] = "6010000000000000000"
    # 商品名称goodsCode不为空时必填；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：&lt;/font&gt;
    dto["goods_name"] = "预付卡"
    # 税率goodsCode不为空时必填，最多三位小数；&lt;font color&#x3D;&quot;green&quot;&gt;示例值：0.130&lt;/font&gt;
    dto["tax_rate"] = "0.03"
    # 含税标识
    dto["is_price_con_tax"] = "1"
    # 金额(元)
    dto["trans_amt"] = "70.00"
    # 规格型号
    dto["goods_model"] = ""
    # 计量单位
    dto["goods_unit"] = ""
    # 优惠政策标识
    dto["preferential_flag"] = "0"
    # 零税率标示
    dto["zero_tax_rate_flag"] = ""
    # 增值税特殊管理
    dto["add_tax_spec_manage"] = ""
    # 商品数量
    dto["goods_count"] = "7"
    # 单价
    dto["goods_price"] = "10"
    # 折扣金额(元)
    dto["sale_amt"] = ""

    dtoList = [dto]
    return json.dumps(dtoList)


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 税控盘编号
    extend_infos["tax_device_id"] = "661919694739"
    # 购方单位识别号
    extend_infos["buyer_no"] = ""
    # 购方单位地址
    extend_infos["buyer_address"] = ""
    # 购方单位电话
    extend_infos["buyer_tel"] = ""
    # 购方开户行名称
    extend_infos["buyer_bank_name"] = ""
    # 购方银行账号
    extend_infos["buyer_acct_no"] = ""
    # 购方企业类型
    extend_infos["buyer_ent_type"] = ""
    # 收票人手机号
    extend_infos["rec_ivc_phone"] = ""
    # 收票人邮件
    extend_infos["rec_ivc_email"] = "test@126.com"
    # 备注
    extend_infos["resv"] = "备注"
    # 特殊票种标识
    extend_infos["special_flag"] = "00"
    # 红字信息表编号
    extend_infos["red_info_number"] = ""
    # 开票人信息
    extend_infos["payer_info"] = get5ff3cd19637443d4A6faEa720f02c952()
    # 开票结果异步通知地址
    extend_infos["callback_url"] = "virgo://http://192.168.85.157:30031/sspm/testVirgo"
    # 强制开票标识
    extend_infos["buyer_info_confirm"] = ""
    return extend_infos


class TestV2InvoiceOpenRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 发票开具 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2InvoiceOpenRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000107430944"
        request.ext_mer_id = ""
        request.channel_id = "test"
        request.ivc_type = "1"
        request.open_type = "0"
        request.buyer_name = "张三"
        request.order_amt = "70.00"
        request.red_apply_reason = "test"
        request.red_apply_source = "test"
        request.ori_ivc_code = "90222082"
        request.ori_ivc_number = "150000020026"
        request.goods_infos = get0836ea582ea54a2eBf31B03c514a80e0()
        request.estate_sales = get61765e5d4e3547ea986fE0b02a336bd0()
        request.estate_lease = get5a5792e6625649409ab3956876eba831()

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
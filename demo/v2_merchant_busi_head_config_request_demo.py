import unittest
import dg_sdk
import json
from demo.demo_config import *


def getE29d5bd315e94756A4edA0b033711bf2():
    dto = dict()
    # 本地生活开关
    # dto["llaWithholdFlag"] = "test"
    # 佣金收取手续费率
    # dto["fee_rate"] = "test"

    dtoList = [dto]
    return dtoList

def get0f3a6b82D33c433190c02a34d1f66776():
    dto = dict()
    # 业务类型
    # dto["bus_type"] = "test"
    # 手续费（百分比/%）
    # dto["fee_rate"] = "test"
    # 手续费（固定/元）
    # dto["fee_fix_amt"] = "test"
    # 是否允许开通
    # dto["open_flag"] = "test"

    dtoList = [dto]
    return json.dumps(dtoList)

def get1d2e212eE7644dcb895e8b3f957c8145():
    dto = dict()
    # 手续费（%）
    # dto["fee_rate"] = "test"
    # 保底手续费(元)
    # dto["fee_min_amt"] = "test"
    # 对公固定手续费(元)
    # dto["public_fee_fix_amt"] = "test"
    # 对私固定手续费(元)
    # dto["private_fee_fix_amt"] = "test"
    # 允许开通全域资金业务(苏商)
    # dto["open_flag"] = "test"

    return json.dumps(dto)

def get4a7da631Cce5438b97f366d1ae8daf7c():
    dto = dict()
    # 手续费（%）
    # dto["fee_rate"] = "test"
    # 固定手续费(元)
    # dto["fee_fix_amt"] = "test"
    # 允许开通大额转账业务
    # dto["open_flag"] = "test"
    # 大额支付业务模式
    # dto["business_model"] = "test"
    # 允许用户入账
    # dto["allow_user_deposit_flag"] = ""
    # 银行卡绑定支付权限
    # dto["mer_same_card_recharge_flag"] = ""
    # 备付金固定账号模式自动退款
    # dto["provisions_auto_refund_flag"] = ""

    return json.dumps(dto)

def get4d041faa65424b149f248b3fcdba2bfe():
    dto = dict()
    # 支持结算手续费外扣
    # dto["settle_out_fee_flag"] = "test"
    # 支持交易手续费外扣
    # dto["trans_fee_out_flag"] = "test"
    # 支持取现手续费外扣
    # dto["cash_out_fee_flag"] = "test"

    return json.dumps(dto)

def getE895a36e52eb4477Ba8d8c3bd48b354a():
    dto = dict()
    # 业务类型
    # dto["bus_type"] = "test"
    # 手续费（%）
    # dto["fee_rate"] = "test"
    # 固定手续费(元)
    # dto["fee_fix_amt"] = "test"
    # 允许开通取现配置
    # dto["open_flag"] = "test"

    dtoList = [dto]
    return json.dumps(dtoList)

def get63e1a90396504a4592a5A896b9bd213f():
    dto = dict()
    # 业务类型
    # dto["bus_type"] = "test"
    # 手续费（%）
    # dto["fee_rate"] = "test"
    # 固定手续费(元)
    # dto["fee_fix_amt"] = "test"
    # 允许开通结算配置
    # dto["open_flag"] = "test"

    dtoList = [dto]
    return json.dumps(dtoList)

def getC07f3d37B92442c1A07f8d0903eac9ee():
    dto = dict()
    # 手续费（%）
    # dto["fee_rate"] = "test"
    # 保底手续费(元)
    # dto["fee_min_amt"] = "test"
    # 对公固定手续费(元)
    # dto["public_fee_fix_amt"] = "test"
    # 对私固定手续费(元)
    # dto["private_fee_fix_amt"] = "test"
    # 允许开通全域资金业务(XW)
    # dto["open_flag"] = "test"

    return json.dumps(dto)

def get8157769435dd4cb893caFbf9727a50d3():
    dto = dict()
    # 手续费（%）
    # dto["fee_rate"] = "test"
    # 开户手续费（元）
    # dto["open_fee_fix_amt"] = "test"
    # 保底手续费(元)
    # dto["fee_fix_amt"] = "test"
    # 允许开通全域资金业务（华通）
    # dto["open_flag"] = "test"

    return json.dumps(dto)

def getC84085ca651043308578Bbacf5483f12():
    dto = dict()
    # 手续费（%）
    # dto["fee_rate"] = "test"
    # 固定手续费(元)
    # dto["fee_fix_amt"] = "test"
    # 允许开通大额转账业务
    # dto["open_flag"] = "test"

    return json.dumps(dto)

def get27866e83213b4344A1bd4fef613fae92():
    dto = dict()
    # 手续费（%）
    # dto["fee_rate"] = "test"
    # 固定手续费(元)
    # dto["fee_fix_amt"] = "test"
    # 允许开通补贴支付业务
    # dto["open_flag"] = "test"

    return json.dumps(dto)

def get175559260b00427591f8Ddffa93c30d1():
    dto = dict()
    # 手续费（%）
    # dto["fee_rate"] = "test"
    # 固定手续费(元)
    # dto["fee_fix_amt"] = "test"
    # 允许开通余额支付业务
    # dto["open_flag"] = "test"

    return json.dumps(dto)

def get8e066fb56e434253Bee06434bf4189b7():
    dto = dict()
    # 业务类型
    # dto["bus_type"] = "test"
    # 借贷记标识
    # dto["dc_flag"] = "test"
    # 固定手续费(元)
    # dto["fee_fix_amt"] = "test"
    # 银行号
    # dto["bank_code"] = "test"
    # 手续费（%）
    # dto["fee_rate"] = "test"
    # 允许开通线上支付业务
    # dto["open_flag"] = "test"
    # 手续费最小值（元）
    # dto["fee_min_amt"] = ""

    dtoList = [dto]
    return json.dumps(dtoList)

def get22a83a2d02524716Ad0484f35714570b():
    dto = dict()
    # 手续费（%）
    # dto["fee_rate"] = "test"
    # 允许开通支付宝直连业务
    # dto["open_flag"] = "test"

    return json.dumps(dto)

def get486010c444c1454eB24cF6f79052635b():
    dto = dict()
    # 支付场景
    # dto["pay_scene"] = "test"
    # 手续费（%）
    # dto["fee_rate"] = "test"
    # 允许开通微信直连业务
    # dto["open_flag"] = "test"

    dtoList = [dto]
    return json.dumps(dtoList)

def get1fac0b0f65034295B2ecD19723fb9a4d():
    dto = dict()
    # 手续费（%）
    # dto["fee_rate"] = "test"
    # 允许开通分账业务
    # dto["open_flag"] = "test"
    # 固定手续费(元)
    # dto["fee_fix_amt"] = ""

    return json.dumps(dto)

def getA1c90b6e4ec24902Bff7Efda73828934():
    dto = dict()
    # 借记卡手续费（%）
    # dto["debit_fee_rate"] = "test"
    # 贷记卡手续费（%）
    # dto["credit_fee_rate"] = "test"
    # 允许开通银行卡业务
    # dto["open_flag"] = "test"
    # 借记卡封顶值
    # dto["debit_fee_limit"] = ""
    # 银联手机闪付借记卡手续费1000以上（%）
    # dto["cloud_debit_fee_rate_up"] = ""
    # 银联手机闪付借记卡封顶1000以上（元）
    # dto["cloud_debit_fee_limit_up"] = ""
    # 银联手机闪付贷记卡手续费1000以上（%）
    # dto["cloud_credit_fee_rate_up"] = ""
    # 银联手机闪付借记卡手续费1000以下（%）
    # dto["cloud_debit_fee_rate_down"] = ""
    # 银联手机闪付借记卡封顶1000以下（元）
    # dto["cloud_debit_fee_limit_down"] = ""
    # 银联手机闪付贷记卡手续费1000以下（%）
    # dto["cloud_credit_fee_rate_down"] = ""

    return json.dumps(dto)

def getA450f441Eda3470e89dbE3a900acf70f():
    dto = dict()
    # 借记卡手续费1000以上(%)
    # dto["debit_fee_rate_up"] = "test"
    # 银联二维码业务贷记卡手续费1000以上(%)
    # dto["credit_fee_rate_up"] = "test"
    # 借记卡手续费1000以下(%)
    # dto["debit_fee_rate_down"] = "test"
    # 银联二维码业务贷记卡手续费1000以下(%)
    # dto["credit_fee_rate_down"] = "test"
    # 允许开通银联二维码业务
    # dto["open_flag"] = "test"
    # 银联业务手续费类型
    # dto["charge_cate_code"] = ""
    # 借记卡封顶1000以上（元）
    # dto["debit_fee_limit_up"] = ""
    # 借记卡封顶1000以下（元）
    # dto["debit_fee_limit_down"] = ""

    dtoList = [dto]
    return json.dumps(dtoList)

def get9a4d0d24741e4b78B891501ef524b9a8():
    dto = dict()
    # 支付场景
    # dto["pay_scene"] = "test"
    # 手续费
    # dto["fee_rate"] = "test"
    # 允许开通该场景业务
    # dto["open_flag"] = "test"
    # 最低收取手续费（元）
    # dto["fee_min_amt"] = "test"

    dtoList = [dto]
    return json.dumps(dtoList)

def get668d7c2dBab344f98d8c33c60b6e86ad():
    dto = dict()
    # 支付场景
    # dto["pay_scene"] = "test"
    # 手续费
    # dto["fee_rate"] = "test"
    # 允许开通该业务
    # dto["open_flag"] = "test"
    # 最低收取手续费（元）
    # dto["fee_min_amt"] = ""

    dtoList = [dto]
    return json.dumps(dtoList)


def build_extend_infos():
    """
    非必填字段

    :return: 非必填字段组成的字典
    """
    extend_infos = dict()
    # 支付宝配置对象
    # extend_infos["ali_conf_list"] = get668d7c2dBab344f98d8c33c60b6e86ad()
    # 微信配置对象
    # extend_infos["wx_conf_list"] = get9a4d0d24741e4b78B891501ef524b9a8()
    # 银联二维码配置对象
    # extend_infos["union_conf_list"] = getA450f441Eda3470e89dbE3a900acf70f()
    # 银联卡配置对象
    # extend_infos["bank_card_config"] = getA1c90b6e4ec24902Bff7Efda73828934()
    # 分账配置对象
    # extend_infos["split_config"] = get1fac0b0f65034295B2ecD19723fb9a4d()
    # 微信直连配置对象
    # extend_infos["wx_zl_conf_list"] = get486010c444c1454eB24cF6f79052635b()
    # 支付宝直连配置对象
    # extend_infos["ali_zl_conf"] = get22a83a2d02524716Ad0484f35714570b()
    # 线上配置对象
    # extend_infos["online_fee_conf_list"] = get8e066fb56e434253Bee06434bf4189b7()
    # 余额支付配置对象
    # extend_infos["balance_pay_config"] = get175559260b00427591f8Ddffa93c30d1()
    # 补贴支付配置对象
    # extend_infos["combine_pay_config"] = get27866e83213b4344A1bd4fef613fae92()
    # 银行大额转账配置对象
    # extend_infos["bank_big_amt_pay_config"] = getC84085ca651043308578Bbacf5483f12()
    # 全域资金管理配置对象（华通银行）
    # extend_infos["out_order_funds_config"] = get8157769435dd4cb893caFbf9727a50d3()
    # 全域资金管理配置(XW银行)
    # extend_infos["out_order_funds_new_net_config"] = getC07f3d37B92442c1A07f8d0903eac9ee()
    # 结算配置对象
    # extend_infos["settle_config_list"] = get63e1a90396504a4592a5A896b9bd213f()
    # 取现配置对象
    # extend_infos["cash_config_list"] = getE895a36e52eb4477Ba8d8c3bd48b354a()
    # 外扣配置对象
    # extend_infos["out_fee_config"] = get4d041faa65424b149f248b3fcdba2bfe()
    # 允许开通支付宝预授权
    # extend_infos["alipay_pre_auth_flag"] = ""
    # 允许开通微信预授权
    # extend_infos["wechatpay_pre_auth_flag"] = ""
    # 允许开通商户定时结算
    # extend_infos["mer_timing_settle_flag"] = ""
    # 允许开通商户优先结算
    # extend_infos["mer_prior_settle_flag"] = ""
    # 允许使用上级商户经营信息
    # extend_infos["use_upper_mer_auth_flag"] = ""
    # 允许使用上级商户号发起AT交易
    # extend_infos["use_upper_mer_at_trans_flag"] = ""
    # 大额支付配置
    # extend_infos["large_amt_pay_config_list"] = get4a7da631Cce5438b97f366d1ae8daf7c()
    # 全域资金管理配置(苏商)
    # extend_infos["out_order_funds_su_shang_config"] = get1d2e212eE7644dcb895e8b3f957c8145()
    # 托管支付开关
    # extend_infos["half_pay_host_flag"] = ""
    # 全域资金费用配置对象
    # extend_infos["out_order_funds_fee_list"] = get0f3a6b82D33c433190c02a34d1f66776()
    # 本地生活生活配置对象
    # extend_infos["lla_withhold_config"] = getE29d5bd315e94756A4edA0b033711bf2()
    return extend_infos


class TestV2MerchantBusiHeadConfigRequestDemo(unittest.TestCase):

    def setUp(self):
        dg_sdk.DGClient.mer_config = dg_sdk.MerConfig(PRIVATE_KEY, PUBLIC_KEY, SYS_ID, PRODUCT_ID)

        print("setup")


    # 开通下级商户权限配置接口 - 示例
    def test_request(self):

        # 接口请求对象
        request = dg_sdk.V2MerchantBusiHeadConfigRequest()
        request.req_seq_id = ""
        request.req_date = ""
        request.huifu_id = "6666000108854952"
        request.product_id = "test"
        request.upper_huifu_id = "test"

        # 所有非必填字段字典
        extend_infos = build_extend_infos()

        result = request.post(extend_infos)

        print(result)
        assert result["resp_code"] != ""
"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class ElevatorEntry(BaseModel):
    """电梯明细结构。"""

    field_0: str | None = None  # 设备注册代码
    field_1: str | None = None  # 使用地点
    field_2: str | None = None  # 电梯类型
    field_3: str | None = None  # 额定载重
    field_4: str | None = None  # 层站数
    field_5: str | None = None  # 制造单位
    field_6: str | None = None  # 安装日期
    field_7: str | None = None  # 使用状态

class MaintainEntry(BaseModel):
    """维保计划明细结构。"""

    field_0: str | None = None  # 计划编号
    field_1: str | None = None  # 所属电梯
    field_2: str | None = None  # 维保类型
    field_3: str | None = None  # 计划日期
    field_4: str | None = None  # 维保单位
    field_5: str | None = None  # 维保人员
    field_6: str | None = None  # 维保时长
    field_7: str | None = None  # 计划状态

class RecordEntry(BaseModel):
    """维保记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 所属电梯
    field_2: str | None = None  # 维保日期
    field_3: str | None = None  # 维保项目清单
    field_4: str | None = None  # 检查结论
    field_5: str | None = None  # 维保人员
    field_6: str | None = None  # 使用单位确认人
    field_7: str | None = None  # 记录状态

class YearlyEntry(BaseModel):
    """年检记录明细结构。"""

    field_0: str | None = None  # 年检编号
    field_1: str | None = None  # 所属电梯
    field_2: str | None = None  # 检验机构
    field_3: str | None = None  # 约定检验日期
    field_4: str | None = None  # 实际检验日期
    field_5: str | None = None  # 检验结论
    field_6: str | None = None  # 下次检验日期
    field_7: str | None = None  # 年检状态

class RescueEntry(BaseModel):
    """困人事件明细结构。"""

    field_0: str | None = None  # 事件编号
    field_1: str | None = None  # 事发电梯
    field_2: str | None = None  # 困人时间
    field_3: str | None = None  # 被困人数
    field_4: str | None = None  # 救援到达时间
    field_5: str | None = None  # 解救完成时间
    field_6: str | None = None  # 救援单位
    field_7: str | None = None  # 事件状态

class PartsEntry(BaseModel):
    """备件明细结构。"""

    field_0: str | None = None  # 备件编号
    field_1: str | None = None  # 备件名称
    field_2: str | None = None  # 适用机型
    field_3: str | None = None  # 规格型号
    field_4: str | None = None  # 安全存量线
    field_5: str | None = None  # 当前存量
    field_6: str | None = None  # 存放位置
    field_7: str | None = None  # 备件状态

class FaultEntry(BaseModel):
    """故障记录明细结构。"""

    field_0: str | None = None  # 故障编号
    field_1: str | None = None  # 所属电梯
    field_2: str | None = None  # 故障现象
    field_3: str | None = None  # 故障代码
    field_4: str | None = None  # 发生时间
    field_5: str | None = None  # 修复时间
    field_6: str | None = None  # 修复人员
    field_7: str | None = None  # 故障状态

class DrillEntry(BaseModel):
    """应急演练明细结构。"""

    field_0: str | None = None  # 演练编号
    field_1: str | None = None  # 演练类型
    field_2: str | None = None  # 参与单位
    field_3: str | None = None  # 演练日期
    field_4: str | None = None  # 演练时长
    field_5: str | None = None  # 参与人数
    field_6: str | None = None  # 演练评估
    field_7: str | None = None  # 演练状态

class InsuranceEntry(BaseModel):
    """保险记录明细结构。"""

    field_0: str | None = None  # 保单编号
    field_1: str | None = None  # 投保电梯
    field_2: str | None = None  # 承保公司
    field_3: str | None = None  # 保险起期
    field_4: str | None = None  # 保险止期
    field_5: str | None = None  # 保险金额
    field_6: str | None = None  # 经办人
    field_7: str | None = None  # 保单状态

class EmergencyCallEntry(BaseModel):
    """应急呼叫设备明细结构。"""

    field_0: str | None = None  # 设备编号
    field_1: str | None = None  # 所属电梯
    field_2: str | None = None  # 设备类型
    field_3: str | None = None  # 安装日期
    field_4: str | None = None  # 上次测试日期
    field_5: str | None = None  # 通话质量
    field_6: str | None = None  # 电池状态
    field_7: str | None = None  # 设备状态

class CompanyEntry(BaseModel):
    """维保单位明细结构。"""

    field_0: str | None = None  # 单位编号
    field_1: str | None = None  # 单位名称
    field_2: str | None = None  # 资质等级
    field_3: str | None = None  # 许可证号
    field_4: str | None = None  # 联系人
    field_5: str | None = None  # 联系电话
    field_6: str | None = None  # 年度考核评分
    field_7: str | None = None  # 合作状态

class SupervisorEntry(BaseModel):
    """使用单位明细结构。"""

    field_0: str | None = None  # 单位编号
    field_1: str | None = None  # 单位名称
    field_2: str | None = None  # 物业地址
    field_3: str | None = None  # 安全管理员
    field_4: str | None = None  # 联系电话
    field_5: str | None = None  # 在用电梯数
    field_6: str | None = None  # 上次检查日期
    field_7: str | None = None  # 单位状态

class LicenseEntry(BaseModel):
    """使用登记证明细结构。"""

    field_0: str | None = None  # 登记证编号
    field_1: str | None = None  # 所属电梯
    field_2: str | None = None  # 发证机关
    field_3: str | None = None  # 发证日期
    field_4: str | None = None  # 有效期至
    field_5: str | None = None  # 使用单位
    field_6: str | None = None  # 下次换证日期
    field_7: str | None = None  # 证件状态

class ComplaintEntry(BaseModel):
    """投诉记录明细结构。"""

    field_0: str | None = None  # 投诉编号
    field_1: str | None = None  # 投诉来源
    field_2: str | None = None  # 涉及电梯
    field_3: str | None = None  # 投诉内容
    field_4: str | None = None  # 投诉时间
    field_5: str | None = None  # 处理人
    field_6: str | None = None  # 办结时间
    field_7: str | None = None  # 处理状态

class RemotesEntry(BaseModel):
    """电梯监测终端明细结构。"""

    field_0: str | None = None  # 终端编号
    field_1: str | None = None  # 所属电梯
    field_2: str | None = None  # 通信方式
    field_3: str | None = None  # 在线状态
    field_4: str | None = None  # 固件版本
    field_5: str | None = None  # 上次上线时间
    field_6: str | None = None  # 数据上传间隔
    field_7: str | None = None  # 终端状态

class ContractEntry(BaseModel):
    """维保合同明细结构。"""

    field_0: str | None = None  # 合同编号
    field_1: str | None = None  # 维保单位
    field_2: str | None = None  # 使用单位
    field_3: str | None = None  # 合同金额
    field_4: str | None = None  # 维保范围
    field_5: str | None = None  # 合同起日
    field_6: str | None = None  # 合同止日
    field_7: str | None = None  # 合同状态

"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import elevator as router_elevator
from app.routers import maintain as router_maintain
from app.routers import record as router_record
from app.routers import yearly as router_yearly
from app.routers import rescue as router_rescue
from app.routers import parts as router_parts
from app.routers import fault as router_fault
from app.routers import drill as router_drill
from app.routers import insurance as router_insurance
from app.routers import emergency_call as router_emergency_call
from app.routers import company as router_company
from app.routers import supervisor as router_supervisor
from app.routers import license as router_license
from app.routers import complaint as router_complaint
from app.routers import remotes as router_remotes
from app.routers import contract as router_contract

ROUTERS = [router_elevator, router_maintain, router_record, router_yearly, router_rescue, router_parts, router_fault, router_drill, router_insurance, router_emergency_call, router_company, router_supervisor, router_license, router_complaint, router_remotes, router_contract]

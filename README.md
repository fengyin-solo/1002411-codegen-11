# 电梯安全维保监管平台

面向电梯台账、维保记录、年度检验、困人救援、备件管理、故障统计与应急演练的一体化电梯安全维保监管后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 电梯台账 | `elevator` | 电梯 | 设备注册代码、使用地点、电梯类型 |
| 维保计划 | `maintain` | 维保计划 | 计划编号、所属电梯、维保类型 |
| 维保记录 | `record` | 维保记录 | 记录编号、所属电梯、维保日期 |
| 年度检验 | `yearly` | 年检记录 | 年检编号、所属电梯、检验机构 |
| 困人救援 | `rescue` | 困人事件 | 事件编号、事发电梯、困人时间 |
| 备件管理 | `parts` | 备件 | 备件编号、备件名称、适用机型 |
| 故障统计 | `fault` | 故障记录 | 故障编号、所属电梯、故障现象 |
| 应急演练 | `drill` | 应急演练 | 演练编号、演练类型、参与单位 |
| 安全责任保险 | `insurance` | 保险记录 | 保单编号、投保电梯、承保公司 |
| 应急呼叫管理 | `emergency_call` | 应急呼叫设备 | 设备编号、所属电梯、设备类型 |
| 维保单位管理 | `company` | 维保单位 | 单位编号、单位名称、资质等级 |
| 使用单位管理 | `supervisor` | 使用单位 | 单位编号、单位名称、物业地址 |
| 使用登记证管理 | `license` | 使用登记证 | 登记证编号、所属电梯、发证机关 |
| 投诉处理 | `complaint` | 投诉记录 | 投诉编号、投诉来源、涉及电梯 |
| 物联网监测 | `remotes` | 电梯监测终端 | 终端编号、所属电梯、通信方式 |
| 维保合同管理 | `contract` | 维保合同 | 合同编号、维保单位、使用单位 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。

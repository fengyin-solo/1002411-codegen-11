<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">电梯安全维保监管平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向电梯台账、维保记录、年度检验、困人救援、备件管理、故障统计与应急演练的一体化电梯安全维保监管后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "电梯台账", path: "/elevator" }, { label: "维保计划", path: "/maintain" }, { label: "维保记录", path: "/record" }, { label: "年度检验", path: "/yearly" }, { label: "困人救援", path: "/rescue" }, { label: "备件管理", path: "/parts" }, { label: "故障统计", path: "/fault" }, { label: "应急演练", path: "/drill" }, { label: "安全责任保险", path: "/insurance" }, { label: "应急呼叫管理", path: "/emergency_call" }, { label: "维保单位管理", path: "/company" }, { label: "使用单位管理", path: "/supervisor" }, { label: "使用登记证管理", path: "/license" }, { label: "投诉处理", path: "/complaint" }, { label: "物联网监测", path: "/remotes" }, { label: "维保合同管理", path: "/contract" }]
</script>

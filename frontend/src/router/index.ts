import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Elevator = () => import('@/views/elevator/index.vue')
const Maintain = () => import('@/views/maintain/index.vue')
const Record = () => import('@/views/record/index.vue')
const Yearly = () => import('@/views/yearly/index.vue')
const Rescue = () => import('@/views/rescue/index.vue')
const Parts = () => import('@/views/parts/index.vue')
const Fault = () => import('@/views/fault/index.vue')
const Drill = () => import('@/views/drill/index.vue')
const Insurance = () => import('@/views/insurance/index.vue')
const EmergencyCall = () => import('@/views/emergency_call/index.vue')
const Company = () => import('@/views/company/index.vue')
const Supervisor = () => import('@/views/supervisor/index.vue')
const License = () => import('@/views/license/index.vue')
const Complaint = () => import('@/views/complaint/index.vue')
const Remotes = () => import('@/views/remotes/index.vue')
const Contract = () => import('@/views/contract/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/elevator', name: 'elevator', component: Elevator },
    { path: '/maintain', name: 'maintain', component: Maintain },
    { path: '/record', name: 'record', component: Record },
    { path: '/yearly', name: 'yearly', component: Yearly },
    { path: '/rescue', name: 'rescue', component: Rescue },
    { path: '/parts', name: 'parts', component: Parts },
    { path: '/fault', name: 'fault', component: Fault },
    { path: '/drill', name: 'drill', component: Drill },
    { path: '/insurance', name: 'insurance', component: Insurance },
    { path: '/emergency_call', name: 'emergency_call', component: EmergencyCall },
    { path: '/company', name: 'company', component: Company },
    { path: '/supervisor', name: 'supervisor', component: Supervisor },
    { path: '/license', name: 'license', component: License },
    { path: '/complaint', name: 'complaint', component: Complaint },
    { path: '/remotes', name: 'remotes', component: Remotes },
    { path: '/contract', name: 'contract', component: Contract },
  ],
})

export default router

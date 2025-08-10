// editor-frontend/src/main.ts

import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import type { App as VueApp } from 'vue' // TypeScript specific import

import App from './App.vue'
import router from './router'

const app: VueApp<Element> = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
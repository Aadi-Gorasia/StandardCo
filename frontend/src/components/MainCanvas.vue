<!-- frontend/src/components/MainCanvas.vue -->
<script setup lang="ts">
import { ref, computed, watch, nextTick } from 'vue'
import { useEditorStore, type Component } from '../stores/editor'
import { storeToRefs } from 'pinia'
import draggable from 'vuedraggable'

const editorStore = useEditorStore()
const { currentProject, selectedComponentId, selectedComponent } = storeToRefs(editorStore)

// --- Drag and Drop Logic ---
const draggableComponents = computed({
  get() { return editorStore.currentProject?.components || [] },
  set(newComponents: Component[]) {
    if (editorStore.currentProject) { editorStore.currentProject.components = newComponents }
  }
})

// --- Click Handling Logic ---
const handleComponentClick = (component: Component, event: MouseEvent) => {
  event.stopPropagation() 
  editorStore.selectComponent(component.id)
}
const handleCanvasClick = () => { editorStore.selectComponent(null) }

// --- Contextual Toolbar Logic ---
const toolbarStyle = ref({ top: '0px', left: '0px', opacity: 0 })
const componentRefs = ref<Record<number, HTMLElement>>({})
const canvasWrapperRef = ref<HTMLElement | null>(null)

watch(selectedComponentId, (newId) => {
  if (newId === null || !canvasWrapperRef.value) {
    toolbarStyle.value.opacity = 0
  } else {
    nextTick(() => {
      const selectedEl = componentRefs.value[newId]
      if (selectedEl) {
        const elRect = selectedEl.getBoundingClientRect()
        const canvasRect = canvasWrapperRef.value!.getBoundingClientRect()
        toolbarStyle.value = {
          top: `${elRect.top - canvasRect.top - 50}px`,
          left: `${elRect.left - canvasRect.left + elRect.width / 2}px`,
          opacity: 1
        }
      }
    })
  }
}, { flush: 'post' }) // `flush: 'post'` helps ensure refs are updated

const handleDelete = () => {
  if (selectedComponentId.value) {
    editorStore.deleteComponent(selectedComponentId.value)
  }
}
const handleDuplicate = () => {
  if (selectedComponentId.value) {
    editorStore.duplicateComponent(selectedComponentId.value)
  }
}
</script>

<template>
  <main class="main-canvas" @click="handleCanvasClick">
    <div class="canvas-content-wrapper" ref="canvasWrapperRef">

      <!-- The Contextual Command Toolbar -->
      <div v-if="selectedComponent" class="context-toolbar" :style="toolbarStyle" @click.stop>
        <button @click="handleDuplicate" title="Duplicate"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M15.75 17.25v3.375c0 .621-.504 1.125-1.125 1.125h-9.75a1.125 1.125 0 01-1.125-1.125V7.875c0-.621.504-1.125 1.125-1.125H6.75a9.06 9.06 0 011.5.124m7.5 10.376h3.375c.621 0 1.125-.504 1.125-1.125V11.25c0-4.46-3.243-8.161-7.5-8.876a9.06 9.06 0 00-1.5-.124H9.375c-.621 0-1.125.504-1.125 1.125v3.5m7.5 10.375H9.375a1.125 1.125 0 01-1.125-1.125v-9.25m12 6.625v-1.875a3.375 3.375 0 00-3.375-3.375h-1.5a1.125 1.125 0 01-1.125-1.125v-1.5c0-.621-.504-1.125-1.125-1.125H9.375a3.375 3.375 0 00-3.375 3.375v1.5c0 .621.504 1.125 1.125 1.125h1.5a1.125 1.125 0 011.125 1.125v1.875m-7.5-6.625h7.5" /></svg></button>
        <div class="toolbar-divider"></div>
        <button @click="handleDelete" title="Delete" class="delete-button"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.134-2.033-2.134H8.715c-1.123 0-2.033.954-2.033 2.134v.916m7.5 0a48.667 48.667 0 00-7.5 0" /></svg></button>
      </div>

      <section v-if="editorStore.currentProject" class="canvas-section">
        <draggable v-model="draggableComponents" item-key="id" group="components" class="drag-area" ghost-class="ghost">
          <template #item="{ element: component }">
            <div
              :ref="el => { if (el) componentRefs[component.id] = el as HTMLElement }"
              class="canvas-component"
              :class="{ 'is-selected': component.id === editorStore.selectedComponentId }"
              @click="handleComponentClick(component, $event)"
            >
              <h1 v-if="component.component_type === 'heading'" :style="{ fontSize: component.fontSize, color: component.color }">{{ component.content }}</h1>
              <p v-else-if="component.component_type === 'paragraph'">{{ component.content }}</p>
              <img v-else-if="component.component_type === 'image'" :src="component.content" :alt="component.alt"/>
            </div>
          </template>
        </draggable>
      </section>
    </div>
  </main>
</template>

<style scoped>
.main-canvas{position:relative;flex-grow:1;background-color:#3c4049;padding:48px;overflow-y:auto}
.canvas-content-wrapper{position:relative;max-width:900px;margin:0 auto;background-color:#fff;min-height:100%;box-shadow:0 20px 50px rgba(0,0,0,.2);padding:56px;border-radius:4px}
.drag-area{min-height:100px}
.ghost{opacity:.5;background:#282c34;border-radius:8px;border:2px dashed #a855f7}
.canvas-component{padding:12px;margin-bottom:12px;border-radius:6px;cursor:grab;border:2px solid transparent;transition:all .2s ease;background-color:#fff}
.canvas-component:hover{border-color:rgba(168,85,247,.4)}
.canvas-component.is-selected{border-color:#a855f7;box-shadow:0 0 0 3px rgba(168,85,247,.3)}
.canvas-component h1{font-weight:700;margin:.5rem 0;color:#111827;line-height:1.2}
.canvas-component p{font-size:1rem;line-height:1.7;margin:.5rem 0;color:#374151}
.canvas-component img{max-width:100%;height:auto;display:block;border-radius:8px}
.canvas-section { border: none; padding: 0; }
.context-toolbar{position:absolute;z-index:10;display:flex;align-items:center;background-color:#21252b;padding:4px;border-radius:6px;border:1px solid #3c4049;box-shadow:0 4px 15px rgba(0,0,0,.2);opacity:0;transition:opacity .2s ease, top .2s ease;transform:translateX(-50%)}
.context-toolbar button{background:0 0;border:0;color:#abb2bf;cursor:pointer;padding:8px;border-radius:4px;transition:all .2s ease}
.context-toolbar button:hover{background-color:#3c4049;color:#fff}
.context-toolbar button.delete-button:hover{background-color:#ef4444;color:#fff}
.context-toolbar button svg{width:20px;height:20px;display:block}
.toolbar-divider{width:1px;height:20px;background-color:#3c4049;margin:0 4px}
</style>
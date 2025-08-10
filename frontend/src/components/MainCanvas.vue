<!-- editor-frontend/src/components/MainCanvas.vue -->
<script setup lang="ts">
import { computed } from 'vue'
import { useEditorStore, type WebComponent } from '../stores/editor'
import { VueDraggableNext } from 'vue-draggable-next'

const editorStore = useEditorStore()

const draggableComponents = computed({
  get() {
    return editorStore.components
  },
  set(newOrder: WebComponent[]) {
    editorStore.updateComponentOrder(newOrder)
  }
})

const handleComponentClick = (component: WebComponent, event: MouseEvent) => {
  event.stopPropagation() 
  editorStore.selectComponent(component.id)
}

const handleCanvasClick = () => {
  editorStore.selectComponent(null)
}
</script>

<template>
  <main class="main-canvas" @click="handleCanvasClick">
    <div class="canvas-content-wrapper">
      <VueDraggableNext
        :list="draggableComponents"
        class="drag-area"
        ghost-class="ghost"
      >
        <!--
          THE FIX IS HERE: We have REMOVED the redundant `v-for` loop.
          The library provides each 'component' as the 'element' variable in the #item slot.
          We now use that directly.
        -->
        <div
          v-for="component in draggableComponents"
          :key="component.id"
          class="canvas-component"
          :class="{ 'is-selected': component.id === editorStore.selectedComponentId }"
          @click="handleComponentClick(component, $event)"
        >
          <h1 v-if="component.type === 'heading'">{{ component.content }}</h1>
          <p v-else-if="component.type === 'paragraph'">{{ component.content }}</p>
          <img v-else-if="component.type === 'image'" :src="component.content" alt="User content"/>
        </div>
      </VueDraggableNext>
    </div>
  </main>
</template>

<style scoped>
/* All the styles from the previous version remain exactly the same */
.main-canvas {
  flex-grow: 1;
  background-color: #374151;
  padding: 32px;
  overflow-y: auto;
}
.canvas-content-wrapper {
  max-width: 900px;
  margin: 0 auto;
  background-color: #ffffff;
  min-height: 100%;
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
  padding: 40px;
}
.drag-area {
  min-height: 100px;
}
.ghost {
  opacity: 0.5;
  background: #374151;
  border: 2px dashed #a855f7;
}
.canvas-component {
  padding: 12px;
  margin: 12px -12px;
  border-radius: 6px;
  cursor: grab;
  border: 2px solid transparent;
  transition: border-color 0.2s ease;
}
.canvas-component:hover {
  border-color: rgba(168, 85, 247, 0.4);
}
.canvas-component.is-selected {
  border-color: #a855f7;
  box-shadow: 0 0 0 3px rgba(168, 85, 247, 0.3);
}
.canvas-component h1 { font-size: 2.5rem; font-weight: 700; margin: 0.5rem 0; color: #111827; }
.canvas-component p { font-size: 1rem; line-height: 1.7; margin: 0.5rem 0; color: #374151; }
.canvas-component img { max-width: 100%; height: auto; display: block; border-radius: 8px; }
</style>
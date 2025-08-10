<!-- frontend/src/components/MainCanvas.vue -->
<script setup lang="ts">
import { computed } from 'vue'
import { useEditorStore, type Component } from '../stores/editor'
import draggable from 'vuedraggable'

const editorStore = useEditorStore()

// This computed property provides a robust, two-way binding to our store's component list.
// This is the industry-standard way to connect vuedraggable to a state management library.
const draggableComponents = computed({
  get() {
    // We get the list of components from the store.
    return editorStore.currentProject?.components || []
  },
  set(newComponents: Component[]) {
    // When the user drags and drops, v-model calls this 'set' method,
    // which directly updates the store with the new order.
    if (editorStore.currentProject) {
      editorStore.currentProject.components = newComponents
    }
  }
})

const handleComponentClick = (component: Component, event: MouseEvent) => {
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
      <section v-if="editorStore.currentProject" class="canvas-section">
        <!-- 
          This is the stable, working implementation.
          - v-model provides the two-way binding for both reordering and dropping new items.
          - The group prop connects it to the sidebar.
        -->
        <draggable
          v-model="draggableComponents"
          item-key="id"
          group="components"
          class="drag-area"
          ghost-class="ghost"
        >
          <template #item="{ element: component }">
            <div
              class="canvas-component"
              :class="{ 'is-selected': component.id === editorStore.selectedComponentId }"
              @click="handleComponentClick(component, $event)"
            >
              <h1 v-if="component.component_type === 'heading'">{{ component.content }}</h1>
              <p v-else-if="component.component_type === 'paragraph'">{{ component.content }}</p>
              <img v-else-if="component.component_type === 'image'" :src="component.content" alt="User content"/>
            </div>
          </template>
        </draggable>
      </section>
    </div>
  </main>
</template>

<style scoped>
/* All styles from your repository's version remain the same */
.main-canvas{flex-grow:1;background-color:#3c4049;padding:48px;overflow-y:auto}
.canvas-content-wrapper{max-width:900px;margin:0 auto;background-color:#fff;min-height:100%;box-shadow:0 20px 50px rgba(0,0,0,.2);padding:56px;border-radius:4px}
.drag-area{min-height:100px}
.ghost{opacity:.5;background:#282c34;border-radius:8px;border:2px dashed #a855f7}
.canvas-component{padding:12px;margin-bottom:12px;border-radius:6px;cursor:grab;border:2px solid transparent;transition:all .2s ease;background-color:#fff}
.canvas-component:hover{border-color:rgba(168,85,247,.4)}
.canvas-component.is-selected{border-color:#a855f7;box-shadow:0 0 0 3px rgba(168,85,247,.3)}
.canvas-component h1{font-size:2.5rem;font-weight:700;margin:.5rem 0;color:#111827}
.canvas-component p{font-size:1rem;line-height:1.7;margin:.5rem 0;color:#374151}
.canvas-component img{max-width:100%;height:auto;display:block;border-radius:8px}
.canvas-section { border: none; padding: 0; } /* Cleaning up old debug styles */
</style>
<!-- frontend/src/components/ComponentSidebar.vue -->
<script setup lang="ts">
import { ref } from 'vue'
import draggable from 'vuedraggable'

// This is our palette of available components.
const availableComponents = ref([
  { component_type: 'heading', content: 'New Heading', label: 'Heading' },
  { component_type: 'paragraph', content: 'This is a new paragraph.', label: 'Paragraph' },
  { component_type: 'image', content: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1964', label: 'Image' }
])

// This function creates a fresh copy with a unique ID when an item is cloned.
const cloneComponent = (componentTemplate: any) => {
  return {
    id: Date.now(),
    component_type: componentTemplate.component_type,
    content: componentTemplate.content
  }
}
</script>

<template>
  <aside class="component-sidebar">
    <div class="sidebar-header">Components</div>
    <div class="component-list">
      <!-- 
        This is the stable, well-supported implementation.
        - `:group` with `pull: 'clone'` and `put: false` makes this a one-way source.
        - `:clone` calls our function to create a unique item for the canvas.
        - `:sort="false"` prevents reordering within the sidebar.
      -->
      <draggable
        :list="availableComponents"
        :group="{ name: 'components', pull: 'clone', put: false }"
        :clone="cloneComponent"
        item-key="label"
        :sort="false"
      >
        <template #item="{ element }">
          <div class="component-item">
            {{ element.label }}
          </div>
        </template>
      </draggable>
    </div>
  </aside>
</template>

<style scoped>
/* All styles from your repository's version remain the same */
.component-sidebar{width:240px;background-color:#21252b;border-right:1px solid #3c4049;display:flex;flex-direction:column}
.sidebar-header{padding:16px;font-weight:700;color:#fff;border-bottom:1px solid #3c4049;flex-shrink:0;font-family:'Space Mono',monospace;font-size:1rem}
.component-list{padding:16px}
.component-item{padding:12px 16px;background-color:#282c34;border:1px solid #3c4049;border-radius:6px;color:#abb2bf;font-weight:600;margin-bottom:12px;cursor:grab;transition:all .2s ease}
.component-item:hover{background-color:#3c4049;border-color:#a855f7;color:#fff}
</style>
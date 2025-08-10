<!-- frontend/src/components/MainCanvas.vue -->
<script setup lang="ts">
import { computed } from 'vue'
import { useEditorStore, type Component, type Page } from '../stores/editor'
import draggable from 'vuedraggable'

const editorStore = useEditorStore()

// We create computed properties to provide clean, two-way bindings for our draggable lists.
const pageSections = computed({
  get() {
    // Return the sections of the first page, or an empty array if none exist.
    return editorStore.currentProject?.pages[0]?.sections || []
  },
  set(newSections) {
    if (editorStore.currentProject?.pages[0]) {
      editorStore.currentProject.pages[0].sections = newSections
    }
  }
})

// Click handlers remain the same, they operate on a global selection state.
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
      <div v-if="editorStore.currentProject">
        <!-- 
          OUTER DRAGGABLE: This handles dragging and reordering of whole SECTIONS.
          It listens on the 'editor-sections' group.
        -->
        <draggable
          v-model="pageSections"
          item-key="id"
          group="editor-sections"
          class="sections-drag-area"
          ghost-class="section-ghost"
        >
          <template #item="{ element: section }">
            <section class="canvas-section">
              <div class="section-header">
                <span>{{ section.section_type }}</span>
              </div>
              <!--
                INNER DRAGGABLE: This handles components WITHIN a section.
                It listens on the 'editor-items' group.
              -->
              <draggable
                v-model="section.components"
                item-key="id"
                group="editor-items"
                class="components-drag-area"
                ghost-class="component-ghost"
              >
                <template #item="{ element: component }">
                  <div
                    class="canvas-component"
                    :class="{ 'is-selected': component.id === editorStore.selectedComponentId }"
                    @click="handleComponentClick(component, $event)"
                  >
                    <h1 v-if="component.component_type === 'heading'" :style="component.styles">{{ component.content }}</h1>
                    <p v-else-if="component.component_type === 'paragraph'" :style="component.styles">{{ component.content }}</p>
                    <img v-else-if="component.component_type === 'image'" :src="component.content" alt="User content"/>
                  </div>
                </template>
              </draggable>
            </section>
          </template>
        </draggable>
      </div>
    </div>
  </main>
</template>

<style scoped>
.main-canvas { flex-grow: 1; background-color: #3c4049; padding: 48px; overflow-y: auto; }
.canvas-content-wrapper { max-width: 900px; margin: 0 auto; background-color: #fff; min-height: 100%; box-shadow: 0 20px 50px rgba(0,0,0,.2); padding: 56px; border-radius: 4px; }

/* Styles for the outer (Sections) draggable area */
.sections-drag-area { min-height: 200px; }
.section-ghost {
  height: 100px;
  background: rgba(168, 85, 247, 0.1);
  border: 2px dashed #a855f7;
  border-radius: 12px;
}
.canvas-section {
  border: 1px solid #e5e7eb;
  margin-bottom: 2rem;
  padding: 1.5rem;
  border-radius: 12px;
  background-color: #f9fafb;
}
.section-header {
  font-family: 'Space Mono', monospace;
  color: #9ca3af;
  font-size: 0.8rem;
  text-transform: uppercase;
  margin-bottom: 1.5rem;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid #e5e7eb;
}

/* Styles for the inner (Components) draggable area */
.components-drag-area { min-height: 50px; }
.component-ghost { opacity: .5; background: #e5e7eb; border-radius: 8px; }

.canvas-component { padding: 12px; margin-bottom: 12px; border-radius: 6px; cursor: grab; border: 2px solid transparent; transition: all .2s ease; background-color: #fff; }
.canvas-component:hover { border-color: rgba(168, 85, 247, .4); }
.canvas-component.is-selected { border-color: #a855f7; box-shadow: 0 0 0 3px rgba(168, 85, 247, .3); }
.canvas-component h1 { font-weight: 700; margin: .5rem 0; color: #111827; line-height: 1.2; }
.canvas-component p { font-size: 1rem; line-height: 1.7; margin: .5rem 0; color: #374151; }
.canvas-component img { max-width: 100%; height: auto; display: block; border-radius: 8px; }
</style>
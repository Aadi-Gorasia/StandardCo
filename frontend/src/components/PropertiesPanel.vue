<!-- editor-frontend/src/components/PropertiesPanel.vue -->
<script setup lang="ts">
import { useEditorStore } from '../stores/editor'
import { storeToRefs } from 'pinia'

const editorStore = useEditorStore()
const { selectedComponent } = storeToRefs(editorStore)

const handleContentChange = (event: Event) => {
  if (selectedComponent.value) {
    const target = event.target as HTMLTextAreaElement
    editorStore.updateComponentContent(selectedComponent.value.id, target.value)
  }
}
</script>

<template>
  <aside class="properties-panel">
    <div class="panel-header">Properties</div>
    <div class="panel-content">
      <div v-if="selectedComponent">
        <div class="form-group">
          <label for="component-content">Content</label>
          <textarea
            id="component-content"
            :value="selectedComponent.content"
            @input="handleContentChange"
            rows="5"
          ></textarea>
        </div>
      </div>
      <div v-else class="panel-placeholder">
        <p>Select a component on the canvas to edit its properties.</p>
      </div>
    </div>
  </aside>
</template>

<style scoped>
.properties-panel {
  width: 280px;
  background-color: #111827; /* Dusk: Background Color */
  border-left: 1px solid rgba(255, 255, 255, 0.1); /* Dusk: Border Color */
  display: flex;
  flex-direction: column;
}
.panel-header {
  padding: 16px;
  font-weight: 700;
  color: #f9fafb; /* Dusk: Heading Color */
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  flex-shrink: 0;
  font-family: 'Space Mono', monospace;
  font-size: 1.1rem;
}
.panel-content {
  padding: 16px;
  flex-grow: 1;
}
.panel-placeholder {
  color: #9ca3af; /* Dusk: Subtle Text Color */
  font-size: 0.9rem;
  text-align: center;
  padding-top: 2rem;
}
.form-group {
  margin-bottom: 1rem;
}
.form-group label {
  display: block;
  font-weight: 600;
  margin-bottom: 8px;
  font-size: 0.9rem;
  color: #d1d5db; /* Dusk: Text Color */
}
.form-group textarea {
  width: 100%;
  padding: 8px 12px;
  border-radius: 6px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  background-color: #1f2937; /* Dusk: Surface Color */
  color: #d1d5db;
  font-family: inherit;
  font-size: 1rem;
  resize: vertical;
}
.form-group textarea:focus {
  outline: none;
  border-color: #a855f7; /* Dusk: Primary Color */
  box-shadow: 0 0 0 3px rgba(168, 85, 247, 0.3);
}
</style>
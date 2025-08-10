<!-- frontend/src/components/PropertiesPanel.vue -->
<script setup lang="ts">
import { useEditorStore } from '../stores/editor'
import { storeToRefs } from 'pinia'
import type { Component } from '../stores/editor'

const editorStore = useEditorStore()
const { selectedComponent } = storeToRefs(editorStore)

// This handler is now more flexible, able to update both 'content' and 'styles'.
const handlePropertyChange = (property: 'content' | keyof Component['styles'], event: Event) => {
  const target = event.target as HTMLInputElement | HTMLTextAreaElement
  editorStore.updateComponentProperty(property, target.value)
}
</script>

<template>
  <aside class="properties-panel">
    <div class="panel-header">Properties</div>
    <div class="panel-content">
      
      <div v-if="selectedComponent">
        
        <!-- HEADING-SPECIFIC CONTROLS -->
        <div v-if="selectedComponent.component_type === 'heading'">
          <div class="form-group">
            <label for="content">Content</label>
            <textarea id="content" :value="selectedComponent.content" @input="handlePropertyChange('content', $event)" rows="3"></textarea>
          </div>
          <div class="form-group">
            <label for="font-size">Font Size</label>
            <input type="text" id="font-size" :value="selectedComponent.styles?.fontSize" @input="handlePropertyChange('fontSize', $event)">
          </div>
          <div class="form-group">
            <label for="color">Color</label>
            <input type="color" id="color" :value="selectedComponent.styles?.color" @input="handlePropertyChange('color', $event)" class="color-input">
          </div>
        </div>

        <!-- PARAGRAPH-SPECIFIC CONTROLS -->
        <div v-else-if="selectedComponent.component_type === 'paragraph'">
          <div class="form-group">
            <label for="content">Content</label>
            <textarea id="content" :value="selectedComponent.content" @input="handlePropertyChange('content', $event)" rows="8"></textarea>
          </div>
        </div>
        
        <!-- IMAGE-SPECIFIC CONTROLS -->
        <div v-else-if="selectedComponent.component_type === 'image'">
          <p class="info-text">Image properties are not yet editable.</p>
        </div>

      </div>

      <div v-else class="panel-placeholder">
        <p>Select a component to edit its properties.</p>
      </div>
    </div>
  </aside>
</template>

<style scoped>
/* All styles from the previous correct version remain the same */
.properties-panel{width:280px;background-color:#21252b;border-left:1px solid #3c4049;display:flex;flex-direction:column}
.panel-header{padding:16px;font-weight:700;color:#fff;border-bottom:1px solid #3c4049;flex-shrink:0;font-family:'Space Mono',monospace;font-size:1rem}
.panel-content{padding:16px;flex-grow:1;overflow-y:auto}
.panel-placeholder{color:#6b7280;font-size:.9rem;text-align:center;padding-top:2rem}
.form-group{margin-bottom:1.25rem}
.form-group label{display:block;font-weight:600;margin-bottom:8px;font-size:.9rem;color:#abb2bf}
.form-group input, .form-group textarea{width:100%;padding:8px 12px;border-radius:6px;border:1px solid #3c4049;background-color:#282c34;color:#abb2bf;font-family:inherit;font-size:1rem}
.form-group textarea{resize:vertical}
.form-group input:focus, .form-group textarea:focus{outline:0;border-color:#a855f7;box-shadow:0 0 0 3px rgba(168,85,247,.3)}
.info-text{color:#6b7280;font-style:italic;font-size:.85rem;margin-top:.5rem}
.color-input{height:40px;padding:4px 8px}
</style>
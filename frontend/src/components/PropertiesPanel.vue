<!-- frontend/src/components/PropertiesPanel.vue -->
<script setup lang="ts">
import { useEditorStore } from '../stores/editor'
import { storeToRefs } from 'pinia'
import type { Component, Navbar, NavLink } from '../stores/editor'

const editorStore = useEditorStore()
const { selectedComponent } = storeToRefs(editorStore)

// Type assertion for style keys
type StyleKeys = keyof Component['styles'];

// Generic handler for most property changes
const handlePropertyChange = (property: 'content' | StyleKeys, event: Event) => {
  const target = event.target as HTMLInputElement | HTMLTextAreaElement
  if (property === 'fontSize' || property === 'color') {
    editorStore.updateComponentProperty(`styles.${property}`, target.value)
  } else {
    editorStore.updateComponentProperty(property, target.value)
  }
}
// Specific handlers for Navbar links
const handleNavLinkChange = (linkId: number, property: 'text' | 'url', event: Event) => {
    const target = event.target as HTMLInputElement;
    editorStore.updateNavLink(linkId, property, target.value);
}
const handleAddLink = () => { editorStore.addNavLink(); }
const handleDeleteLink = (linkId: number) => { editorStore.deleteNavLink(linkId); }
</script>

<template>
  <aside class="properties-panel">
    <div class="panel-header">Properties</div>
    <div class="panel-content">
      <div v-if="selectedComponent">
        <!-- HEADING CONTROLS -->
        <div v-if="selectedComponent.component_type === 'heading'"><div class="form-group"><label>Content</label><textarea :value="selectedComponent.content" @input="handlePropertyChange('content', $event)" rows="3"></textarea></div><div class="form-group"><label>Font Size</label><input type="text" :value="selectedComponent.styles?.fontSize" @input="handlePropertyChange('fontSize', $event)"></div><div class="form-group"><label>Color</label><input type="color" :value="selectedComponent.styles?.color" @input="handlePropertyChange('color', $event)" class="color-input"></div></div>
        <!-- PARAGRAPH CONTROLS -->
        <div v-else-if="selectedComponent.component_type === 'paragraph'"><div class="form-group"><label>Content</label><textarea :value="selectedComponent.content" @input="handlePropertyChange('content', $event)" rows="8"></textarea></div></div>
        <!-- IMAGE CONTROLS -->
        <div v-else-if="selectedComponent.component_type === 'image'"><p class="info-text">Image properties are not yet editable.</p></div>
        
        <!-- NAVBAR CONTROLS -->
        <div v-else-if="selectedComponent.component_type === 'navbar'">
          <div class="form-group"><label>Site Title</label><input type="text" :value="selectedComponent.content" @input="handlePropertyChange('content', $event)"></div>
          <fieldset class="form-fieldset">
            <legend>Navigation Links</legend>
            <div v-for="link in (selectedComponent as Navbar).links" :key="link.id" class="link-editor-group">
              <input class="link-text-input" type="text" placeholder="Link Text" :value="link.text" @input="handleNavLinkChange(link.id, 'text', $event)">
              <input class="link-url-input" type="text" placeholder="URL" :value="link.url" @input="handleNavLinkChange(link.id, 'url', $event)">
              <button @click="handleDeleteLink(link.id)" class="delete-link-btn" title="Delete Link">&times;</button>
            </div>
            <button @click="handleAddLink" class="add-link-btn">Add Link</button>
          </fieldset>
        </div>
      </div>
      <div v-else class="panel-placeholder"><p>Select a component to edit.</p></div>
    </div>
  </aside>
</template>

<style scoped>
/* THIS IS THE DEFINITIVE, CORRECTED CSS */
.properties-panel { width: 280px; background-color: #21252b; border-left: 1px solid #3c4049; display: flex; flex-direction: column; }
.panel-header { padding: 16px; font-weight: 700; color: #fff; border-bottom: 1px solid #3c4049; flex-shrink: 0; font-family: 'Space Mono', monospace; font-size: 1rem; }
.panel-content { padding: 16px; flex-grow: 1; overflow-y: auto; }
.panel-placeholder { color: #6b7280; font-size: .9rem; text-align: center; padding-top: 2rem; }
.form-group { margin-bottom: 1.25rem; }
.form-group label { display: block; font-weight: 600; margin-bottom: 8px; font-size: .9rem; color: #abb2bf; }
.form-group input, .form-group textarea, .form-group select {
  width: 100%;
  padding: 10px 12px; /* Increased padding */
  border-radius: 6px;
  border: 1px solid #3c4049;
  background-color: #282c34;
  color: #abb2bf;
  font-family: inherit;
  font-size: 1rem;
}
.form-group textarea { resize: vertical; }
.form-group input:focus, .form-group textarea:focus, .form-group select:focus { outline: 0; border-color: #a855f7; box-shadow: 0 0 0 3px rgba(168, 85, 247, .3); }
.info-text { color: #6b7280; font-style: italic; font-size: .85rem; margin-top: .5rem; }
.color-input { height: 44px; padding: 4px 8px; }
.form-fieldset { border: none; padding: 0; margin-top: 2rem; padding-top: 1.5rem; border-top: 1px solid #3c4049; }
.form-fieldset legend { padding: 0 .5rem; margin-left: -.5rem; font-family: 'Space Mono', monospace; font-size: 1rem; font-weight: 700; color: #f9fafb; }

/* Styles for the Navbar link editor */
.link-editor-group { display: flex; gap: 8px; margin-bottom: 12px; align-items: center; }
.link-text-input { flex: 1 1 60%; } /* Give more space to the text input */
.link-url-input { flex: 1 1 40%; } /* Give less space to the URL input */
.add-link-btn { width: 100%; padding: 8px; background-color: #374151; border: 1px solid #4a4f5b; color: #abb2bf; font-weight: 600; border-radius: 6px; cursor: pointer; transition: all .2s ease; margin-top: 8px; }
.add-link-btn:hover { background-color: #4b5563; color: #fff; }
.delete-link-btn { background: transparent; border: none; color: #6b7280; font-size: 1.8rem; line-height: 1; cursor: pointer; padding: 0 4px; transition: color 0.2s ease; font-weight: bold; }
.delete-link-btn:hover { color: #ef4444; }
</style>
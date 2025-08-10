<!-- editor-frontend/src/views/EditorView.vue -->
<script setup lang="ts">
// Note: We've added lang="ts" to the script tag for proper TypeScript support.
import EditorHeader from '../components/EditorHeader.vue'
import ComponentSidebar from '../components/ComponentSidebar.vue'
import PropertiesPanel from '../components/PropertiesPanel.vue'
import MainCanvas from '../components/MainCanvas.vue'
</script>

<template>
  <div class="editor-layout">
    <EditorHeader />
    <div class="editor-main-content">
      <ComponentSidebar />
      <MainCanvas />
      <PropertiesPanel />
    </div>
  </div>
</template>

<style scoped>
.editor-layout {
  display: flex;
  flex-direction: column;
  height: 100vh; /* Make the layout fill the entire screen height */
  overflow: hidden; /* Prevent scrolling on the main layout */
  background-color: #ffffff; /* Explicitly set a background color */
}

.editor-main-content {
  display: flex;
  flex-grow: 1; /* This makes the main content area fill the remaining space */
  height: calc(100vh - 60px); /* Full height minus the header height */
}
</style>
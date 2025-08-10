<!-- editor-frontend/src/components/ComponentSidebar.vue -->
<template>
  <aside class="component-sidebar">
    <div class="sidebar-header">Components</div>
    <div class="component-list">
      <!-- We will make these draggable later -->
      <div class="component-item">Heading</div>
      <div class="component-item">Paragraph</div>
      <div class="component-item">Image</div>
    </div>
  </aside>
</template>

<style scoped>
.component-sidebar {
  width: 240px;
  background-color: #111827; /* Dusk: Background Color */
  border-right: 1px solid rgba(255, 255, 255, 0.1); /* Dusk: Border Color */
  display: flex;
  flex-direction: column;
}
.sidebar-header {
  padding: 16px;
  font-weight: 700;
  color: #f9fafb; /* Dusk: Heading Color */
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  flex-shrink: 0;
  font-family: 'Space Mono', monospace;
  font-size: 1.1rem;
}
.component-list {
  padding: 16px;
}
.component-item {
  padding: 12px 16px;
  background-color: #1f2937; /* Dusk: Surface Color */
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 6px;
  color: #d1d5db; /* Dusk: Text Color */
  font-weight: 600;
  margin-bottom: 12px;
  cursor: grab; /* Indicates this will be draggable */
  transition: all 0.2s ease;
}
.component-item:hover {
  background-color: #374151;
  border-color: #a855f7; /* Dusk: Primary Color */
  color: #fff;
}
</style>
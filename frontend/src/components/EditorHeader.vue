<!-- editor-frontend/src/components/EditorHeader.vue -->
<template>
  <header class="editor-header">
    <div class="logo">Standard Editor</div>
    <div class="actions">
      <button class="action-button">Save</button>
      <button class="action-button primary">Download</button>
    </div>
  </header>
</template>

<style scoped>
.editor-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 24px;
  height: 60px;
  background-color: #1f2937; /* Dusk: Surface Color */
  border-bottom: 1px solid rgba(255, 255, 255, 0.1); /* Dusk: Border Color */
  flex-shrink: 0;
}
.logo {
  font-family: 'Space Mono', monospace;
  font-size: 1.2rem;
  font-weight: 700;
  color: #f9fafb; /* Dusk: Heading Color */
}
.actions {
  display: flex;
  gap: 12px;
}
.action-button {
  padding: 8px 16px;
  border-radius: 6px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  background-color: #374151; /* A darker grey */
  color: #f9fafb;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s ease;
}
.action-button:hover {
  background-color: #4b5563;
}
.action-button.primary {
  background: linear-gradient(45deg, #a855f7, #6366f1); /* Dusk: Primary Gradient */
  color: #ffffff;
  border-color: transparent;
}
</style>
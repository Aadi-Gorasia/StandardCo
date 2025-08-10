<!-- frontend/src/components/ComponentSidebar.vue -->
<script setup lang="ts">
import { ref } from 'vue'
import draggable from 'vuedraggable'

// --- The "Palette" of available items ---

const availableComponents = ref([
  { component_type: 'heading', content: 'New Heading', label: 'Heading', styles: { fontSize: '2.5rem', color: '#111827' }, order: 1 },
  { component_type: 'paragraph', content: 'This is a new paragraph. Write something amazing.', label: 'Paragraph', styles: {}, order: 2 },
  { component_type: 'image', content: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1964', label: 'Image', styles: {}, order: 3 }
])

const availableSections = ref([
  {
    section_type: 'Hero',
    label: 'Hero Section',
    components: [
      { component_type: 'heading', content: 'Your Big, Bold Headline', styles: { fontSize: '3.5rem', color: '#111827' }, order: 1 },
      { component_type: 'paragraph', content: 'A compelling subtitle that explains your value proposition in a single, clear sentence.', styles: {}, order: 2 }
    ]
  },
  {
    section_type: 'FeatureGrid',
    label: '3-Column Grid',
    components: [
      { component_type: 'heading', content: 'Feature One', styles: { fontSize: '1.5rem', color: '#333' }, order: 1 },
      { component_type: 'paragraph', content: 'Describe a key benefit of your product or service.', styles: {}, order: 2 },
      { component_type: 'heading', content: 'Feature Two', styles: { fontSize: '1.5rem', color: '#333' }, order: 3 },
      { component_type: 'paragraph', content: 'Describe another key benefit of your product or service.', styles: {}, order: 4 },
      { component_type: 'heading', content: 'Feature Three', styles: { fontSize: '1.5rem', color: '#333' }, order: 5 },
      { component_type: 'paragraph', content: 'Describe a final key benefit of your product or service.', styles: {}, order: 6 },
    ]
  }
])

// --- The UI State ---
const activeTab = ref<'components' | 'sections'>('components')

// --- Drag-and-Drop Logic ---
const cloneItem = (item: any) => {
  // Deep copy the item and give it a unique ID for tracking
  const newItem = JSON.parse(JSON.stringify(item));
  newItem.id = Date.now();
  // If it's a section, its components also need unique IDs
  if (newItem.components) {
    newItem.components.forEach((comp: any) => comp.id = Date.now() + Math.random());
  }
  return newItem;
}
</script>

<template>
  <aside class="library-panel">
    <div class="panel-header">
      <button :class="{ active: activeTab === 'components' }" @click="activeTab = 'components'">Components</button>
      <button :class="{ active: activeTab === 'sections' }" @click="activeTab = 'sections'">Sections</button>
    </div>
    
    <div class="panel-content">
      <!-- Components Tab -->
      <div v-show="activeTab === 'components'" class="item-list">
        <draggable
          :list="availableComponents"
          :group="{ name: 'editor-items', pull: 'clone', put: false }"
          :clone="cloneItem"
          item-key="label"
          :sort="false"
        >
          <template #item="{ element }">
            <div class="library-item">{{ element.label }}</div>
          </template>
        </draggable>
      </div>

      <!-- Sections Tab -->
      <div v-show="activeTab === 'sections'" class="item-list">
        <draggable
          :list="availableSections"
          :group="{ name: 'editor-sections', pull: 'clone', put: false }"
          :clone="cloneItem"
          item-key="label"
          :sort="false"
        >
          <template #item="{ element }">
            <div class="library-item">{{ element.label }}</div>
          </template>
        </draggable>
      </div>
    </div>
  </aside>
</template>

<style scoped>
.library-panel { width: 280px; background-color: #21252b; border-right: 1px solid #3c4049; display: flex; flex-direction: column; }
.panel-header { display: flex; flex-shrink: 0; border-bottom: 1px solid #3c4049; }
.panel-header button {
  flex: 1;
  padding: 16px;
  background: transparent;
  border: none;
  color: #6b7280;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s ease;
  border-bottom: 2px solid transparent;
}
.panel-header button:hover {
  color: #fff;
}
.panel-header button.active {
  color: #fff;
  border-bottom-color: #a855f7;
}
.panel-content { padding: 16px; overflow-y: auto; }
.library-item {
  padding: 12px 16px;
  background-color: #282c34;
  border: 1px solid #3c4049;
  border-radius: 6px;
  color: #abb2bf;
  font-weight: 600;
  margin-bottom: 12px;
  cursor: grab;
  transition: all 0.2s ease;
}
.library-item:hover {
  background-color: #3c4049;
  border-color: #a855f7;
  color: #fff;
}
</style>
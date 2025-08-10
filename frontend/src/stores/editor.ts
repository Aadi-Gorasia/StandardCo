// frontend/src/stores/editor.ts
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

// This is the correct, simplified structure from your repo
export interface Component {
  id: number
  component_type: 'heading' | 'paragraph' | 'image'
  content: string
}
export interface Project {
  id: number
  name: string
  components: Component[]
}

export const useEditorStore = defineStore('editor', () => {
  const currentProject = ref<Project | null>({
    id: 1,
    name: 'Phoenix Alpha',
    components: [
      { id: 1, component_type: 'heading', content: 'Welcome to the Phoenix Editor.' },
      { id: 2, component_type: 'paragraph', content: 'Drag components from the left and drop them here. Click to edit on the right.' },
      { id: 3, component_type: 'image', content: 'https://images.unsplash.com/photo-1555949963-ff98c6258fa9?q=80&w=2070' },
    ]
  });
  const selectedComponentId = ref<number | null>(null);

  const selectedComponent = computed((): Component | undefined => {
    return currentProject.value?.components.find(c => c.id === selectedComponentId.value);
  });

  function selectComponent(id: number | null) {
    selectedComponentId.value = id;
  }
  function updateComponentContent(id: number, newContent: string) {
    if (selectedComponent.value) {
      selectedComponent.value.content = newContent;
    }
  }
  
  return {
    currentProject,
    selectedComponentId,
    selectedComponent,
    selectComponent,
    updateComponentContent,
  }
});
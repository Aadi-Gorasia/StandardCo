// frontend/src/stores/editor.ts
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

// The upgraded component interface
export interface Component {
  id: number
  component_type: 'heading' | 'paragraph' | 'image'
  content: string
  fontSize?: string
  color?: string
  alt?: string
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
      { id: 1, component_type: 'heading', content: 'Welcome to the Phoenix Editor.', fontSize: '2.5rem', color: '#111827' },
      { id: 2, component_type: 'paragraph', content: 'Drag components. Drop them. Click to edit.' },
      { id: 3, component_type: 'image', content: 'https://images.unsplash.com/photo-1555949963-ff98c6258fa9?q=80&w=2070', alt: 'A laptop with code on the screen' },
    ]
  });
  const selectedComponentId = ref<number | null>(null);

  const selectedComponent = computed(() => {
    return currentProject.value?.components.find(c => c.id === selectedComponentId.value);
  });

  function selectComponent(id: number | null) {
    selectedComponentId.value = id;
  }

  // A powerful, generic action to update ANY property
  function updateComponentProperty(property: keyof Component, value: any) {
    if (selectedComponent.value) {
      const componentToUpdate = selectedComponent.value as any;
      componentToUpdate[property] = value;
    }
  }

  // Action to delete a component
  function deleteComponent(componentId: number) {
    if (currentProject.value) {
      const index = currentProject.value.components.findIndex(c => c.id === componentId);
      if (index > -1) {
        currentProject.value.components.splice(index, 1);
        if (selectedComponentId.value === componentId) {
          selectedComponentId.value = null;
        }
      }
    }
  }

  // Action to duplicate a component
  function duplicateComponent(componentId: number) {
    if (currentProject.value) {
      const originalComponent = currentProject.value.components.find(c => c.id === componentId);
      const index = currentProject.value.components.findIndex(c => c.id === componentId);
      if (originalComponent && index > -1) {
        const newComponent = JSON.parse(JSON.stringify(originalComponent));
        newComponent.id = Date.now();
        currentProject.value.components.splice(index + 1, 0, newComponent);
      }
    }
  }
  
  return { 
    currentProject, 
    selectedComponentId, 
    selectedComponent, 
    selectComponent, 
    updateComponentProperty,
    deleteComponent,
    duplicateComponent,
  }
});
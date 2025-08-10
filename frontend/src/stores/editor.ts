// frontend/src/stores/editor.ts
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

// --- SINGLE SOURCE OF TRUTH FOR TYPES ---
// These now perfectly match our Django API models.
export interface Component {
  id: number
  component_type: 'heading' | 'paragraph' | 'image'
  content: string
  styles: {
    fontSize?: string
    color?: string
  }
  order: number
}
export interface Section {
  id: number
  section_type: string
  order: number
  components: Component[]
}
export interface Page {
  id: number
  name: string
  sections: Section[]
}
export interface Project {
  id: number
  name: string
  pages: Page[]
}

export const useEditorStore = defineStore('editor', () => {
  // --- STATE ---
  // The state now reflects the full, nested structure.
  const currentProject = ref<Project | null>({
    id: 1,
    name: 'Phoenix Alpha',
    pages: [
      {
        id: 1,
        name: 'Home',
        sections: [
          {
            id: 1,
            section_type: 'Hero',
            order: 1,
            components: [
              { id: 1, component_type: 'heading', content: 'Welcome to the Phoenix Editor.', styles: { fontSize: '2.5rem', color: '#111827' }, order: 1 },
              { id: 2, component_type: 'paragraph', content: 'You can now drag and drop entire sections, or individual components within a section.', styles: {}, order: 2 },
            ]
          }
        ]
      }
    ]
  });
  const selectedComponentId = ref<number | null>(null);

  // --- GETTERS ---
  const selectedComponent = computed((): Component | undefined => {
    if (!currentProject.value || selectedComponentId.value === null) return undefined;
    // We must now loop through pages and sections to find the selected component
    for (const page of currentProject.value.pages) {
      for (const section of page.sections) {
        const component = section.components.find(c => c.id === selectedComponentId.value);
        if (component) return component;
      }
    }
    return undefined;
  });

  // --- ACTIONS ---
  function selectComponent(id: number | null) {
    selectedComponentId.value = id;
  }

  function updateComponentProperty(property: keyof Component['styles'] | 'content', value: any) {
    if (selectedComponent.value) {
        if (property === 'content') {
            selectedComponent.value.content = value;
        } else {
            selectedComponent.value.styles[property] = value;
        }
    }
  }

  function addComponent(sectionId: number, component: Omit<Component, 'id'>) {
    if (currentProject.value?.pages[0]) {
        const section = currentProject.value.pages[0].sections.find(s => s.id === sectionId);
        if (section) {
            const newComponent: Component = {
                id: Date.now(),
                ...component
            };
            section.components.push(newComponent);
        }
    }
  }

  return {
    currentProject,
    selectedComponentId,
    selectedComponent,
    selectComponent,
    updateComponentProperty,
    addComponent,
  }
});
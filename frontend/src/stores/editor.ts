// frontend/src/stores/editor.ts
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

// --- UPGRADED TYPES ---
export interface NavLink {
  id: number
  text: string
  url: string
}

export interface Navbar {
  id: number
  component_type: 'navbar'
  content: string // This will be the Site Title
  links: NavLink[]
}

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

// THE CHANGE IS HERE: A Page now has a dedicated, optional navbar property.
export interface Page {
  id: number
  name: string
  navbar: Navbar | null
  sections: Section[]
}

export interface Project {
  id: number
  name: string
  pages: Page[]
}

export const useEditorStore = defineStore('editor', () => {
  // --- STATE ---
  const currentProject = ref<Project | null>({
    id: 1,
    name: 'Phoenix Alpha',
    pages: [
      {
        id: 1,
        name: 'Home',
        // The navbar is now a first-class citizen of the page
        navbar: {
          id: 100, // A unique ID
          component_type: 'navbar',
          content: 'Standard',
          links: [
            { id: 1, text: 'Home', url: '#' },
            { id: 2, text: 'About', url: '#' },
            { id: 3, text: 'Contact', url: '#' },
          ]
        },
        // The sections are now separate
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
  const selectedComponent = computed((): Component | Navbar | undefined => {
    if (!currentProject.value || selectedComponentId.value === null) return undefined;
    for (const page of currentProject.value.pages) {
      // First, check if the selected component is the navbar
      if (page.navbar?.id === selectedComponentId.value) {
        return page.navbar;
      }
      // If not, search within the sections
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

  function updateComponentProperty(property: keyof Component | 'content' | `styles.${keyof Component['styles']}`, value: any) {
    if (!selectedComponent.value) return;
    
    // Handle style updates
    if (typeof property === 'string' && property.startsWith('styles.')) {
        const styleKey = property.split('.')[1] as keyof Component['styles'];
        if ('styles' in selectedComponent.value && selectedComponent.value.styles) {
            selectedComponent.value.styles[styleKey] = value;
        }
    } 
    // Handle all other property updates
    else if ('content' === property) {
        (selectedComponent.value as Component | Navbar).content = value;
    }
  }

  function addNavLink() {
    const navbar = currentProject.value?.pages[0]?.navbar;
    if (navbar) {
      if (!navbar.links) navbar.links = [];
      navbar.links.push({ id: Date.now(), text: 'New Link', url: '#' });
    }
  }

  function updateNavLink(linkId: number, property: 'text' | 'url', value: string) {
    const navbar = currentProject.value?.pages[0]?.navbar;
    if (navbar?.links) {
      const link = navbar.links.find(l => l.id === linkId);
      if (link) {
        link[property] = value;
      }
    }
  }

  function deleteNavLink(linkId: number) {
    const navbar = currentProject.value?.pages[0]?.navbar;
    if (navbar?.links) {
      navbar.links = navbar.links.filter(l => l.id !== linkId);
    }
  }
  
  return {
    currentProject,
    selectedComponentId,
    selectedComponent,
    selectComponent,
    updateComponentProperty,
    addNavLink,
    updateNavLink,
    deleteNavLink
  }
});
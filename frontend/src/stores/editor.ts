// editor-frontend/src/stores/editor.ts

import { defineStore } from 'pinia'

// Define a type for our components for TypeScript
export interface WebComponent {
  id: number
  type: 'heading' | 'paragraph' | 'image' // Added 'image' type
  content: string
}

export const useEditorStore = defineStore('editor', {
  state: () => ({
    components: [
      { id: 1, type: 'heading', content: 'Your Awesome Headline' },
      { id: 2, type: 'paragraph', content: 'This is a paragraph. Click me to edit my text!' },
      { id: 3, type: 'image', content: 'https://via.placeholder.com/800x400' } // Added a placeholder image component
    ] as WebComponent[],
    selectedComponentId: null as number | null,
  }),

  getters: {
    selectedComponent: (state) => {
      return state.components.find(c => c.id === state.selectedComponentId)
    }
  },

  actions: {
    selectComponent(id: number | null) {
      this.selectedComponentId = id
    },
    updateComponentContent(id: number, newContent: string) {
      const component = this.components.find(c => c.id === id)
      if (component) {
        component.content = newContent
      }
    },
    // NEW: This action updates the order of the components array
    updateComponentOrder(newOrder: WebComponent[]) {
        this.components = newOrder
    }
  }
})
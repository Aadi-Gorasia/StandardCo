// editor-frontend/vite.config.ts

import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  // THE FIX IS HERE: This block tells Vite how to build our files for Django.
  build: {
    // This is the folder where the built files will be placed.
    outDir: '../static/vite', 
    // This tells Vite to create a 'manifest' file, which Django will use to find the assets.
    manifest: true,
    rollupOptions: {
      // This tells Vite where to put the final index.html file.
      input: {
        main: fileURLToPath(new URL('./src/main.ts', import.meta.url))
      }
    }
  }
})
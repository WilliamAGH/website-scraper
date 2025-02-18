import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'
import path from 'path'

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    port: process.env.APP_PORT ? parseInt(process.env.APP_PORT) : 3000,
    host: true,
    strictPort: true,
    proxy: {
      '/api': {
        target: process.env.API_URL || 'http://localhost:5000',
        changeOrigin: true,
        secure: false,
      },
    },
    allowedHosts: true,
    hmr: {
      clientPort: 443
    }
  },
})
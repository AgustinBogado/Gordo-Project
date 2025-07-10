//Desarrollo
npm run dev      # levanta el servidor Vite en localhost:5173
npm run start    # abre la ventana Electron apuntando a http://localhost:5173

//Produccion
npm run build-renderer   # genera dist/renderer/index.html + assets (bundle.js, css...)
npm run start            # ahora carga desde dist/renderer/index.html

//Crear ejecutable
npm run dist

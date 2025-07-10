// preload.js
const { contextBridge, ipcRenderer } = require('electron');
const fs = require('fs');
const ExcelJS = require('exceljs');

contextBridge.exposeInMainWorld('api', {
  leerExcel: async (rutaExcel) => {
    const workbook = new ExcelJS.Workbook();
    await workbook.xlsx.readFile(rutaExcel);
    const hoja = workbook.worksheets[0];
    const datos = [];
    hoja.eachRow({ includeEmpty: false }, (row, rowNumber) => {
      if (rowNumber === 1) return;

      const [nombre, precio, marca] = row.values.slice(1);
      datos.push({ nombre, precio, marca });
    });
    return datos;
  },

  parsearPDF: async (rutaPDF) => {
    const data = fs.readFileSync(rutaPDF);
    const { text } = await pdfParse(data);
    // Aquí podrías aplicar tu lógica para extraer productos, precios, etc.
    return text;
  },

  generarPDF: (productos, rutaSalida) => {
    const doc = new PDFDocument();
    const stream = fs.createWriteStream(rutaSalida);
    doc.pipe(stream);
    doc.fontSize(14).text('Catálogo de Productos', { align: 'center' });
    productos.forEach(p => {
      doc.moveDown().text(`${p.nombre} — $${p.precio}`);
    });
    doc.end();
    return new Promise(res => stream.on('finish', res));
  }
});

// processor.js
const ExcelJS = require('exceljs');

async function leerExcel(filePath) {
  const wb = new ExcelJS.Workbook();
  await wb.xlsx.readFile(filePath);
  const sheet = wb.worksheets[0];
  const rows = [];
  sheet.eachRow((row, rowNumber) => {
    // asume columnas: Producto (A), Precio (B), Marca (C), etc.
    rows.push({
      Producto: row.getCell(1).value,
      Precio: row.getCell(2).value,
      Marca:   row.getCell(3).value
    });
  });
  return rows;
}

module.exports = { leerExcel };

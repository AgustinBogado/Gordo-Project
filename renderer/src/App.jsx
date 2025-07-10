import { useState } from 'react';
import { FileText, History, Folder, Download, FileSpreadsheet } from 'lucide-react';

function App() {
  const [selectedPriceList, setSelectedPriceList] = useState('');
  const [selectedPrevious, setSelectedPrevious] = useState('');
  const [selectedFolder, setSelectedFolder] = useState('');

  const handlePriceListSelect = () => {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = '.xlsx,.xls,.pdf';
    input.onchange = (e) => {
      const file = e.target.files?.[0];
      if (file) setSelectedPriceList(file.name);
    };
    input.click();
  };

  const handlePreviousSelect = () => {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = '.pdf';
    input.onchange = (e) => {
      const file = e.target.files?.[0];
      if (file) setSelectedPrevious(file.name);
    };
    input.click();
  };

  const handleFolderSelect = () => {
    if ('showDirectoryPicker' in window) {
      window.showDirectoryPicker()
        .then(dir => setSelectedFolder(dir.name))
        .catch(() => {});
    } else {
      const input = document.createElement('input');
      input.type = 'file';
      input.webkitdirectory = true;
      input.onchange = (e) => {
        const files = e.target.files;
        if (files?.length) {
          const path = files[0].webkitRelativePath.split('/')[0];
          setSelectedFolder(path);
        }
      };
      input.click();
    }
  };

  const handleGeneratePDF = () => {
    // aquí iría tu llamada a window.api u otra lógica
    alert('¡PDF Generator activado! Aquí implementarás tu lógica.');
  };

  const buttons = [
    { id: 'price-list',    label: 'Lista de precios',  icon: FileSpreadsheet, onClick: handlePriceListSelect, description: 'Seleccionar Excel o PDF', selected: selectedPriceList },
    { id: 'previous-list', label: 'Lista anterior',    icon: History,        onClick: handlePreviousSelect,  description: 'Seleccionar PDF anterior', selected: selectedPrevious },
    { id: 'choose-folder', label: 'Elegir carpeta',    icon: Folder,         onClick: handleFolderSelect,   description: 'Carpeta de destino',       selected: selectedFolder },
    { id: 'generate-pdf',  label: 'Generar PDF',       icon: Download,       onClick: handleGeneratePDF,    description: 'Crear nuevo PDF',          selected: '' },
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-blue-900 to-slate-800 flex items-center justify-center p-8">
      <div className="w-full max-w-md">
        {/* Header */}
        <div className="flex flex-row items-center justify-center mb-8 mr-16">
          <div className="w-16 h-16 bg-gradient-to-br from-blue-400 to-cyan-300 rounded-2xl flex items-center justify-center mx-auto mb-4 shadow-lg">
            <FileText className="w-8 h-8 text-slate-900" />
          </div>
          <div className="text-center mb-4">
            <h1 className="text-3xl font-bold text-white mb-2">Listas Launcher</h1>
            <p className="text-blue-200 text-sm">Generador de listas de precios</p>
          </div>
        </div>
        {/* Buttons */}
        <div className="space-y-4">
          {buttons.map(btn => {
            const Icon = btn.icon;
            return (
              <button
                key={btn.id}
                onClick={btn.onClick}
                className="w-full bg-slate-800/50 backdrop-blur-sm border border-slate-700/50 rounded-xl p-6 text-left transition-all duration-300 hover:bg-gradient-to-r hover:from-cyan-500/20 hover:to-blue-500/20 hover:border-cyan-400/50 hover:shadow-lg hover:shadow-cyan-500/25 hover:scale-105 group"
              >
                <div className="flex items-center space-x-4">
                  <div className="w-12 h-12 bg-slate-700/50 rounded-lg flex items-center justify-center group-hover:bg-cyan-500/20 transition-colors duration-300">
                    <Icon className="w-6 h-6 text-blue-300 group-hover:text-cyan-300 transition-colors duration-300" />
                  </div>
                  <div className="flex-1 min-w-0">
                    <h3 className="text-white font-semibold text-lg group-hover:text-cyan-100">{btn.label}</h3>
                    <p className="text-slate-400 text-sm group-hover:text-cyan-200">{btn.description}</p>
                    {btn.selected && <p className="text-cyan-400 text-xs mt-1 truncate">{btn.selected}</p>}
                  </div>
                </div>
              </button>
            );
          })}
        </div>
      </div>
    </div>
  );
}

export default App;

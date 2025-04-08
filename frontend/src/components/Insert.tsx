import { useRef, useState } from "react";
import axios from "axios";

import { registerAllModules } from "handsontable/registry";
import { HotTable, HotTableRef } from "@handsontable/react-wrapper";
import Handsontable from "handsontable";

registerAllModules();

function Insert() {
  const [tableData, setTableData] = useState([[null]]);
  const hotRef = useRef<HotTableRef>(null);

  async function sendTableData(data: Handsontable.CellValue[]) {
    try {
      await axios.post(
        "http://127.0.0.1:8000/ppto",
        { table: data },
        {
          headers: { "Content-Type": "application/json" },
        },
      );
    } catch (error) {
      console.error("Error:", error);
    }
  }

  return (
    <div className="flex h-full w-full flex-col">
      <span className="p-4 text-3xl">Let's Insert!</span>
      {/* Hands On Table Component */}
      <div className="ht-theme-main overflow-y-auto">
        <HotTable
          ref={hotRef}
          // hot reloads the sheet with every change
          afterChange={function (
            changes: Handsontable.CellChange[] | null,
            source: Handsontable.ChangeSource,
          ) {
            const hot = hotRef.current?.hotInstance;
            if (changes && source !== "loadData" && hot) {
              let newTable = hot.getData();
              // sendTableData(newTable);
            }
          }}
          data={tableData}
          columns={[
            { type: "text" }, // Nombre
            { type: "text" }, // Consorcio
            { type: "text" }, // Empresa
            {
              type: "numeric", // Monto
              className: "htRight",
              allowInvalid: false,
              numericFormat: { pattern: "0,0.00" },
            },
            { type: "text" }, // Entidad
            {
              type: "date", // Fecha de Contrato
              dateFormat: "DD/MM/YYYY",
              correctFormat: true,
            },
            {
              type: "date", // Fecha de Recepción
              dateFormat: "DD/MM/YYYY",
              correctFormat: true,
            },
          ]}
          rowHeaders={false}
          colHeaders={[
            "Nombre",
            "Consorcio",
            "Empresa",
            "Monto",
            "Entidad",
            "Fecha de Contrato",
            "Fecha de Recepción",
          ]}
          autoWrapRow={true}
          autoWrapCol={true}
          licenseKey="non-commercial-and-evaluation"
          minSpareRows={1}
          stretchH="all"
          width="100%"
          height="auto"
          contextMenu={{
            items: {
              copy: {},
              cut: {},
              "---------": {},
              row_above: {},
              row_below: {},
              remove_row: {},
            },
          }}
          hiddenColumns={{
            columns: [],
            indicators: true,
            copyPasteEnabled: false,
          }}
          manualColumnMove={false}
          manualColumnFreeze={true}
          manualColumnResize={true}
          filters={false}
          hiddenRows={{
            rows: [],
            indicators: true,
            copyPasteEnabled: false,
          }}
          manualRowMove={true}
          manualRowResize={true}
          columnSorting={true}
          mergeCells={true}
        />
      </div>
    </div>
  );
}

export default Insert;

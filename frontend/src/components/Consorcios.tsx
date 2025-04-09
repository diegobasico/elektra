import { useRef, useEffect, useState } from "react";
import axios from "axios";

import { registerAllModules } from "handsontable/registry";
import { HotTable, HotTableRef } from "@handsontable/react-wrapper";
import Handsontable from "handsontable";

registerAllModules();

function Consorcios() {
  const [tableData, setTableData] = useState([[null]]);
  const [consorciosDropdown, setconsorciosDropdown] = useState([]);
  const [empresasDropdown, setEmpresasDropdown] = useState([]);
  const hotRef = useRef<HotTableRef>(null);

  useEffect(() => {
    const fetchDropdowns = async () => {
      try {
        const consorcios = await axios.get("http://localhost:8000/consorcios");
        setconsorciosDropdown(consorcios.data);
        const empresas = await axios.get("http://localhost:8000/empresas");
        setEmpresasDropdown(empresas.data);
      } catch (error) {
        console.error("Error fetching dropdowns:", error);
      }
    };

    fetchDropdowns();
  }, []);

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
            {
              type: "dropdown", // Consorcio
              source: consorciosDropdown,
            },
            {
              type: "dropdown", // Empresa
              source: empresasDropdown,
            },
          ]}
          rowHeaders={false}
          colHeaders={["Consorcio", "Empresa"]}
          autoWrapRow={true}
          autoWrapCol={true}
          licenseKey="non-commercial-and-evaluation"
          minSpareRows={10}
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

export default Consorcios;
